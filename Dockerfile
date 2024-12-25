FROM python:3.11-slim

WORKDIR /app

COPY ./type_annotations .
COPY ./pyproject.toml .

RUN pip install poetry && poetry install --with dev

ENTRYPOINT ["poetry", "run"]
