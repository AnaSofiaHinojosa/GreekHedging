import pandas as pd

def main():
    # Load the Excel file and select the sheet
    df = pd.read_excel('Datos AAPL proyecto cuanti.xlsx', sheet_name='Hoja2')
    df_filtered = df.head(10)
    
    # Show the filtered DataFrame
    print(df_filtered)

if __name__ == "__main__":
    main()