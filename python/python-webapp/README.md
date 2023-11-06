
# Random Quote and Picture Web App

This is a simple web application built using Flask that displays a random quote along with a random picture. Users can optionally specify a ``key`` for the quote and choose whether the picture should be displayed in grayscale.

## Disclaimer

This application was developed as part of a job interview assessment. It is built using the Flask framework, which, while suitable for development and testing purposes, may not be optimized for handling high levels of concurrent requests in a production environment."

## Features

- Display a random quote and picture on a web page.
- Optional: Specify a ``key`` for the quote using the "?key=######" parameter in the URL.
- Optional: Display the picture in grayscale using the "?grayscale" parameter in the URL.

> **<u>Note</u>**: these two(2) discretionary files are not to be used, but are simplified samples of the approach I would take in deploying a real production level app to AWS ECS

- Discretionary: a github action sample ``github_action.yaml`` that could build, test and deploy this project to AWS ECS via ...
- Discretionary: ... Terraform! in the ``main.tf`` file. 

## Ignore the Prerequisites! Use Docker instead

You can build a docker image and run it locally, provided you have the docker engine installed. 

```bash
docker build -t webapp . && \
docker run --rm -p 8080:5000 webapp &

# then
curl -X GET http://127.0.0.1:8080
```

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.11
- Flask
- Requests (for making HTTP requests)

You can install everything needed using pip in a virtual env:

```
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
```
## Usage

1. Clone the repository:

```bash
git clone https://github.com/arichter-tc/senior-software-engineer-domains-application.git

cd python/python-webapp
```

2. Run the Flask application:
```
    python app.py
```

3. Open a web browser and navigate to [http://localhost:5000/](http://localhost:5000/) to view a random quote and picture.

### Optional Parameters

- To specify a category for the quote, add the "category" parameter to the URL. For example:

  [http://localhost:5000/?key=123456](http://localhost:5000/?key=123456)

- To display the picture in grayscale, add the "grayscale" parameter to the URL. For example:

  [http://localhost:5000/?grayscale](http://localhost:5000/?grayscale)

- To specify both the category and grayscale options:

  [http://localhost:5000/?key=123456&grayscale](http://localhost:5000/?key=123456&grayscale)

## Unit Tests

```bash
python -m unittest
```

## API Sources

- Quotes are fetched from the [Forismatic Quote API](http://forismatic.com/en/api/).
- Pictures are retrieved from the [Lorem Picsum](https://picsum.photos/) API.
