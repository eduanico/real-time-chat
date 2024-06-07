# Dockerfile

FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=chat_project.settings

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "--workers=3", "chat_project.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]
