# Visualize reports
# First, give executable permission to the Python script ticky_check.py.
chmod +x ticky_check.py

# Run the ticky_check.py by using the following command:
./ticky_check.py

# Executing ticky_check.py will generate two report file __error_message.csv __and user_statistics.csv.

# You can now visualize the __error_message.csv __and user_statistics.csv by converting them to HTML pages. To do this, pass the files one by one to the script csv_to _html.py file, like we did in the previous section.

# To convert the error_message.csv into HTML file run the following command:
./csv_to_html.py error_message.csv /var/www/html/<html-filename>.html
# Replace <html-filename> with the name of your choice.

# To convert user_statistics.csv into HTML file, run the following command:
./csv_to_html.py user_statistics.csv /var/www/html/<html-filename>.html
# Replace <html-filename> with the new name

# Now, to view these HTML pages, open any web-browser and enter the following URL in the search bar.

# [linux-instance-external-IP]/[html-filename].html

# Generate two CSV report files and visualize data on the web

