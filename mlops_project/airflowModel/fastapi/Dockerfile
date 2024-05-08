# Use Python 3.9 as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy all the files from the current directory to the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean