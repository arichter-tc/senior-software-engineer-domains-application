# Sr. Software Engineer Application - Domains 

## Greetings 

In this directory you'll find the solution(s) to the application assignment in the ``python/`` directory. There are two, one for the webapp and one for the cli. 
I have provided ``Dockerfile``(s) for both solutions. If you have the docker engine installed you *should* be able to just run ``docker build -t <webapp | cli> .`` while in the appropriate directory. 
Then calling ``docker run --rm -p 80:5000 webapp`` or ``docker run --rm cli -h`` 

If you do not have docker engine installed, never fear, you can simply set up a python virtual environment and execute both programs locally. 

```bash
# change directory into appropriate folder 
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 ./<name of program>.py
```

I look forward to speaking with you all further. Thank you for your consideration

> <u>**Note**</u>: You may occassionally hit the handler for 'Bad JSON from API'. Some of the JSON for the quotations are not escaped properly and get mangled on decode. Just try again and you'll get a quote

## Directory Contents

```
./
├── error.png
├── golang/
│   └── Explanation.md
├── python/
│   ├── python-cli/
│   │   ├── cli.py
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── test_cli.py
│   └── python-webapp/
│       ├── app.py
│       ├── Dockerfile
│       ├── github_action_deploy.yaml
│       ├── main.tf
│       ├── README.md
│       ├── requests
│       ├── requirements.txt
│       ├── templates
│       │   └── index.html
│       └── test_app.py
└── README.md

5 directories, 17 files
```


## Breakdown of approach

```
DONE  Create a small web app that displays an HTML page containing a random quote, and random picture from the two APIs below.
DONE  Make it resilient to one or both providers being unavailable
DONE  Add an option to web app so a category (“key” in the API) can optionally be specified for the quote. (sane/working default if not specified)
DONE  Add an option to web app to allow specifying a grayscale image
DONE  Create a back-end CLI tool to do the same
DONE  How can you return an image on cli?
DONE  Add an option to the CLI so a category (“key” in the API) can optionally be specified for the quote. (sane/working default if not specified)
DONE  Add an option to the CLI to allow specifying a grayscale image
DONE  finish all 'decorators' / clean all functions
DONE  Provide unit tests
DONE  Provide any documentation you think might be helpful
DONE  Feel free to add anythng that you think might be useful
DONE  troubleshoot the Docker container
```
