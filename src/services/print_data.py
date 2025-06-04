import asyncio
from sqlalchemy import text

from database.connection_to_db import get_session
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

QUERY = text("""
    WITH regional_stats AS (
        SELECT
            region,
            SUM(population) AS total_population
        FROM countries
        GROUP BY region
    ),
    max_country AS (
        SELECT DISTINCT ON (region)
            region, name AS max_country, population AS max_population
        FROM countries
        ORDER BY region, population DESC
    ),
    min_country AS (
        SELECT DISTINCT ON (region)
            region, name AS min_country, population AS min_population
        FROM countries
        ORDER BY region, population ASC
    )
    SELECT
        r.region,
        r.total_population,
        mc.max_country,
        mc.max_population,
        mi.min_country,
        mi.min_population
    FROM regional_stats r
    JOIN max_country mc ON r.region = mc.region
    JOIN min_country mi ON r.region = mi.region
    ORDER BY r.total_population DESC;
""")


async def print_aggregated_data():
    async with get_session() as session:
        result = await session.execute(QUERY)
        for row in result:
            logger.info(f"Регіон: {row.region}")
            logger.info(f"  Загальне населення: {row.total_population}")
            logger.info(f"  Найбільша країна: {row.max_country}")
            logger.info(f"  Населення найбільшої країни в регіоні: {row.max_population}")
            logger.info(f"  Найменша країна: {row.min_country}")
            logger.info(f"  Населення найменшої  країни в регіоні: {row.min_population}")
            logger.info("")


if __name__ == "__main__":
    asyncio.run(print_aggregated_data())
