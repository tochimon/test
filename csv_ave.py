import numpy as np
#from scipy import integrate
#import pandas as pd
import csv

#配列宣言
csv_input = []

#csvファイルを指定
MyPath = 'naka.csv'

#csvファイルを読み込み
with open(MyPath) as f:
    reader = csv.reader(f)
    #csvファイルのデータをループ
    for row in reader:
        #B列を配列へ格納
        csv_input.append(int(row[1]))

#ave = np.mean(csv_input, axis=0)
#print(ave)