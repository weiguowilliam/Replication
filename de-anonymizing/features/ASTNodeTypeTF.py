
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")


def get_ASTNodeTypeTF(file_cursor):

    def get_ASTNodeTypeTF_inside(cursor, NodeTypeDic = {}):
        """
        store the occurance of each node in dictionary NodeTypeDic
        """
        for c in cursor.get_children():
            feature_name = "NodeTypeTF" + str(c.kind)
            if feature_name not in NodeTypeDic:
                NodeTypeDic[feature_name] = 1
            else:
                NodeTypeDic[feature_name] += 1
            get_ASTNodeTypeTF_inside(c, NodeTypeDic)
    
    def get_bi_tf(rd = {}):
        tf_d = {i:0 for i in rd}
        sum_node = 0
        for i in rd:
            sum_node += rd[i]
        for i in tf_d:
            tf_d[i] = float(rd[i])/sum_node
        return tf_d

    dic_tem = {}
    get_ASTNodeTypeTF_inside(cursor = file_cursor, NodeTypeDic=dic_tem)
    dic_out = get_bi_tf(rd = dic_tem)
    return dic_out
    

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    print 'Translation unit:', tu.spelling
    
    ntd = get_ASTNodeTypeTF(tu.cursor)
    print ntd
    print len(ntd)

    # ck = CursorKind.get_all_kinds()
    # print len(ck)
    # There are 205 node kinds in Clang, different from 58 types in joern.

        
