#Cesar Hernandez 1835494
import csv
file_name = input()
with open(file_name, 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  pass_through = dict()
  for i in reader:
    for j in i:
      if j in pass_through:
        pass_through[j] = pass_through[j]+1
      else:
        pass_through[j]=1
for k in list(pass_through.keys()):
  print("{} {}".format(k, pass_through[k]))