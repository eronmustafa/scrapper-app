# from ..celery_app import celery
# from app.tasks.scrape_tasks import update_vikings_data, update_norsemen_data
# # tasks/__init__.py
# # from .scrape_tasks import *
# # from .store_data_tasks import *


# @celery.task
# def scrape_and_update_vikings():
#     import asyncio
#     from app.db import get_db_pool
#     pool = asyncio.run(get_db_pool())
#     asyncio.run(update_vikings_data(pool))

# @celery.task
# def scrape_and_update_norsemen():
#     import asyncio
#     from app.db import get_db_pool
#     pool = asyncio.run(get_db_pool())
#     asyncio.run(update_norsemen_data(pool))
