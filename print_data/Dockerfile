FROM python:3.12-slim

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock ./
RUN pip install --no-cache-dir poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY ./src ./src
COPY .env .env

ENV PYTHONPATH="${PYTHONPATH}:/app/src"

CMD ["python", "src/services/print_data.py"]
