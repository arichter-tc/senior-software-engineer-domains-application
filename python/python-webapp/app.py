from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder="templates/")


@app.route("/")
def display_random_quote_and_picture():
    """
    Displays a random quote and picture on an HTML page using Flask.

    This function fetches a random quote and a random picture, and then renders an HTML page
    containing both the quote and the picture. Users can optionally specify a category for
    the quote, and whether the picture should be displayed in grayscale.

    Args:
        None

    Returns:
        str: An HTML page containing a random quote and picture.

    Example:
        Visit the web page at http://localhost.com:5000/ to view a random quote and picture.
    """

    def is_valid_six_digit_int(string_value):
        if isinstance(string_value, str) and string_value.isdigit() and len(string_value) == 6:
            return True
        else:
            return False

    # quote request params

    # API endpoints for quote and picture
    quote_api = "http://api.forismatic.com/api/1.0/"
    key = request.args.get("key", "")

    # this means key would not be valid for use
    if key != "" and not is_valid_six_digit_int(key):
        # Return a 400 Bad Request response
        return jsonify(error="Invalid value for Key"), 400

    # this means user did supply input
    if key != "":
        keyquery = f"&{request.args.get('key' , '')}"

    # this means user has supplied no input
    if key == "":
        keyquery = ""

    # pic request params
    if request.args.get("grayscale") == "":
        is_grayscale = "?grayscale"
    else:
        is_grayscale = ""

    # Fetch a random quote
    try:
        quote_response = requests.get(f"{quote_api}?method=getQuote&lang=en&format=json{keyquery}")
        quote_response.raise_for_status()
        quote = quote_response.json()["quoteText"]

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the quote: {e}")
    except Exception as e:
        quote = "Failed to fetch a quote."

    # Fetch a random picture
    try:
        # the html rendering handles the picture via <img src=> tag.
        picture_url = f"https://picsum.photos/200{is_grayscale}"

    # if, at render time, it cannot load the image Flask catches the exception and displays the fallback image
    except Exception as e:
        picture_url = "https://static.thenounproject.com/png/2347713-200.png"

    return render_template("index.html", quote=quote, picture_url=picture_url)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
