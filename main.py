from utils.search import perform_searches_for_all_periods
from utils.data_utils import save_results_to_csv
from utils.harmonize_classify_verify import create_safe_filename
from datetime import datetime

def main():
    search_terms = ["Cérélia"]
    results = perform_searches_for_all_periods(search_terms)
    safe_name = create_safe_filename(search_terms[0])
    csv_filename = f"results/{safe_name}_{datetime.now().strftime('%Y_%m_%d_%Hh%M')}.csv"
    save_results_to_csv(results, csv_filename)

if __name__ == "__main__":
    main()
