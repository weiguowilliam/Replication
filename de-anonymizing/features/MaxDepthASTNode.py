
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")



# def get_ast(cursor, level = 0, depthlist = []):
#     """
#     store the depth of each node into depthlist, use max(depthlist) to get the MaxDepthASTNode of each tree
#     """
#     depthlist.append(level)
#     for c in cursor.get_children():
#         get_ast(c,  level+1, depthlist)

def get_MaxDepthNode(file_cursor):

    def get_mdn_inside(cursor, level = 0, depthlist = []):
        depthlist.append(level)
        for c in cursor.get_children():
                get_mdn_inside(c,  level+1, depthlist)
    
    dll_tem = [0]
    get_mdn_inside(cursor = file_cursor, level = 0, depthlist = dll_tem)
    return max(dll_tem)

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test2.cpp')
    print 'Translation unit:', tu.spelling
    print get_MaxDepthNode(tu.cursor)
#     dll = [0]
#     get_MaxDepthNode(cursor = tu.cursor, level = 0, depthlist= dll)
#     print max(dll)

        
