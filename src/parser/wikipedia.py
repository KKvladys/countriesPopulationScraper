import requests
from bs4 import BeautifulSoup
from typing import List, Dict


WIKI_URL = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959"


class WikipediaParser:
    source_url = WIKI_URL

    def parse(self) -> List[Dict[str, str]]:
        response = requests.get(self.source_url)
        soup = BeautifulSoup(response.text, "lxml")

        table = soup.find("table", class_="wikitable")
        rows = table.find_all("tr")[1:]

        data = []
        for i, row in enumerate(rows):
            cols = row.find_all("td")
            if len(cols) < 6:
                continue

            try:
                country_span = cols[0].find("span", attrs={"data-sort-value": True})
                if not country_span:
                    continue
                country = country_span["data-sort-value"]

                population_str = cols[1].text.strip().replace(",", "").replace(" ", "")
                population = int(population_str)

                region = cols[4].text.strip()

                data.append({
                    "name": country,
                    "region": region,
                    "population": population
                })
            except Exception:
                continue

        return data
