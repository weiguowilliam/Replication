import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
from utils import *
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

    
    ld_tem = {}
    get_leaves_inside(cur = file_cursor, ld = ld_tem)

    ld_out = {}
    for l in ld_tem:
        ld_out[l] = float(sum(ld_tem[l]))/len(ld_tem[l])

    #translate
    ld_tran_out = trans(d = ld_out, s = "levesAD")

    
    return ld_tran_out