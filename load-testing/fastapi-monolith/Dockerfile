# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages 
RUN pip install fastapi
RUN pip install uvicorn

# Define the command to run the app using uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "3002"]
