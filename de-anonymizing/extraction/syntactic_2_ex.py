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
            # print tu.spelling
            # print len(num_user_dict[user])
            get_ast(tu.cursor,num_user_dict[user])
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
    
    return num_user_all_dict
    # return num_user_all_dict, num_user_dict
    # return num_user_dict
                    



if __name__ == '__main__':
    b = syntactic_2_extractor(num_user= 2)
    for user in b:
        print len(a[user])
    #test right: 154 in first user, 147 in second user, 199 differeent pairs, so 51 pair in common, then total number = 154+147-51 = 250
    # test different number of pairs
    # i = 0
    # for user in a:
    #     for item in a[user]:
    #         for uuser in a:
    #             if uuser != user:
    #                 if item not in a[uuser]:
    #                     i += 1
    # print i
    