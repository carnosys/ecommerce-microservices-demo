FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./product_service .
EXPOSE 5003
CMD ["python", "app.py"]

