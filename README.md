# sparrow
A lightweight shell for Twitter botmaking

_This is for Python version 3_

Remember:
1. Generally do NOT put your API credentials in your source code
2. API creds are sensitive information that can control access to accounts
3. I'm only doing this so you can have an easy demo

## Setup Steps
Here are some things you should make sure are
done before working with this repository.

1. Install Python3
    You can get this for free on the Python website - https://www.python.org/downloads/

2. Create a Python virtual environment
    `python -m venv my_venv`

3. Turn on the virtual environment
    On Mac or Linux `source my_venv/bin/activate`
    On Windows `my_venv\Scripts\activate`
    After this your terminal/command prompt should look something like this `(my_venv) $` or this `(my_venv) C:\Users\yourusername>`.

4. Install Twython
    Now that your Python virtual environment is turned on you should be able to install Twython with:

    `pip install twython`

    But if you have any issues you can check the 
    documentation here: 
    https://twython.readthedocs.io/en/latest/usage/install.html

5. Then you can start working in the sparrow.py file to get your bot up and running.

6. When you're done, run the program in your terminal or command prompt:
    `python sparrow.py`
