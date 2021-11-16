# Use an official Python runtime as a parent image
FROM python:3

# Makes sure the output is not buffered
ENV PYTHONUNBUFFERED 1

# Generate and enter the app directory
WORKDIR /app

# Copy the project's code
ADD ./app

# Volume for database
VOLUME /var/run/django

# Install dependencies
RUN pip install -r requirements.txt
