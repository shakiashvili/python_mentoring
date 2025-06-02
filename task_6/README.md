First we need to create virtual environment:
`python -m venv env`
Then to activate it

`source env/bin/activate`

Then, We need to install the required packages

`pip install requests`
`pip install beautifulsoup4`
`pip install pytest`

I have chosen 'html.parser' for parsing purposes but you could use lxml or html5lib

To test the application

`pytest`