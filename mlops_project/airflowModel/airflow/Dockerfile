# Use Python 3.11 as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     libpq-dev \
#     python-dev \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Apache Airflow
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt apache-airflow

# Copy the DAG file into the dags folder
COPY dags/my_dag.py dags/my_dag.py

# Initialize Airflow database
RUN airflow db init

# Expose the port used by Apache Airflow (8080 by default)
EXPOSE 8080

# Command to run Apache Airflow webserver
CMD ["airflow", "webserver", "--port", "8080"]

FROM apache/airflow:latest

USER root
RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean

USER airflow