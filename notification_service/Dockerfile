FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
COPY ./notification_service/notification_service_requirements.txt .
RUN pip install -r requirements.txt && pip install -r notification_service_requirements.txt
COPY ./notification_service .
EXPOSE 5006
CMD ["python", "app.py"]

