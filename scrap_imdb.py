import csv 

with open('abcd.csv', 'r') as a:
    with open('a.csv','w') as w:
        writer = csv.writer(w)
        reader = csv.reader(a)
        for row in reader:
            print(row)