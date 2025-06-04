from bs4 import BeautifulSoup
import requests

from src.database.models.country import Country
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

STAT_TIME_URL = "https://statisticstimes.com/demographics/countries-by-population.php"


class StatisticsTimesParser:
    source_url = STAT_TIME_URL

    def parse(self) -> list[Country]:
        response = requests.get(self.source_url)
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", {"id": "table_id"})

        countries = []
        for row in table.tbody.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) < 8:
                continue

            name = cells[0].find("a")
            if not name:
                continue

            try:
                country = Country(
                    name=name.text.strip(),
                    population=int(cells[1].text.strip().replace(",", "")),
                    region=cells[-1].text.strip()
                )
                countries.append(country)
            except Exception as e:
                logger.error(f"Error parsing row: {e}")
                continue

        return countries
