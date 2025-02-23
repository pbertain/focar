import requests
from yattag import Doc, indent
from datetime import datetime, timedelta
import os

# local modules
import get_date

def get_news():
    url = 'https://newsapi.org/v2/everything'

    # Calculate date 30 days ago from today
    thirty_days_ago = datetime.now() - timedelta(days=25)
    thirty_days_ago_str = thirty_days_ago.strftime('%Y-%m-%d')  # Format the date as required by the API

    parameters = {
        'q': 'Central African Republic',  # query phrase
        'from': thirty_days_ago_str, # Will change to a dynamic date calculator
        'pageSize': 20,  # maximum is 100
        'apiKey': '1d1e5b9a946f4483bade19d3ff1df788',  # your own API key
    }

    response = requests.get(url, params=parameters)

    # Convert the response to JSON format
    response_json = response.json()
    #if response['totalResults'] < 1:
        #print("sad face - no articles returned")

    # Check if the response contains 'articles'
    if 'articles' not in response_json:
        print("No articles in the response")
        print(response_json)
        return

    news_items = [(article['title'], article['url']) for article in response_json['articles']]

    # Generate HTML
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            with tag('title'):
                text('Friends of C.A.R. - FOCAR')
            with tag('style'):
                text('body { background-color: darkblue; color: white; } h1 { color: yellow; }')
        with tag('body'):
            with tag('div', style='display: flex; align-items: center; gap: 10px;'):
                with tag('img', src='images/car-flags-round-2.gif', alt='Flag of CAR', width='125', height='125'):
                    pass
                with tag('span', style='font-size: 24px; font-weight: bold; color: white;'):
                    text('Friends of C.A.R.')

            with tag('h1'):
                text('Top 20 News Articles on Central African Republic')
            with tag('ol'):
                for news_title, news_url in news_items:
                    with tag('li'):
                        with tag('a', href=news_url, style='color: white;'):
                            text(news_title)
            with tag('p'):
                text('This page was generated on: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Define the output directory and file
    output_directory = '/var/www/vhosts/focar/html/includes/'
    output_file = 'news.html'
    output_path = os.path.join(output_directory, output_file)

    # Write the HTML to a file
    with open(output_path, 'w') as f:
        indented_html = indent(
            doc.getvalue(),
            indentation = ' ' * 4,
            newline = '\n'
        )
        f.write(indented_html)

# local modules
import get_date

current_date = get_date.generate_date()
get_news()

