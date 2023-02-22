import csv

hosts = [["workstation.local", "192.168.2.1"], ["webserver.cloud", "10.2.6.3"]]
with open("hosts.csv", "w") as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts)