import pandas as pd

list_of_locations = pd.read_csv("data.txt", header=None, names=["RawData"])
df = list_of_locations["RawData"].str.split(r'\s+', expand=True)  # Use regex for splitting
df.columns = ["Location1", "Location2"]
df["Location1"] = pd.to_numeric(df["Location1"])
df["Location2"] = pd.to_numeric(df["Location2"])
Location1_list = df.Location1.values.tolist()
Location2_list = df.Location2.values.tolist()
sum = 0


while Location1_list:
    min_data_Location1 = min(Location1_list)
    min_data_Location2 = min(Location2_list)
    calculation_result = abs(min_data_Location1 - min_data_Location2)
    sum += calculation_result
    Location1_list.remove(min_data_Location1)
    Location2_list.remove(min_data_Location2)

print(sum)

