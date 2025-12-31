FROM python:3.11-slim

RUN useradd -m appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

USER appuser

ENV APP_PORT=8000
EXPOSE 8000

CMD ["python", "app.py"]

