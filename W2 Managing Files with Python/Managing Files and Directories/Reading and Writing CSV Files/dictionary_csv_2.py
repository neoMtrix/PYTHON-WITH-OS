# we can use DictWriter in a similar way to generate a CSV file from the contents of a list of dictionaries. This means that each element in the list will be a row in the file, and the values of each field will come out of each of the dictionaries.

import csv

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
            {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
            {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open("by_deparment.csv", "w") as by_deparment:
    writer = csv.DictWriter(by_deparment, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

# So here we have our list of dictionaries and each contain the keys, name, username and department. We now want to write this HTML file and the code will look like this. So we first define the list of keys that we want to write to the file, then we open the file for writing. Next we created the DictWriter passing the keys that we had identified before, and then we call two different methods on the writer. The right header method will create the first line of the CSV based on keys that we passed, and the right rows method will turn the list of dictionaries into lines in that file.