import pandas as pd
import glob

def merge_excel_files(folder=".", output_file="clean_output.xlsx"):
    all_files = glob.glob(folder + "/*.xlsx")
    dfs = []

    for file in all_files:
        try:
            df = pd.read_excel(file)
            dfs.append(df)
            print(f"Loaded {file} with {len(df)} rows.")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if not dfs:
        print("No Excel files found.")
        return

    combined = pd.concat(dfs, ignore_index=True)

    # Clean data
    combined.drop_duplicates(inplace=True)
    combined.fillna("N/A", inplace=True)

    combined.to_excel(output_file, index=False)
    print(f"Saved merged file as {output_file} with {len(combined)} rows.")

if __name__ == "__main__":
    merge_excel_files()