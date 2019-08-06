
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

import math

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_lexical_feature_2(cursor):
    
    def get_ast(cur):
        '''
        use variable pre_str to get pre_str-this_str to catch "else if" structure
        '''
        NumKeyDic = {}
        pre_str = ""
        for token in cur.get_tokens():
            this_str = token.spelling
            if pre_str+this_str == "elseif":
                if "elseif" not in NumKeyDic:
                    NumKeyDic["elseif"] = 1
                else:
                    NumKeyDic["elseif"] += 1
            else:
                if this_str not in NumKeyDic:
                    NumKeyDic[this_str] = 1
                else:
                    NumKeyDic[this_str] += 1
            
            pre_str = this_str
        
        if "elseif" in NumKeyDic:
            NumKeyDic["else"] -= NumKeyDic["elseif"]
        
        return NumKeyDic
    
    def get_keyword(dic):
        key_list = ['do','elseif','if','else','switch','for','while']
        key_dic = {}
        for k in key_list:
            if k in dic:
                key_dic[k] = math.log(float(dic[k])/file_length)
            else:
                # key_dic[k] = 0
                key_dic[k] = -10000 #since ln(0) is invalid, it is negative infinity.
        return key_dic

    def get_file_length(cur):
        cursor_content=""
        for token in cur.get_tokens():
            str_token = token.spelling
            cursor_content = cursor_content+str_token
        return len(cursor_content)
    
    file_length = get_file_length(cur = cursor)
    nkd = get_ast(cur = cursor)
    okd = get_keyword(dic = nkd)
    return okd




if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    # tu = index.parse('test2.cpp')
    print 'Translation unit:', tu.spelling
    print tu.cursor.kind
    # bd = {}
    bd = get_lexical_feature_2(tu.cursor)
    print len(bd)
    print bd
    print bd['else']
