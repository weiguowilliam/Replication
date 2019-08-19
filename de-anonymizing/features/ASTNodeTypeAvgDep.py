
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")



def get_ASTNodeTypeAvgDepth(file_cursor):
    def get_dep_inside(cursor, level = 0, NodeTypeDic = {}):
        for c in cursor.get_children():
            feature_name = "NodeTypeAvgDep" + str(c.kind)
            if feature_name not in NodeTypeDic:
                NodeTypeDic[feature_name] = [level+1]
            else:
                temp = NodeTypeDic[feature_name]
                temp.append(level+1)
                NodeTypeDic[feature_name] = temp
            get_dep_inside(c, level+1, NodeTypeDic)
    
    def get_avgdep(DepthListDict):
        add = {}
        for i in DepthListDict:
            tem = DepthListDict[i]
            add[i] = float(sum(tem))/len(tem)
        return add

    def trans(d,s):
        d_out = {}
        for i, raw_feature in enumerate(d):
            new_feature = str(s) + str(i)
            d_out[new_feature] = d[raw_feature]
        return d_out

    avgdepth_tem = {}
    get_dep_inside(cursor = file_cursor, level = 0, NodeTypeDic= avgdepth_tem)
    avg_depth_dic = get_avgdep(avgdepth_tem)
    # avg_out = trans(avg_depth_dic,"s5_feature")
    return avg_depth_dic


if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    print 'Translation unit:', tu.spelling
    a = get_ASTNodeTypeAvgDepth(tu.cursor)
    print a
        
