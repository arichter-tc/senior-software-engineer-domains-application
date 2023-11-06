import argparse
import requests


def get_quote(key=""):
    """
    Fetches a random quote using an optional key.

    Parameters:
        key (str, optional): A key that can be used to fetch a quote. It should be a string
            representing a six-digit integer. Defaults to an empty string.

    Returns:
        str: A random quote if the key is valid, or an error message if the key is invalid.

    Example:
        To fetch a quote with a specific key:
        >>> get_quote("123456")

        To fetch a random quote:
        >>> get_quote()
    """

    def is_valid_six_digit_int(string_value):
        if isinstance(string_value, str) and string_value.isdigit() and len(string_value) == 6:
            return True
        else:
            return False

    def try_quote_request(quote_url, keyquery=""):
        try:
            quote_response = requests.get(
                f"{quote_url}?method=getQuote&lang=en&format=json{keyquery}", timeout=5
            )  # quote API is slow I find, allow 5 seconds to return
            quote_response.raise_for_status()
        except Exception as e:
            quote = "Error: API not responsive. Failed to fetch a quote."
        else:
            try:
                quote = quote_response.json().get("quoteText")
            except requests.exceptions.JSONDecodeError as e:
                quote = f"Error: {e}: \nBad JSON from API"
        return quote

    # this means key would not be valid for use
    if key != "" and not is_valid_six_digit_int(key):
        raise ValueError(f"invalid <key> : {key}. Key must be in format ######")

    # this means user did supply input
    if key != "":
        keyquery = f"&key={key}"

    # this means user has supplied no input
    if key == "":
        keyquery = ""

    # API endpoint for quote
    quote_url = "http://api.forismatic.com/api/1.0/"

    # try to get quote, returns if successful
    quote = try_quote_request(quote_url, keyquery)
    return quote


def get_picture(grayscale=False):
    """
    Fetches a random picture and displays it in ANSI colors for the terminal.

    Parameters:
        grayscale (bool, optional): Whether to fetch and display the picture in grayscale.
            If True, the picture will be displayed in grayscale; if False (default), it will
            be displayed in color.

    Returns:
        None: This function does not return a value but displays the fetched picture in the terminal.

    Example:
        To fetch and display a random picture in color:
        >>> get_picture()

        To fetch and display a random picture in grayscale:
        >>> get_picture(grayscale=True)
    """
    from PIL import Image
    from io import BytesIO
    import climage

    # image url, set to 80 pixels for "most" terminals
    image_url = "https://picsum.photos/80"

    if grayscale:
        image_url = "https://picsum.photos/80?grayscale"

    # get image, open image as raw Bytes, convert to ANSI colors
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check for any HTTP errors

        img = Image.open(BytesIO(response.content)).convert("RGB")
        converted = climage.convert_pil(img, is_unicode=True)

    except requests.exceptions.RequestException as e:
        pass
        # print(f"An error occurred while fetching the image: {e}")
    except Exception as e:
        pass
        # print(f"An error occurred: {e}")
    return converted


def main():
    """
    Command-line interface (CLI) tool to fetch random quotes and/or pictures.

    Usage:
        - Use '--getquote' to fetch a random quote.
        - Use '--getpicture' to fetch a random picture.
        - Use '--key' to specify a key for the quote (optional).
        - Use '--grayscale' to fetch a picture in grayscale (optional).

    Args:
        None

    Returns:
        None: This function doesn't return a value but processes the command-line arguments
        and performs the corresponding action.

    Example:
        To fetch a random quote:
        >>> python main.py --getquote

        To fetch a random picture:
        >>> python main.py --getpicture

        To fetch a random picture and a random quote:
        >>> python main.py --getpicture --getquote

        To fetch a random picture in grayscale:
        >>> python main.py --getpicture [--grayscale]

        To fetch a quote with a specific key:
        >>> python main.py --getquote [--key 123456]

        To fetch a random picture in grayscale and a random quote with a specific key:
        >>> python main.py --getpicture [--grayscale] --getquote [--key 123456]
    """
    parser = argparse.ArgumentParser(description="CLI tool to get a quote or picture")
    parser.add_argument("--getquote", action="store_true", help="Get a random quote")
    parser.add_argument("--getpicture", action="store_true", help="Get a random picture")
    parser.add_argument("--key", help="Specify a key for the quote (optional)", required=False)
    parser.add_argument("--grayscale", action="store_true", help="Get a grayscale picture (optional)", required=False)
    args = parser.parse_args()

    if args.getquote:
        if args.key:
            print(get_quote(args.key))
        else:
            print(get_quote())

    if args.getpicture:
        if args.grayscale:
            print(get_picture(grayscale=True))
        else:
            print(get_picture())


if __name__ == "__main__":
    main()
