FROM python:3.12-slim

WORKDIR /app

# Установите ВСЕ зависимости в одном RUN
RUN pip install --no-cache-dir \
    flask \
    gunicorn \
    flask-caching \
    python-dotenv \
    gigachat \
    requests

COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]

