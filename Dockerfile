FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
# we user --user to make the docker file to be responsible to install this package in a home directory and not in a low level directory that might require the root priveleges.
RUN pip install --user -r requirements.txt
COPY . /code/