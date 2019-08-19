
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_L1(file_cursor):
    '''
    tokenize cpp file and store the unigram into a dictionary
    '''
    UniDic= {}
    token_len = 0
    for token in file_cursor.get_tokens():
        token_len += 1
        str_token = token.spelling
        if str_token not in UniDic:
            UniDic[str_token] = 1
        else:
            UniDic[str_token] += 1
        
    for token in UniDic:
        tem = UniDic[token]
        UniDic[token] = float(tem)/token_len

    def trans(d,s):
        d_out = {}
        for i,raw_feature in enumerate(d):
            new_feature = str(s) + str(raw_feature)
            d_out[new_feature] = d[raw_feature]
        return d_out

    dic_out = trans(UniDic,'l1_feature')
    return dic_out


if __name__ == '__main__':
    index = clang.cindex.Index.create()
    # tu = index.parse('test1.cpp')
    tu = index.parse('test2.cpp')
    print 'Translation unit:', tu.spelling
    print tu.cursor.kind
    bd = get_L1(tu.cursor)
    print len(bd)
    print bd
