import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import math

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_l10(cur):
    def ast(cursor, level = 0, depthlist = []):
        """
        control statement:if-else, switch,for, while, do-while
        CursorKind.IF_STMT,CursorKind.SWITCH_STMT,CursorKind.WHILE_STMT,CursorKind.DO_STMT,CursorKind.FOR_STMT
        """
        if (cursor.kind == CursorKind.IF_STMT) or (cursor.kind == CursorKind.SWITCH_STMT) or (cursor.kind == CursorKind.WHILE_STMT) or (cursor.kind == CursorKind.DO_STMT) or (cursor.kind == CursorKind.FOR_STMT):
            level += 1

        depthlist.append(level)
        for c in cursor.get_children():
            ast(c,  level, depthlist)
    
    def get_file_length(cur):
        cursor_content=""
        for token in cur.get_tokens():
            str_token = token.spelling
            cursor_content = cursor_content+str_token
        return len(cursor_content)

    dll = []
    ast(cursor = cur, level = 0, depthlist= dll)
    max_d = max(dll)
    file_length = get_file_length(cur)

    if max_d == 0:
        return 0
    else:
        return math.log(float(max_d)/file_length)




def test_ast(cursor):
    def spell(cursor):
        if cursor.spelling.strip():
            return cursor.kind,cursor.spelling
        else:
            return cursor.kind,""
    
    print spell(cursor)
    # if cursor.kind == CursorKind.FUNCTION_DECL:
    # if (cursor.kind == CursorKind.PREPROCESSING_DIRECTIVE) or (cursor.kind == CursorKind.MACRO_DEFINITION) or (cursor.kind == CursorKind.MACRO_INSTANTIATION) or (cursor.kind == CursorKind.INCLUSION_DIRECTIVE):
    #     print "aloha"

    for cur in cursor.get_children():
        test_ast(cur)

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    print get_l10(tu.cursor)
    # test_ast(tu.cursor)
    # dll = []
    # get_ast(cursor = tu.cursor, level = 0, depthlist= dll)
    # print max(dll)
    # print dll