FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./payment_service .
EXPOSE 5005
CMD ["python", "app.py"]

