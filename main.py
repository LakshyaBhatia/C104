'''import csv 
with open ('height-weight.csv',newline = '') as f:
   reader = csv.reader(f)
   #list function is use to convert into list/array
   file_data = list(reader)
   print(file_data)
'''
from collections import Counter
n = "whitehat jr"
data  = Counter(n)
print(data)

k = data.values()
print(k)
