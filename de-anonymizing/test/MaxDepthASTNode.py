
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_ast(cursor, level = 0):
    print level
    for c in cursor.get_children():
        get_ast(c,  level+1)
        

class features(object):
    def __init__(self):
        self.depth = []

    def get_ast(self, cursor, level = 0):
        self.depth.append(level)
        print level
        for c in cursor.get_children():
            get_ast(c,  level+1)
        

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    print 'Translation unit:', tu.spelling
    a = features()
    a.get_ast(tu.cursor)
    print a.depth
    # get_ast(tu.cursor)


#TODO
#store the depth to a list and return max(depth list)
