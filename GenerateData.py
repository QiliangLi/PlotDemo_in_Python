import random
import csv


with open("01.csv", "w", encoding="GBK", newline="") as file:
    writer=csv.writer(file)
    for i in range(100):
        row=[random.random()+1, random.random()+1, random.random()+1, random.random()+1]
        print(row)
        writer.writerow(row)