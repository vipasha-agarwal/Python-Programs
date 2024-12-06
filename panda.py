import pandas as pd

try:
    df = pd.read_excel("Book1.xlsx")
    print(df)
except Exception as e:
    print(f"Error: {e}")
