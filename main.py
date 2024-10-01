from utils.search import perform_searches_for_all_periods
from utils.data_utils import save_results_to_csv, save_results_to_excel
from utils.harmonize_classify_verify import create_safe_filename
from datetime import datetime

def main():
    # search_terms = ["Cérélia"]
    # Prompt the user to enter a search term
    search_term = input("Enter the search term: ")
    search_terms = [search_term]

    results = perform_searches_for_all_periods(search_terms)
    safe_name = create_safe_filename(search_terms[0])
    csv_filename = f"results/{safe_name}_{datetime.now().strftime('%Y_%m_%d_%Hh%M')}.csv"
    excel_filename = csv_filename.replace(".csv", ".xlsx")
    # save_results_to_csv(results, csv_filename)
    save_results_to_excel(results, excel_filename)
    print(f"*** Results saved to {excel_filename} ***")

if __name__ == "__main__":
    main()
