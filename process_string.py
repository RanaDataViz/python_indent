import csv
import re

with open("search_file.csv") as source, open("list.csv") as module_names, open("Final_File.csv","w",newline="") as result:
    reader=csv.reader(source)
    module=csv.reader(module_names)
    writer=csv.writer(result)
    flag=False
    for row in reader:
        i=row[1]
        for s in module_names:
            k=s[0].strip()
			l=s[1].strip()
            print(k)
			if i.find(k)!=-1 and flag==False:
                row[1]=l
                writer.writerow(row)
                flag=True
        module_names.seek(0)
        flag=False
