from app.celery_app import celery
from app.db import get_db_pool
from scripts.scrape_norseman import scrape_norsemen_cast
from scripts.scrape_vikings import scrape_vikings_cast
import asyncio
from app.store_data import store_data


@celery.task(name="app.tasks.store_data_tasks.scrape_and_store_vikings")
def scrape_and_store_vikings():
    print("Starting Vikings scrape and store task...")
    try:
        data = scrape_vikings_cast()
        if not data or not isinstance(data, list):
            print(f"Scraped Vikings data is invalid: {data}")
            raise ValueError("Invalid data format from scrape_vikings_cast")
        # print(f"Scraped Vikings data: {data}")
        asyncio.run(store_data(scrape_vikings_cast, "vikings"))
    except Exception as e:
        print(f"Error in scrape_and_store_vikings: {e}")


@celery.task(name="app.tasks.store_data_tasks.scrape_and_store_norsemen")
def scrape_and_store_norsemen():
    print("Starting Norsemen scrape and store task...")
    try:
        data = scrape_norsemen_cast()
        if not data or not isinstance(data, list):
            print(f"Scraped Norsemen data is invalid: {data}")
            raise ValueError("Invalid data format from scrape_norsemen_cast")
        print(f"Scraped Norsemen data: {data}")
        asyncio.run(store_data(scrape_norsemen_cast, "norsemen"))
    except Exception as e:
        print(f"Error in scrape_and_store_norsemen: {e}")



async def scrape_and_store_data(scrape_function, table_type):
    """Generic async function to scrape and store data."""
    pool = await get_db_pool()
    try:
        # Scrape the data
        data = scrape_function()
        if not data or not isinstance(data, list):
            raise ValueError(f"Scraped data is invalid: {data}")

        # Log data for debugging
        print(f"Scraped {len(data)} records for {table_type}.")

        # Store data in the appropriate table
        if table_type == "vikings":
            await store_vikings_data(pool, data)
        elif table_type == "norsemen":
            await store_norsemen_data(pool, data)
    except Exception as e:
        print(f"Error in scrape_and_store_data for {table_type}: {e}")
    finally:
        await pool.close()


async def store_vikings_data(pool, data):
    async with pool.acquire() as conn:
        for character in data:
            try:
                await conn.execute("""
                    INSERT INTO vikings_characters (character_name, actor_name, description, image_url)
                    VALUES ($1, $2, $3, $4)
                    ON CONFLICT (character_name) DO NOTHING;
                """, character['character'], character['actor'], character['description'], character['image_url'])
            except Exception as e:
                print(f"Error inserting Vikings character {character['character']}: {e}")
                raise


async def store_norsemen_data(pool, data):
    """Store Norsemen data in the database."""
    async with pool.acquire() as conn:
        for character in data:
            try:
                await conn.execute("""
                    INSERT INTO norsemen_characters (character_name, actor_name, description)
                    VALUES ($1, $2, $3)
                    ON CONFLICT (character_name) DO NOTHING;
                """, character['character'], character['actor'], character['description'])
            except Exception as e:
                print(f"Error inserting Norsemen character {character['character']}: {e}")
