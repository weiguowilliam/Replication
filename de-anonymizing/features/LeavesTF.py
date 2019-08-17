import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
from utils import *
Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_LeavesTF(file_cursor,idf_dic):
    def get_leaves_inside(cur,ld={}):
        if any(True for _ in cur.get_children()) == False:
            # print "ffff"
            if cur.spelling.strip():
                leave = cur.spelling
                if leave not in ld:
                    ld[leave] = 1
                else:
                    ld[leave] += 1 
        else:
            # print "t"
            for c in cur.get_children():
                get_leaves_inside(c, ld)

    
    ld_tem = {}
    get_leaves_inside(cur = file_cursor, ld = ld_tem)

    ls = 0
    for l in ld_tem:
        ls += ld_tem[l]
    
    ld_out = {}
    for l in ld_tem:
        ld_out[l] = float(ld_tem[l])/ls

    #tfidf
    ld_idf_out = {}
    for l in ld_tem:
        ld_idf_out[l] = float(ld_out[l]) * idf_dic[l]


    #translate
    tf_tran_out = trans(d = ld_out, s = "leavesTF")
    tfidf_tran_out = trans(d = ld_idf_out, s = "leavesTFIDF")
    
    return tf_tran_out,tfidf_tran_out
        




if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test4.cpp')
    # print get_LeavesTF(tu.cursor)
    # print next(next(tu.cursor.get_children()).get_children()).spelling
    # a = tu.cursor.get_children()
    # print any(True for _ in a)