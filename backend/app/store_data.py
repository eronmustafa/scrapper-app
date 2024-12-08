import asyncio
import asyncpg
from scripts.scrape_norseman import scrape_norsemen_cast
from scripts.scrape_vikings import scrape_vikings_cast
from dotenv import load_dotenv
import os
from app.db import get_db_pool

# Load environment variables from .env file
load_dotenv()

# Database configuration from environment variables
DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
}

# Function to check if a record already exists
async def record_exists(conn, table_name, character_name):
    query = f"SELECT EXISTS (SELECT 1 FROM {table_name} WHERE character_name = $1)"
    result = await conn.fetchval(query, character_name)
    return result

# Function to store Vikings data
async def store_vikings_data(pool, data):
    async with pool.acquire() as conn:
        for character in data:
            try:
                # Check if the record already exists
                if not await record_exists(conn, "vikings_characters", character["character"]):
                    await conn.execute(
                        """
                        INSERT INTO vikings_characters (character_name, actor_name, description, image_url)
                        VALUES ($1, $2, $3, $4)
                        """,
                        character["character"],
                        character["actor"],
                        character["description"],
                        character["image_url"],
                    )
                    print(f"Inserted: {character['character']}")
                else:
                    print(f"Skipped (already exists): {character['character']}")
            except Exception as e:
                print(f"Error inserting Vikings character {character['character']}: {e}")

# Function to store Norsemen data
async def store_norsemen_data(pool, data):
    async with pool.acquire() as conn:
        for character in data:
            try:
                # Check if the record already exists
                if not await record_exists(conn, "norsemen_characters", character["character"]):
                    await conn.execute(
                        """
                        INSERT INTO norsemen_characters (character_name, actor_name, description)
                        VALUES ($1, $2, $3)
                        """,
                        character["character"],
                        character["actor"],
                        character["description"],
                    )
                    print(f"Inserted: {character['character']}")
                else:
                    print(f"Skipped (already exists): {character['character']}")
            except Exception as e:
                print(f"Error inserting Norsemen character {character['character']}: {e}")

# Generic function to scrape and store data
async def store_data(scrape_function, table_type):
    """Generic function to scrape and store data."""
    pool = await get_db_pool()
    data = scrape_function()

    if table_type == "vikings":
        await store_vikings_data(pool, data)
    elif table_type == "norsemen":
        await store_norsemen_data(pool, data)

    await pool.close()

# Main function to scrape and store data
async def main():
    # Create database connection pool
    pool = await asyncpg.create_pool(**DB_CONFIG)

    # Scrape and store Vikings data
    print("Scraping Vikings data...")
    vikings_data = scrape_vikings_cast()
    print(f"Scraped {len(vikings_data)} Vikings characters.")
    print("Storing Vikings data...")
    await store_vikings_data(pool, vikings_data)

    # Scrape and store Norsemen data
    print("Scraping Norsemen data...")
    norsemen_data = scrape_norsemen_cast()
    print(f"Scraped {len(norsemen_data)} Norsemen characters.")
    print("Storing Norsemen data...")
    await store_norsemen_data(pool, norsemen_data)

    # Close the pool
    await pool.close()
    print("Data storage complete.")

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
