import time
from datetime import datetime, timedelta
from .harmonize_classify_verify import (
    clean_source, format_date_french
)
from .data_utils import load_sources
from .pygooglenews import GoogleNews


def classify_article(source, useful_sources, useless_sources):
    if source in useful_sources:
        return "Utile"
    elif source in useless_sources:
        return "Inutile"
    else:
        return "Autre"


def extract_article_data(article, useful_sources, useless_sources):
    title = article['title'].split(" - ")[0]  # Extract the title before " - "
    link = article['link']
    published_date = article['published']
    published_datetime = datetime.strptime(published_date, '%a, %d %b %Y %H:%M:%S %Z')
    year = published_datetime.year
    source_href = article['source']['href']
    source_cleaned = clean_source(source_href)
    category = classify_article(source_cleaned, useful_sources, useless_sources)
    
    # name = get_longest_word(title)
    # periodique = article['source']['title']
    french_date = format_date_french(published_date)

    return [title, source_cleaned, category, french_date, year, link]


def perform_news_search(search_terms, from_date, to_date, useful_sources, useless_sources):
    gn = GoogleNews(lang='fr')
    results = []
    # Convert datetime to string format (YYYY-MM-DD)
    from_date_str = from_date.strftime('%Y-%m-%d')
    to_date_str = to_date.strftime('%Y-%m-%d')

    for term in search_terms:
        try:
            search_result = gn.search(term, from_=from_date_str, to_=to_date_str)
            entries = search_result.get('entries', [])
            for entry in entries:
                article_data = extract_article_data(entry, useful_sources, useless_sources)
                results.append(article_data)
        except Exception as e:
            print(f"Error during search for term {term} between {from_date_str} and {to_date_str}: {e}")
            continue

    return results

def split_and_search(search_terms, from_date, to_date, useful_sources, useless_sources, max_results=98, depth=0):
    results = perform_news_search(search_terms, from_date, to_date, useful_sources, useless_sources)
    if len(results) >= max_results:
        print(f"  {'  ' * depth}Found {len(results)} results (max: {max_results}). Splitting period and searching again.")
        # Split the period in two and search again for each half
        mid_date = from_date + (to_date - from_date) / 2
        # results = split_and_search(search_terms, from_date, mid_date, useful_sources, useless_sources, max_results, depth+1) + \
                #   split_and_search(search_terms, mid_date + timedelta(days=1), to_date, useful_sources, useless_sources, max_results, depth+1)
        
        # updated version to Accumulate results from recursive calls
        left_results = split_and_search(search_terms, from_date, mid_date, useful_sources, useless_sources, max_results, depth + 1)
        right_results = split_and_search(search_terms, mid_date + timedelta(days=1), to_date, useful_sources, useless_sources, max_results, depth + 1)
        
        results.extend(left_results)
        results.extend(right_results) 
    
    return results


def perform_searches_for_all_periods(search_terms):
    results = []
    current_date = datetime.now()
    total_searches = 1 + 10 + ((current_date.year - 2020) * 12 + current_date.month)
    completed_searches = 0

        # Load useful and useless sources
    useful_sources = load_sources('data/sources_utiles.csv')
    useless_sources = load_sources('data/sources_inutiles.csv')

    def update_progress():
        nonlocal completed_searches
        completed_searches += 1
        progress = (completed_searches / total_searches) * 100
        print(f"Progress: {progress:.2f}% ({completed_searches}/{total_searches} searches completed)")

    print("*** Starting search process... ***")

    # 1. Global search before 2010
    print("Performing global search before 2010...")
    period_results = split_and_search(search_terms, datetime(1900, 1, 1), datetime(2009, 12, 31), useful_sources, useless_sources)
    results += period_results
    print(f"Total results for period before 2010: {len(period_results)}")
    update_progress()

    # 2. Yearly searches from 2010 to 2019
    print("Performing yearly searches from 2010 to 2019...")
    for year in range(2010, 2020):
        print(f"Searching year {year}...")
        period_results = split_and_search(search_terms, datetime(year, 1, 1), datetime(year, 12, 31), useful_sources, useless_sources)
        results += period_results
        print(f"Total results for year {year}: {len(period_results)}")
        update_progress()

    # 3. Monthly searches after 2019 until the current date
    print("Performing monthly searches from 2020 to present...")
    start_year, start_month = 2020, 1
    end_year, end_month = current_date.year, current_date.month

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if year == end_year and month > end_month:
                break
            print(f"Searching {year}-{month:02d}...")
            from_date = datetime(year, month, 1)
            to_date = (from_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            period_results = split_and_search(search_terms, from_date, to_date, useful_sources, useless_sources)
            results += period_results
            print(f"Total results for {year}-{month:02d}: {len(period_results)}")
            update_progress()

            # Wait between each search to avoid being blocked
            time.sleep(2)

    print("Search process completed.")
    print(f"Total results across all periods: {len(results)}")
    return results



def perform_test_search(search_terms):
    results = []
    current_date = datetime.now()

            # Load useful and useless sources
    useful_sources = load_sources('data/sources_utiles.csv')
    useless_sources = load_sources('data/sources_inutiles.csv')

    print("*** Starting test search process... ***")

    # 1. Global search before 2010 (or any time period you'd like to test)
    print("Performing a global search for testing...")
    period_results = split_and_search(search_terms, datetime(1900, 1, 1), current_date, useful_sources, useless_sources)  # Adjust the date range if needed
    results += period_results
    print(f"Total results for the test search: {len(period_results)}")

    print("Test search process completed.")
    print(f"Total results: {len(results)}")
    return results
