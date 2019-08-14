import os
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import pandas as pd
import pickle

sys.path.append(os.path.abspath("/Users/weiguo/Desktop/Replication/de-anonymizing"))
# from features.ASTNodeBigramTF import get_bigram
# from features.ASTNodeBigramTF import get_bigram
from features.ASTNodeBigramTF import get_bigram
Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")


def syntactic_2_extractor_nb(num_user = 2, num_file_per_author = 9):

    path = "/Users/weiguo/Desktop/traindata"
    i = 0
    num_file_dict = {}
    for r, d, f in os.walk(path):
        
        for file in f:
            if str(file) != '.DS_Store':
                num_file_dict[file] = {}
                f_path = os.path.join(r, file)
                index = clang.cindex.Index.create()
                tu = index.parse(f_path)
                get_bigram(tu.cursor, num_file_dict[file])
                # file_class_tem = str(file).split('.')[0:-1] #delete ".cpp"
                file_class_tem = str(file)[0:-4]
                file_class = file_class_tem.split('_')[-1]
                num_file_dict[file]['class'] = file_class
        i += 1
        if i > num_user:
            break

    num_file_all_dict = {i:{} for i in num_file_dict}
    for file in num_file_dict:
        num_file_all_dict[file] = num_file_dict[file]
        for other_file in num_file_dict:
            if other_file != file:
                for item in num_file_dict[other_file]:
                    if item not in num_file_dict[file]:
                        num_file_all_dict[file][item] = 0

    for file in num_file_all_dict:
        file_sample = file
        item_len = num_file_all_dict[file_sample]
        break

    trans_dict = {}
    i = 0
    for old_feature in num_file_all_dict[file_sample]:
        if old_feature != 'class':
            new_feature_name = "bigram" + str(i)
            trans_dict[old_feature] = new_feature_name
            i += 1
    trans_dict['class'] = 'class'
    out_dict = {i:{} for i in num_file_all_dict}

    for file in out_dict:
        for old_feature in num_file_all_dict[file]:
            new_feature = trans_dict[old_feature]
            out_dict[file][new_feature] = num_file_all_dict[file][old_feature]
    
    return out_dict

#this one is wrong.
def syntactic_2_extractor(num_user = 50):
    path = "/Users/weiguo/Desktop/traindata"
    all_user_list = next(os.walk(path))[1]
    num_user_list = all_user_list[0:num_user]
    num_user_dict = {i:{} for i in num_user_list}
    for user in num_user_list:
        user_path = os.path.join(path,user)
        for f in os.listdir(user_path):
            f_path = os.path.join(user_path,f)
            index = clang.cindex.Index.create()
            tu = index.parse(f_path)
            # print tu.spelling
            # print len(num_user_dict[user])
            get_bigram(tu.cursor,num_user_dict[user])
            # print len(num_user_dict[user])
        # print "*********"
    # return num_user_dict 

    num_user_all_dict = {i:{} for i in num_user_list}
    for user in num_user_list:
        num_user_all_dict[user] = num_user_dict[user]
        for other_user in num_user_dict:
            if other_user != user:
                for item in num_user_dict[other_user]:
                    if item not in num_user_all_dict[user]:
                        num_user_all_dict[user][item] = 0

    for user in num_user_all_dict:
        user_sample = user
        item_len = num_user_all_dict[user]
        break
    
    
    trans_dict = {}
    i = 0
    for f in num_user_all_dict[user_sample]:
        new_feature_name = "bigram" + str(i)
        # trans_dict[new_feature_name] = f
        trans_dict[f] = new_feature_name
        i += 1
    
    out_dict = {i:{} for i in num_user_list}
    for user in out_dict:
        for old_feature in num_user_all_dict[user]:
            new_f = trans_dict[old_feature]
            out_dict[user][new_f] = num_user_all_dict[user][old_feature]

    return out_dict

            



if __name__ == '__main__':
    b = syntactic_2_extractor_nb(num_user=5)
    b_frame = pd.DataFrame.from_dict(b,orient='index')
    b_frame.to_csv('/Users/weiguo/Desktop/Replication/de-anonymizing/data/bigram0814.csv')
    
    