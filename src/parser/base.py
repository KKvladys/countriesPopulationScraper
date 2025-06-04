import os

from src.parser.statistics_times import StatisticsTimesParser
from src.parser.wikipedia import WikipediaParser


def get_parser():
    source = os.getenv("DATA_SOURCE", "wikipedia").lower()

    if source == "wikipedia":
        parser = WikipediaParser()
    elif source == "statistics_times":
        parser = StatisticsTimesParser()
    else:
        raise ValueError(f"Unknown DATA_SOURCE: {source}")

    return parser
