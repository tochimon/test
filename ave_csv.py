import numpy as np
import csv

#配列に挿入
with open('./naka.csv') as f:
    reader = csv.reader(f)
    #for row in reader:
        #print(row)
    l = [row for row in reader]

print(l)

#平均値を計算
#ave = np.mean(l, axis=0)
#print(ave)
