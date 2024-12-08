import requests
from bs4 import BeautifulSoup
import re

def scrape_norsemen_cast():
    # URL of the Wikipedia page
    url = "https://en.wikipedia.org/wiki/Norsemen_(TV_series)"
    
    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return []
    
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the "Cast and characters" section using header text
    cast_section = None
    for header in soup.find_all(['h2', 'h3']):
        if "Cast and characters" in header.text:
            cast_section = header.find_next('ul')
            break
    
    if not cast_section:
        print("Unable to find the 'Cast and characters' section.")
        return []
    
    # Extract individual character details
    characters = []
    for item in cast_section.find_all('li'):
        # Match entries with "as" in the text (actor and character separation)
        if "as" in item.text:
            try:
                actor_name, remainder = item.text.split(" as ", 1)
                # Try splitting for character name and description
                split_remainder = re.split(r',|\.', remainder, maxsplit=1)
                character_name = split_remainder[0].strip()
                description = split_remainder[1].strip() if len(split_remainder) > 1 else "No description available."
                characters.append({
                    'actor': actor_name.strip(),
                    'character': character_name,
                    'description': description
                })
            except ValueError:
                print(f"Could not parse entry: {item.text}")
    
    return characters

# Run the scraper
norsemen_characters = scrape_norsemen_cast()

# Display the results
# for character in norsemen_characters:
#     print(f"Actor: {character['actor']}")
#     print(f"Character: {character['character']}")
#     print(f"Description: {character['description']}")
#     print("-" * 50)
