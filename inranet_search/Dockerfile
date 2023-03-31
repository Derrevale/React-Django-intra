FROM python:3.10

# Expose a default port
EXPOSE 8001

# Update system and install tesseract
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-fra \
    libtika-java \
 && rm -rf /var/lib/apt/lists/*

# Define the working directory
WORKDIR /code

# Copy the requirements.txt file
COPY ./requirements.txt /code/requirements.txt

# Install the python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the sources
COPY ./app /code/app

# Export the right profile
ENV profile=docker

# Start the application within uvicorn
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8001"]
