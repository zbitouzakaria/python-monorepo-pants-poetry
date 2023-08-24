FROM python:3.10 as base

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry config virtualenvs.create false

FROM base as app
RUN poetry install --only app --no-directory
COPY projects/ projects/
RUN poetry install --only app
CMD ["poetry", "run", "python", "projects/app/src/org/app/main.py"]

FROM base as cli
RUN poetry install --only cli --no-directory
COPY projects/ projects/
RUN poetry install --only cli
CMD ["poetry", "run", "python", "projects/cli/src/org/cli/main.py"]
