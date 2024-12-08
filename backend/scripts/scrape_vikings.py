import requests
from bs4 import BeautifulSoup
import random
import time
import requests

def scrape_vikings_cast():
    # URL of the History Channel Vikings cast page
    url = "https://www.history.com/shows/vikings/cast"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    time.sleep(random.uniform(1, 3))  # Random delay to prevent bans
    
    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return []
    
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Locate the cast section using the div with the "tile-list tile-boxed" class
    cast_section = soup.find('div', class_='tile-list tile-boxed')
    if not cast_section:
        print("Unable to find cast information on the page.")
        return []
    
    # Locate all list items (li elements) within the section
    cast_items = cast_section.find_all('li')
    if not cast_items:
        print("No cast items found in the section.")
        return []
    
    # Extract individual character details
    characters = []
    for item in cast_items:
        try:
            # Extract the image URL
            img_container = item.find('div', class_='img-container')
            img_url = img_container.find('img')['src'] if img_container else "No image available"
            
            # Extract character name and description
            details = item.find('div', class_='details')
            if not details:
                continue
            
            character_name = details.find('strong').get_text(strip=True)
            description = details.find('small').get_text(strip=True)  # "Played by [Actor Name]"
            
            # Extract the actor name from the description
            if "Played by" in description:
                actor_name = description.replace("Played by", "").strip()
            else:
                actor_name = "Unknown Actor"
            
            # Append to the list
            characters.append({
                'character': character_name,
                'actor': actor_name,
                'description': description,
                'image_url': img_url
            })
        except AttributeError:
            print("Failed to parse a cast item. Skipping...")
    
    return characters

# Run the scraper
vikings_characters = scrape_vikings_cast()

# Display the results
# for character in vikings_characters:
#     print(f"Character: {character['character']}")
#     print(f"Actor: {character['actor']}")
#     print(f"Description: {character['description']}")
#     print(f"Image URL: {character['image_url']}")
#     print("-" * 50)
