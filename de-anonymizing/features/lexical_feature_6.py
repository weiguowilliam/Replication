import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import math

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_l6(file_cursor):
    def ast(cur,literal_list = []):
        """
        count the number of string,character,numeric literal
        literal = constance
        """
        for c in cur.get_children():
            if c.kind == CursorKind.INTEGER_LITERAL:
                literal_list.append(1)
                # print literal_list
                # print "aloha"
            elif c.kind == CursorKind.FLOATING_LITERAL:
                literal_list.append(1)
            elif c.kind == CursorKind.IMAGINARY_LITERAL:
                literal_list.append(1)
            elif c.kind == CursorKind.STRING_LITERAL:
                literal_list.append(1)
            elif c.kind == CursorKind.CHARACTER_LITERAL:
                literal_list.append(1)
            else:
                pass

            ast(c, literal_list)

    def get_file_length(cur):
        cursor_content=""
        for token in cur.get_tokens():
            str_token = token.spelling
            cursor_content = cursor_content+str_token
        return len(cursor_content)

    l_literal = []
    ast(file_cursor, l_literal)
    num_literal = len(l_literal)
    file_length = get_file_length(file_cursor)

    if num_literal == 0:
        return 0
    else:
        return math.log(float(num_literal)/file_length)

def test_ast(cursor):
    def spell(cursor):
        if cursor.spelling.strip():
            return cursor.kind,cursor.spelling
        else:
            return cursor.kind,""
    
    print spell(cursor)
    if cursor.kind == CursorKind.INTEGER_LITERAL:
        print "aloha"

    for cur in cursor.get_children():
        test_ast(cur)

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test2.cpp')
    print get_l6(tu.cursor)
    # test_ast(tu.cursor)

