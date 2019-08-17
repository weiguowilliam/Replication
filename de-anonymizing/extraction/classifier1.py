import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import random
import math

bdf = pd.read_csv("/Users/weiguo/Desktop/Replication/de-anonymizing/data/bigram0817_forweka.csv") 
bdf_head = list(bdf.columns) 
use_column_incsv = [2535,7368,2831,1441,1310,4603,2454,5585,2263,1589,6521,717,6404,4732,6100,3036,3298,7125,1850,5291,4675,1592,2920,1863,4336,2617,3005,3194,5678,2235,2707,6530,6150,5512,671,3485,4678,4962,1752,72,555,2147,4358,1,5510,5043,3800,2433,5246,1230,5518,5734,4505,4598,806,4026,7434,3534,2695,6563,6164,2472,5182,4995,2160,4174,6895,711,6439,151,2092,4162,380,6467,1040,4665,2643,6174,3168,2113,6264,2061,7309,3458,7248,2963,4106,5563,7148,1821,3921,5297,6640,1926,4098,5676,3292,6378,7226,6542,5368,939,5138,2677,572,3348,625,5509,5846,6824,3963,3795,3120,1825,5269,4955,1448,6267,1391,632,5963,7043,724,7174,93,3068,5554,2443,4230,6185,4198,3501,6376,6146,5778,3467,6683,7091,2636,4243,1675,1438,3203,5070,6806,3090,1973,2027,900,7180,3808,2901,6505,3770,5507,718,1888,514,5357,3433,1335,3952,3768,832,5117,4588,5022,2915,6975,2994,6351,2242,5589,85,5728,5578,1145,6301,6684,4646,4164,5019,5522,2938,3908,4534,7192,2723,2834,1823,2939,3054,7433,1758,4818,342,479,1008,5754,4051,758,7249,6550,6201,3586,4114,1345,3103,1417,2110,523,2419,2183,4981,1403,3756,231,1630,3727,5356,4278]
use_column_incsv = [2535,7368,2831,1441,1310,4603,2454,5585,2263,1589,6521,717,6404,4732,6100,3036,3298,7125,1850,5291,4675,1592,2920,1863,4336,2617,3005,3194,5678,2235,2707,6530,6150,5512,671,3485,4678,4962,1752,72,555,2147,4358,1,5510,5043,3800,2433,5246,1230,5518,5734,4505,4598,806,4026,7434,3534,2695,6563,6164,2472,5182,4995,2160,4174,6895,711,6439,151,2092,4162,380,6467,1040,4665,2643,6174,3168,2113,6264,2061,7309,3458,7248,2963,4106,5563,7148,1821,3921,5297,6640,1926,4098,5676,3292,6378,7226,6542,5368,939,5138,2677,572,3348,625,5509,5846,6824,3963,3795,3120,1825,5269,4955,1448,6267,1391,632,5963,7043,724,7174,93,3068,5554,2443,4230,6185,4198,3501,6376,6146,5778,3467,6683,7091,2636,4243,1675,1438,3203,5070,6806,3090,1973,2027,900,7180,3808,2901,6505,3770,5507,718,1888,514,5357,3433,1335,3952,3768,832,5117,4588,5022,2915,6975,2994,6351,2242,5589,85,5728,5578,1145,6301,6684,4646,4164,5019,5522,2938,3908,4534,7192,2723,2834,1823,2939,3054,7433,1758,4818,342,479,1008,5754,4051,758,7249,6550,6201,3586,4114,1345,3103,1417,2110,523,2419,2183,4981,1403,3756,231,1630,3727,5356,4278]
use_column = [i-1 for i in use_column_incsv]
user_head = []
for i in use_column:
    user_head.append(bdf_head[i])

M = int(math.log(len(use_column_incsv)))+1

# Y_fac = pd.factorize(bdf[user_head[-1]])[0]
Y_fac = list(pd.factorize(bdf.iloc[:,-1])[0])

df = bdf[user_head] #only features
df['class'] = Y_fac

# df.insert(-1, "class", list(Y_fac), True) 



def get_test_row(num_user = 50):
    
    test_ind_dic = {i:random.randint(1,9) for i in range(50)}
    num_user_dic = {}
    test_row = []
    for ind, user in enumerate(Y_fac):
        if user not in num_user_dic:
            num_user_dic[user] = 1
        else:
            num_user_dic[user] += 1
        if num_user_dic[user] == test_ind_dic[user]:
            test_row.append(ind)

    return test_row
 
testrow = get_test_row()

#test set
df_test = df.iloc[testrow,:]

dddd = df_test.iloc[:,0:-1]
X_test = df_test[user_head] #Yclass is not in user_head
Y_test = df_test.iloc[:,-1]


#train set
df_train = df.drop(df.index[testrow])
X_train = df_train[user_head]
Y_train = df_train.iloc[:,-1]

#classfier
clf = RandomForestClassifier(n_estimators=300, criterion='entropy', max_features=M)
clf.fit(X_train,Y_train)

Y_predict = clf.predict(X_test)
print Y_predict
print Y_test

wrong = 0
for i in range(len(Y_predict)):
    if list(Y_predict)[i] == list(Y_test)[i]:
        wrong += 1

accuracy = float(wrong)/len(Y_predict)
print accuracy
