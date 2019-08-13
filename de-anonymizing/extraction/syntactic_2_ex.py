import os
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

sys.path.append(os.path.abspath("/Users/weiguo/Desktop/Replication/de-anonymizing/features"))
from ASTNodeBigramTF import *
Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")


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
            get_ast(tu.cursor,num_user_dict[user])
    # return num_user_dict 

    num_user_all_dict = {i:{} for i in num_user_list}
    for user in num_user_list:
        num_user_all_dict[user] = num_user_dict[user]
        for other_user in num_user_dict:
            if other_user != user:
                for item in num_user_dict[other_user]:
                    if item not in num_user_all_dict[user]:
                        num_user_all_dict[user][item] = 0
    
    return num_user_all_dict, num_user_dict
                    



if __name__ == '__main__':
    a,b = syntactic_2_extractor(num_user= 4)
    for i in a:
        print len(a[i])
    for i in b:
        print len(b[i])