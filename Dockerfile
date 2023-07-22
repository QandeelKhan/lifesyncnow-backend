# Build stage
FROM python:3.11-alpine3.18 as builder
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-client mariadb-dev build-base python3-dev \
    cairo-dev \
    jpeg-dev \
    libffi-dev \
    pango-dev \
    musl-dev \
    bash \
    libpq-dev \
    libpq \
    redis

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install --user -r requirements.txt
COPY . /app/
COPY wait-for-it.sh /app/
COPY run-migrations.sh /app/
RUN chmod +x /app/wait-for-it.sh /app/run-migrations.sh

FROM python:3.11-alpine3.18
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-libs mariadb-connector-c bash
# RUN apk update && apk add --no-cache postgresql-libs mariadb-connector-c bash
WORKDIR /root/lifesyncnow-backend
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /root/lifesyncnow-backend
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
EXPOSE 6379
