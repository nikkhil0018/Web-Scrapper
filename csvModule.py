import csv

with open('mycsv.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['Col1', 'Col2', 'Col3'])
    csv_writer.writerow(['one', 'two', 'three'])
    csv_file.close()