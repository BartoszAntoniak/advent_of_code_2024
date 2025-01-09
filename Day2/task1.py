import pandas as pd

list_of_reports = pd.read_csv("data.txt", header=None, names=["Report"])
list_of_reports["Report"] = list_of_reports["Report"].apply(lambda x: list(map(int, x.split())))
reports_list = list_of_reports["Report"].tolist()

reports_counter = 0

for report in reports_list:
    report_verification_list_1 = []

    for level in range(len(report)-1):
        if report[level] > report[level+1]:
            report_verification_list_1.append("descending")
        elif report[level] < report[level+1]:
            report_verification_list_1.append("ascending")
        else:
            report_verification_list_1.append("no change")

    report_verification_list_2 = []
    for level in range(len(report)-1):
        value_change = report[level] - report[level+1]
        report_verification_list_2.append(value_change)

    print(report_verification_list_1)
    print(report_verification_list_2)

    if all(each_value == "descending" for each_value in report_verification_list_1) or all(each_value == "ascending" for each_value in report_verification_list_1):
        print("1st check passed")
        if max(report_verification_list_2)<=3 and min(report_verification_list_2)>=-3:
            reports_counter+=1
            print("2nd check passed")
    else:
        print("1st check failed")

    print(reports_counter)