# this file is for informative features

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import random
import math
from sklearn.metrics import confusion_matrix
import numpy as np

#0818
# bdf = pd.read_csv("/Users/weiguo/Desktop/Replication/de-anonymizing/data/bigram_50.csv") #50 all features
# bdf = pd.read_csv("/Users/weiguo/Desktop/Replication/de-anonymizing/data/data_50.csv") # 50 informative
# bdf = pd.read_csv("/Users/weiguo/Desktop/Replication/de-anonymizing/data/bigram0818_100.csv")  #this uses all features
# bdf = pd.read_csv("/Users/weiguo/Desktop/Replication/de-anonymizing/data/data_100.csv")
#0819
# bdf = pd.read_csv("/Users/weiguo/Desktop/Replication/de-anonymizing/data/DATA50ori_0819.csv") # 50 ALL FEATURES
bdf = pd.read_csv("/Users/weiguo/Desktop/Replication/de-anonymizing/data/data0823.csv") # 50 informative

bdf_head = list(bdf.columns) 
use_head = bdf_head

user_head = bdf_head[0:-1]

M = int(math.log(len(bdf_head)))+1

Y_fac = list(pd.factorize(bdf.iloc[:,-1])[0])
label_list = pd.factorize(bdf.iloc[:,-1])

df = bdf[user_head] #only features
df['class'] = Y_fac

def get_test_row(num_user = 50):
    
    test_ind_dic = {i:random.randint(1,9) for i in range(num_user)}
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

def stratified_cv(term = 9):
    list_accuracy = []
    confuse = np.array([0])
    for i in range(term):
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


        wrong = 0
        for i in range(len(Y_predict)):
            if list(Y_predict)[i] == list(Y_test)[i]:
                wrong += 1

        accuracy = float(wrong)/len(Y_predict)
        list_accuracy.append(accuracy)
        cm = confusion_matrix(y_true = Y_test, y_pred = Y_predict)
        cm_np = np.array(cm)
        confuse  = confuse + cm_np

    return float(sum(list_accuracy))/len(list_accuracy), confuse

# ac, ma = stratified_cv()
# print ac
# print ma
# a = np.asarray(ma)
# np.savetxt("foo.csv", a, delimiter=",")

#accuracy = 0.958 with informative features
#accuracy = 0.866 with all features

# print label_list
i = 0
m = np.array([0])
acc = []
while i<10:
    ac, mm = stratified_cv()
    acc.append(ac)
    m = m+mm
    print ac
    i += 1
print float(sum(acc))/len(acc)
np.savetxt("foo.csv", m, delimiter=",")


