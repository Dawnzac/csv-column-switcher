import os
import csv

def switch_columns():
    folder_path = os.getcwd()
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                header = next(csvreader)
                new_header = header[10], header[0], header[7], header[4], header[2],header[9], header[1]
                with open('new_' + filename, 'w', newline='') as new_csvfile:
                    csvwriter = csv.writer(new_csvfile)
                    csvwriter.writerow(new_header)
                    for row in csvreader:
                        csvwriter.writerow([row[10], row[0], row[7], row[4], row[2], row[9], row[1]])

if __name__ == '__main__':
    folder_path = os.getcwd()
    
    print("Confirm the folder ! > ", folder_path ," (y/n) : ")
    if input() == 'y' :
        switch_columns()
    else:
        exit()