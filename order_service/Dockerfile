FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./order_service .
EXPOSE 5004
CMD ["python", "app.py"]

