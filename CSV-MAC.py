import csv
import os
import sys

FILE = "contacts.csv"


def read_list():
    contacts = []
    with open(os.path.join(sys.path[0], FILE), newline = "") as f:
        reader = csv.reader(f)
        for row in reader:
            contacts.append(row)
        return contacts

def write_list(contacts):
    with open(os.path.join(sys.path[0], FILE), 'w', newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(contacts)