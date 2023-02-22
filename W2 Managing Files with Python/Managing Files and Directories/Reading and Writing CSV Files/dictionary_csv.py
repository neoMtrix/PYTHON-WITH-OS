import csv

with open("hosts.csv", "w") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} user").format(row["name"], row["users"]))
