import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import math

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_ast(file_cursor):
    def ast(cursor,func_list = []):
        """
        """
        if cursor.kind == CursorKind.FUNCTION_DECL:
            func_list_tem = []
        for c in cursor.get_children():
            parent_kind = cursor.kind
            children_kind = c.kind
            if (parent_kind == CursorKind.FUNCTION_DECL) and (children_kind == CursorKind.PARM_DECL):
                func_list_tem.append(1)
            ast(c,func)
        if cursor.kind == CursorKind.FUNCTION_DECL:
            func_list.append(func_list_tem)
    
    func = []
    ast(cursor = file_cursor, func_list = func)
    len_list = [len(x) for x in func]
    return float(sum(len_list))/len(len_list)


        

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test3.cpp')
    # func = []
    print get_ast(tu.cursor)
    
    # print get_ast(tu.cursor)
    # test_ast(tu.cursor)