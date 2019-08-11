import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import math
Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_ast(cur):
    num_token = 0
    for token in cur.get_tokens():
        num_token += 1
        # str_token = token.spelling
        # if str_token == "?":
        #     num_ternary += 1
    
    def get_file_length(cur):
        cursor_content=""
        for token in cur.get_tokens():
            str_token = token.spelling
            cursor_content = cursor_content+str_token
        return len(cursor_content)
    
    file_length = get_file_length(cur = cur)
    
    num_return = math.log(float(num_token)/file_length)
    
    return num_return
    

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    # tu = index.parse('test1.cpp')
    tu = index.parse('test2.cpp')
    print 'Translation unit:', tu.spelling
    print tu.cursor.kind
    # bd = {}
    print get_ast(tu.cursor)
    # print len(bd)
    # print bd