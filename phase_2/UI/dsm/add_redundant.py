import csv
f1 = open('train_snli.txt','r')
f2 = open('trani_snli2.txt','w')

while(1):
    line = f1.readline()
    if not line:
        break
    f2.write(line)
f1.close()
with open('dataset3.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            row = str(row)
            row = row[2:-5]
            row = row + '\t' + row + '\t' + '1' + '\n'
            print(row)
            f2.write(row)
            line_count += 1
    print(f'Processed {line_count} lines.')
f2.close()