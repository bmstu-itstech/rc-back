FROM python:3.12-alpine AS poetry

RUN pip install poetry

WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry export -f requirements.txt --output requirements.txt


FROM python:3.12-alpine
EXPOSE 8000

WORKDIR /app
COPY --from=poetry /app/requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN python manage.py collectstatic
RUN python manage.py migrate

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]