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

WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install --user -r requirements.txt
COPY . /app/
# RUN find /app -type d -name "migrations" -exec rm -r {} +
RUN chmod +x -R /app/scripts

# Build stage
FROM python:3.11-alpine3.18 as production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-libs mariadb-connector-c bash
# RUN apk update && apk add --no-cache postgresql-libs mariadb-connector-c bash
WORKDIR /root/lifesyncnow-backend
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /root/lifesyncnow-backend
# COPY --from=builder /app /root/lifesyncnow-backend --exclude=/app/*/migrations/
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
EXPOSE 6379
