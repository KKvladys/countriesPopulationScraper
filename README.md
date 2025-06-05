# Population Scraper

This project is a application that parses country population data from different sources and stores it in a PostgreSQL
database. It includes functionality to aggregate and display regional statistics.

## 🛠️ Technologies Used

- **Python 3.12**
- **PostgreSQL**
- **SQLAlchemy (async)**
- **Alembic**
- **Poetry**
- **Docker + Docker Compose**
- **BeautifulSoup**
- **Ruff**

## 📦 Services

The app contains the following services:

- **db** – PostgreSQL database
- **get_data** – Parses population data and saves it to the database
- **print_data** – Outputs aggregated statistics from the database

## 🌐 Supported Data Sources

The data source is selected via the `DATA_SOURCE` environment variable.

- `wikipedia` – Parses data
  from [Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations))
- `statistics_times` – Parses data
  from [Statistics Times](https://statisticstimes.com/demographics/countries-by-population.php)


1. **Clone the repository**:

   ```bash
   git clone https://github.com/KKvladys/countriesPopulationScraper.git
   ```
   ```bash
   cd countriesPopulationScraper
    ```

## 🔧 Environment Variables

Define them in a `.env` file in the root directory:

```env
POSTGRES_USER=user
POSTGRES_PASSWORD=pass
POSTGRES_DB=population_db
POSTGRES_HOST=db
POSTGRES_DB_PORT=5432
DATA_SOURCE=wikipedia
```

**Build and run the services**

```bash
  docker-compose up --build
```

```bash
  docker-compose up get_data
```
Wait for the get_data container to finish parsing and loading data into the database.
```bash
  docker-compose up print_data
```
You should see output with aggregated population data by region.

## Output Example
```angular2html
Регіон: Oceania                                                                                                                                 
Загальне населення: 45562783                                                                                                                  
Найбільша країна: Australia
Населення найбільшої країни в регіоні: 26451124                                                                                               
Найменша країна: Niue                                                                                                                         
Населення найменшої  країни в регіоні: 1817  
```
