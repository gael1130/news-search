import re
import unicodedata
# for the new code
import datetime
import requests


def create_safe_filename(search_term):
    """
    Create a safe filename from the search term by removing special characters
    and replacing spaces with underscores.
    """
    # Normalize unicode characters
    normalized = unicodedata.normalize('NFKD', search_term)
    # Remove non-ASCII characters
    ascii_text = normalized.encode('ASCII', 'ignore').decode()
    # Replace spaces with underscores and remove other special characters
    safe_filename = re.sub(r'[^\w\s-]', '', ascii_text).strip().replace(' ', '_')
    return safe_filename


def clean_source(source_href):
    """
    Clean the source by removing 'https://', 'http://', and 'www.' from the beginning
    """
    source_href = str(source_href)  # Ensure the input is a string
    
    # Remove http:// or https://
    if source_href.startswith(('http://', 'https://')):
        source_href = source_href.split('//', 1)[1]
    
    # Remove www.
    if source_href.startswith('www.'):
        source_href = source_href[4:]
    
    return source_href

# Date Utility Functions
def bisextile(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month == 2:
        return 29 if bisextile(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
    
# New code ***

def get_longest_word(text):
    """
    Get the longest word from a text.
    """
    words = re.findall(r'\w+', text)
    return max(words, key=len)


def get_real_article_link(rss_link):
    """
    Translate Google News RSS link into the real article link.
    """
    response = requests.get(rss_link)
    real_link = response.url
    return real_link


def format_date_french(date_string):
    """
    Convert a date string in the format 'YYYY-MM-DD' to French format 'D MMMM YYYY'.
    """
    months = [
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"
    ]
    date_obj = datetime.datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S GMT')
    day = date_obj.day
    month = months[date_obj.month - 1]
    year = date_obj.year
    return f"{day} {month} {year}"
# End of new code ***
    
# List Utility Functions
def remove_empty_values(row):
    """ Remove all empty strings from the row. """
    return [value for value in row if value]