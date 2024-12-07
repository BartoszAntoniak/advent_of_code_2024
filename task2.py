import pandas as pd

list_of_locations = pd.read_csv("data.txt", header=None, names=["RawData"])
df = list_of_locations["RawData"].str.split(r'\s+', expand=True)  # Use regex for splitting
df.columns = ["Location1", "Location2"]
df["Location1"] = pd.to_numeric(df["Location1"])
df["Location2"] = pd.to_numeric(df["Location2"])
Location1_list = df.Location1.values.tolist()
Location2_list = df.Location2.values.tolist()
sum = 0

for each_row in Location1_list:
    counter = Location2_list.count(each_row)
    row_result = each_row * counter
    sum += row_result

print(sum)

