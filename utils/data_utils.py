import pandas as pd
import csv

def load_sources(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f)

def save_results_to_csv(results, csv_filename):
    df = pd.DataFrame(results, columns=["Titre", "Source", "Utilité", "Date (French)", "Année", "Lien"])
    df.to_csv(csv_filename, index=False, quoting=csv.QUOTE_ALL, encoding='utf-8-sig')
    print(f"Results saved to {csv_filename}")
    print(f"Total results: {len(df)}")
    print(f"Results by utility: {df['Utilité'].value_counts().to_dict()}")
    print(f"Results by year: {df['Année'].value_counts().sort_index().to_dict()}")



def save_results_to_excel(results, excel_filename):
    # Convert results to a pandas DataFrame
    df = pd.DataFrame(results, columns=["Titre", "Source", "Utilité", "Date (French)", "Année", "Lien"])

    # Save to Excel using .to_excel()
    df.to_excel(excel_filename, index=False, engine='openpyxl')

    # Print confirmation and summary
    print(f"Results saved to {excel_filename}")
    print(f"Total results: {len(df)}")
    print(f"Results by utility: {df['Utilité'].value_counts().to_dict()}")
    print(f"Results by year: {df['Année'].value_counts().sort_index().to_dict()}")
