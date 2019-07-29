
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")



def get_ast(cursor, NodeTypeDic = {}):
    """
    store the occurance of each node in dictionary NodeTypeDic
    """
    for c in cursor.get_children():
        if c.kind not in NodeTypeDic:
            NodeTypeDic[c.kind] = 1
        else:
            NodeTypeDic[c.kind] += 1
        # print c.kind
        # print c.type.kind
        get_ast(c, NodeTypeDic)

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    print 'Translation unit:', tu.spelling
    ntd = {}
    get_ast(tu.cursor, NodeTypeDic= ntd)
    print ntd
    print len(ntd)

    # ck = CursorKind.get_all_kinds()
    # print len(ck)
    # There are 205 node kinds in Clang, different from 58 types in joern.

        
