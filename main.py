import csv
from datetime import datetime
from utils.google_sheets import setup_google_sheets_api, write_to_google_sheet
from utils.search import perform_search

def save_results_to_csv(results, csv_filename):
    """ Save the results of the news searches to a local CSV file. """
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Search Term", "Article Title", "Link"])  # Header row
        writer.writerows(results)

def main():
    credentials = {"type": "..."}  # Your Google credentials as a dictionary

    # Set your search terms manually here
    search_term = "Pierre Hermé"

    # results = perform_news_search(search_terms)
    results = perform_search(search_term, '2010-01-01', '2010-12-31', worksheet, useful_sources, useless_sources)

    # Save the results to a local CSV file
    csv_filename = f"news_search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    save_results_to_csv(results, csv_filename)

    # After the search is completed, write the results back to the Google Sheet

    # sheet_name = "news-searches"
    # data_to_write = [["Search Term", "Article Title", "Link"]] + results  # Include header
    # write_to_google_sheet(credentials, sheet_name, data_to_write)

if __name__ == "__main__":
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()
    main()
