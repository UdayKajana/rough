import pandas as pd
combined_df = pd.DataFrame(columns=['Employee ID', 'Name', 'Email', 'Phone Number', 'Department'])
for i in range(10):
    try:
        filename = "synthetic_employee_data{}.csv".format(i)
        df = pd.read_csv(filename)
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    except FileNotFoundError:
        print("File synthetic_employee_data{}.csv not found.".format(i))
combined_df.drop_duplicates(inplace=True)
combined_df.reset_index(drop=True, inplace=True)
combined_df.drop_duplicates(inplace=True)
combined_df.reset_index(drop=True, inplace=True)
combined_df.to_csv("final_synthetic_data_with_dedupe.csv")
print(combined_df)
