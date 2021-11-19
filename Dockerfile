# Use an official Python runtime as a parent image
FROM python:3

ENV PATH="/app/.local/bin:${PATH}"
# Makes sure the output is not buffered
ENV PYTHONUNBUFFERED 1
# Makes no PYC code generated
ENV PYTHONDONTWRITEBYTECODE 1

RUN useradd --create-home application -d /app
# Generate and enter the app directory
WORKDIR /app

USER application

# Volume for database
RUN mkdir /app/db
RUN chown -R application /app/db
VOLUME /app/db

# Point to correct settings
ENV DJANGO_SETTINGS_MODULE "afterend.docker"

# Copy the project's code
ADD . /app 

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
