
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_ast(cur, UniDic = {}):
        '''
        tokenize cpp file and store the unigram into a dictionary
        '''
        for token in cur.get_tokens():
            str_token = token.spelling
            if str_token not in UniDic:
                UniDic[str_token] = 1
            else:
                UniDic[str_token] += 1

        cursor_content=""
        for token in cur.get_tokens():
            str_token = token.spelling+" "
            cursor_content = cursor_content+str_token


if __name__ == '__main__':
    index = clang.cindex.Index.create()
    # tu = index.parse('test1.cpp')
    tu = index.parse('test2.cpp')
    print 'Translation unit:', tu.spelling
    print tu.cursor.kind
    bd = {}
    get_ast(tu.cursor,bd)
    print len(bd)
    print bd
