FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./user_service .
EXPOSE 5002
CMD ["python", "app.py"]

