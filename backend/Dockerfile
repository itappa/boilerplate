FROM python:3 AS base
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg nodejs npm

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install uv
RUN uv pip install --system -r requirements.txt
COPY . .


FROM base AS web
RUN npm install



FROM base AS celery


FROM base AS flower