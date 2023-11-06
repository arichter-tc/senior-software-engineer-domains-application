# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /cli
WORKDIR /cli

# Copy the current directory contents into the container at /cli
COPY . /cli

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run cli.py when the container launches
ENTRYPOINT [ "python", "cli.py" ]