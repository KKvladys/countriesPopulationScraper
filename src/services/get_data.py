import asyncio
import os

from sqlalchemy import delete
from database.connection_to_db import get_session
from database.models.country import Country
from src.parser.base import get_parser
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

async def load_data():
    async with get_session() as session:
        await session.execute(delete(Country))
        parser = get_parser()
        logger.info(f"Збираємо дані з: {parser.source_url}")
        parsed_data = parser.parse()
        countries = parsed_data
        session.add_all(countries)
        await session.commit()
        logger.info(f"Load {len(countries)} country.")

if __name__ == "__main__":
    asyncio.run(load_data())
