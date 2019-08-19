import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_LeavesAD(file_cursor):
    def get_leaves_inside(cur,ld={}, level = 1):
        if any(True for _ in cur.get_children()) == False:
            # print "ffff"
            if cur.spelling.strip():
                leave = cur.spelling
                if leave not in ld:
                    ld[leave] = [level]
                else:
                    ld[leave].append(level)
        else:
            # print "t"
            for c in cur.get_children():
                get_leaves_inside(c, ld, level+1)

    def trans(d,s):
        d_out = {}
        for i,raw_feature in enumerate(d):
            new_feature = str(s) + str(raw_feature)
            d_out[new_feature] = d[raw_feature]
        return d_out
    
    ld_tem = {}
    get_leaves_inside(cur = file_cursor, ld = ld_tem)

    ld_out = {}
    for l in ld_tem:
        ld_out[l] = float(sum(ld_tem[l]))/len(ld_tem[l])

    #translate
    ld_tran_out = trans(d = ld_out, s = "s9_feature")

    
    return ld_tran_out

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test4.cpp')
    a = get_LeavesAD(tu.cursor)
    print a