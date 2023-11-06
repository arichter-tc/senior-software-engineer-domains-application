
# Random Quote and Picture CLI



## Disclaimer

Please note that the ANSI art representation of the randomly retrieved image may not always provide the best visual quality. ANSI art is a text-based representation and may not capture all the details or colors present in the original image. While it adds a unique and creative touch to the tool's output, the fidelity of the image may vary.

If you require high-quality images, it is recommended to use a different tool or method to retrieve and display images. This tool primarily focuses on providing random content in a fun and text-based format, with an emphasis on simplicity and speed.

I appreciate your understanding.


## Features

- Display a random quote and picture on a web page.
- Optional: Specify a ``key`` for the quote using the "?key=######" parameter in the URL.
- Optional: Display the picture in grayscale using the "?grayscale" parameter in the URL.



## Ignore the Prerequisites! Use Docker instead

You can build a docker image and run it locally, provided you have the docker engine installed. 

```bash
docker build -t webapp . && \
docker run --rm -p 80:5000 webapp &

# then
curl http://127.0.0.1:80
```

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.11

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

cd python/python-cli
```

2. Usage

To use the Random Quote and Picture Generator, follow the usage examples below:


```bash
# to print a picture to the terminal
python cli.py --getpicture 

# Display a Picture in Grayscale
python cli.py --getpicture --grayscale

# to get a quote
python cli.py --getquote

# Specify a Key for the Quote
python cli.py --getquote --key 123456
```

You can combine options to fetch both a random quote and a random picture. For example:

```bash
# Fetch Both a Quote and a Picture
python cli.py --getquote --getpicture
```

## Unit Tests

```bash
python -m unittest
```

## API Sources

- Quotes are fetched from the [Forismatic Quote API](http://forismatic.com/en/api/).
- Pictures are retrieved from the [Lorem Picsum](https://picsum.photos/) API.
