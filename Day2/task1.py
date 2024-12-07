import pandas

list_of_reports = pandas.read_csv("data.txt", header=None, names=["RawData"])
df = list_of_reports["RawData"].str.split(r'\s+', expand=True)  # Use regex for splitting
list_of_reports = df.values.tolist()

list_of_reports = [[int(each_value) for each_value in row if each_value not in (None, '')] for row in list_of_reports]
safe_reports_counter = 0

for row in list_of_reports:

    verification_list = []
    ascension_counter = 0

    for each_value in range(len(row)-1):
        value_A = row[each_value]
        value_B = row[each_value +1]

        if value_A > value_B:
            ascension_counter -=1
        elif value_A < value_B:
            ascension_counter +=1
    values_quantity_ascending = len(row)-1
    values_quantity_descending = -len(row)+1

    print(row)
    print(f"Ascension Counter: {ascension_counter}, Values Quantity: {values_quantity_ascending}, {values_quantity_descending}")  # Debug counters

    if (values_quantity_descending) == ascension_counter or values_quantity_ascending== ascension_counter:
        print("1st check passed")
        for each_value in range(len(row) - 2):
            value_A = row[each_value]
            value_B = row[each_value + 1]
            value_C = row[each_value+2]

            calculated_range_left = abs(value_A - value_B)
            calculated_range_right = abs(value_B - value_C)
            verification_list.append(calculated_range_left)
            verification_list.append(calculated_range_right)

        if all(-2 <= x <= 3 for x in verification_list):
            print("2nd check passed")
            safe_reports_counter +=1

    print(safe_reports_counter)
