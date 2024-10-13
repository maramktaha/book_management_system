# Use official Python image as the base
FROM python:3.10-slim


# Set working directory
WORKDIR /app

# Update and install system dependencies
RUN apt-get update  && apt-get install -y python3-pip && apt-get install -y cron

# Install GDAL Python bindings
RUN apt-get install -y gdal-bin \
    libgdal-dev \
    gettext 


RUN pip3 install GDAL==3.6.2
RUN apt-get update && apt-get install -y postgresql-client

COPY requirements.txt /app/
# Install Python dependencies
RUN pip install -r requirements.txt

RUN echo "0 0 * * * /usr/local/bin/python /app/manage.py runcrons >> /var/log/cron.log 2>&1"
# Copy the Django application code
COPY . /app/

# Command to run your application
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "book_management_system.asgi:application"]
