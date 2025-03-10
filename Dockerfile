FROM python:3.11-slim

WORKDIR /app

COPY src/ .
CMD ["python", "test_code.py"]

