FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./auth_service .
EXPOSE 5001
CMD ["python", "app.py"]

