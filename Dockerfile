# this is a multi stage file,using a multi-stage build to separate the build environment from the runtime environment. This can help reduce the size of the final image.
# Build stage
FROM python:3.9 AS build
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client postgresql
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
# we user --user to make the docker file to be responsible to install this package in a home directory and not in a low level directory that might require the root priveleges.
# RUN pip install --user -r requirements.txt
# RUN pip3 install --user -r requirements.txt
RUN pip3 install --user --no-cache-dir -r requirements.txt
COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# ---------------------------------------------------------
# FROM python:3.9-slim-buster as builder
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# RUN apt-get update && apt-get install -y postgresql-client
# RUN mkdir /build
# WORKDIR /build
# COPY requirements.txt /build/
# RUN pip install --no-cache-dir -r requirements.txt
# # Install psycopg2
# RUN pip3 install psycopg2-binary
# COPY . /build/

# # Runtime stage
# # Stage 2: Production environment
# FROM python:3.9-slim-buster
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# RUN apt-get update && apt-get install -y postgresql-client postgresql
# RUN mkdir /code
# COPY --from=builder /build /code
# WORKDIR /code
# VOLUME /var/lib/postgresql/data
# COPY ./entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
