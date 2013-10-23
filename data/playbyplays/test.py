import csv

inline = '{}_nfl_pbp_data.csv'
file1 = open(inline.format('2002'),'r')
file2 = open(inline.format('2003'),'r')
reader1 = list(csv.DictReader(file1))
reader2 = list(csv.DictReader(file2))
items = ["game1 seconds = {}, game2 seconds = {}".format(x['sec'],y['sec']) for y in reader2 for x in reader1]
print items
