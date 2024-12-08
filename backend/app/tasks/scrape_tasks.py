from app.db import get_db_pool
from scripts.scrape_vikings import scrape_vikings_cast
from scripts.scrape_norseman import scrape_norsemen_cast
import asyncio

async def update_vikings_data(pool):
    data = scrape_vikings_cast()
    async with pool.acquire() as conn:
        for character in data:
            await conn.execute("""
                INSERT INTO vikings_characters (character_name, actor_name, description, image_url)
                VALUES ($1, $2, $3, $4)
                ON CONFLICT (character_name)
                DO UPDATE SET
                    actor_name = EXCLUDED.actor_name,
                    description = EXCLUDED.description,
                    image_url = EXCLUDED.image_url;
            """, character['character'], character['actor'], character['description'], character['image_url'])

async def update_norsemen_data(pool):
    data = scrape_norsemen_cast()
    async with pool.acquire() as conn:
        for character in data:
            await conn.execute("""
                INSERT INTO norsemen_characters (character_name, actor_name, description)
                VALUES ($1, $2, $3)
                ON CONFLICT (character_name)
                DO UPDATE SET
                    actor_name = EXCLUDED.actor_name,
                    description = EXCLUDED.description;
            """, character['character'], character['actor'], character['description'])
