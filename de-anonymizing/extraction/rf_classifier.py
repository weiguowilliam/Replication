import pandas as pd


"""
based on weka information gain criteria, positive feature column number in (..forweka.csv) are:
14,461,368,654,449,661,54,31,360,45,149,142,4,181,305,372,674,99,396,697,297,556,208,55,416,96,11,628,425,644,667,233,389,138
"""

#just use the hand-crafted "forweka.csv" for classification

bdf = pd.read_csv("/Users/weiguo/Desktop/Replication/de-anonymizing/data/bigram0814_forweka.csv") 
print bdf.iloc[:3]

bdf_head = list(bdf.columns) 
# print bdf_head

use_column_incsv = [14,461,368,654,449,661,54,31,360,45,149,142,4,181,305,372,674,99,396,697,297,556,208,55,416,96,11,628,425,644,667,233,389,138]
# use_column_incsv = [590,669,1544,108,554,76,26,547,693,1395,1558,305,1564,287,427,168,556,1340,1336,1449,226,543,24,36,1335,181,953,1403,553,1500,279,428,1490,306,853,652,423,1445,1550,1070,732,1002,465,1127,906,1450,1045,555,332,197,189,1339,1498,558,668,686,1183,294,1189,772,857,769,961,1039,539,946,1425,993,642,213,1243,1448,1052,1233,758,807,173,39,954,982,775,20,1166,1145,1023,270,1161,309,1364,871,1071,1447,114,1359,440,429,1412,485,183,685,909,247,1310,712,1436,945,738,1043,54,430,1493,2,1216,928,148,604,182,1338,830,431,1471,74,53,175,177,1041,188,1459,1442,1578,1222,126,1237,733,451,1283,1334,1331,421,536,727,386,980,445]
use_column = [i-1 for i in use_column_incsv]
user_head = []
for i in use_column:
    user_head.append(bdf_head[i])

# print user_head[0:3]
# print len(user_head)#checked.right.
# print len(use_column_incsv)

user_head.append(bdf_head[-1])
df = bdf[user_head]


"""
each row should be for a file instead of a programmer. So for n programmer, there should be 9n rows.
"""