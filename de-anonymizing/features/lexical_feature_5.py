import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import math

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_l5(cursor):
    """
    store the depth of each node into depthlist, use max(depthlist) to get the MaxDepthASTNode of each tree
    """
    num_comment = 0
    for t in cursor.get_tokens():
        if (t.spelling[0:2] == "//") or (t.spelling[0:2]=="/*"):
            num_comment += 1
    
    def get_file_length(cur):
        cursor_content=""
        for token in cur.get_tokens():
            str_token = token.spelling
            cursor_content = cursor_content+str_token
        return len(cursor_content)

    file_length = get_file_length(cur = cursor)
    
    if num_comment == 0:
        num_return = 0
    else:
        num_return = math.log(float(num_comment)/file_length)
    
    return num_return


if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test2.cpp')
    get_l5(tu.cursor)