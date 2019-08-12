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
        token_spelling = token.spelling
        # print token_spelling
        if token_spelling == "#":
            num_token += 1
            # print "aloha"
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
    
    if num_token == 0:
        return 0
    else:
        num_return = math.log(float(num_token)/file_length)
    
    return num_return




def test_ast(cursor):
    def spell(cursor):
        if cursor.spelling.strip():
            return cursor.kind,cursor.spelling
        else:
            return cursor.kind,""
    
    print spell(cursor)
    # if cursor.kind == CursorKind.FUNCTION_DECL:
    if (cursor.kind == CursorKind.PREPROCESSING_DIRECTIVE) or (cursor.kind == CursorKind.MACRO_DEFINITION) or (cursor.kind == CursorKind.MACRO_INSTANTIATION) or (cursor.kind == CursorKind.INCLUSION_DIRECTIVE):
        print "aloha"

    for cur in cursor.get_children():
        test_ast(cur)

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test2.cpp')
    print get_ast(tu.cursor)
    # test_ast(tu.cursor)