# Webscraping
# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt

# Initiate scrape_all() to receive data
def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Possible arrangement of scraping function (easily flexible)
    news_title, news_paragraph = world_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": news_facts(),
        "last_modified": dt.datetime.now(),
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def world_news(browser):

    # Visit the mars nasa news site
    url = ''
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    html = browser.html
    news_soup = soup(html, 'html.parser')

    try:

        # Webscrape code for news titles and articles. Could be a list of both
    
    except AttributeError:
        return None, None

    return news_title, news_paragraph

# Scrape an image by clicking clicking on <button> on the website
def featured_image(browser):

    # Visit URL
    url = ''
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative image url
        # Webscrape code for images. Possibly replace button with select 
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}' #replace url here

    return img_url

# Scrape a dataframe in html format from a website
def news_facts():
    try:
        # Using Pandas Dataframe to scrape a table from a website
        # The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML. May need to click and search on webpages.
        df = pd.read_html('')[0]
    
    except BaseException:
        return None

    df.columns=['Description', 'Mars', 'Earth'] # Replace name of columns in the table
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()