
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")



# def get_dep_inside(cursor, level = 0, NodeTypeDic = {}):
#     """
#     store the depth of each node into depthlist, use max(depthlist) to get the MaxDepthASTNode of each tree
#     """
#     for c in cursor.get_children():
#         # print "The kind of cursor is",c.kind
#         if c.kind not in NodeTypeDic:
#             # print "new type"
#             NodeTypeDic[c.kind] = [level+1]
#         else:
#             # print "exsited type"
#             temp = NodeTypeDic[c.kind]
#             # print "the depth list of this type is",temp
#             # print type(temp)
#             temp.append(level+1)
#             NodeTypeDic[c.kind] = temp
#         # print "new depth list of this type is",NodeTypeDic[c.kind]
        
#         # print c.kind
#         # print c.type.kind
#         get_dep_inside(c, level+1, NodeTypeDic)

# def get_avgdep(DepthListDict={}):
#     add = {}
#     for i in DepthListDict:
#         tem = DepthListDict[i]
#         add[i] = float(sum(tem))/len(tem)
    
#     return add

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

    avgdepth_tem = {}
    get_dep_inside(cursor = file_cursor, level = 0, NodeTypeDic= avgdepth_tem)
    avg_depth_dic = get_avgdep(avgdepth_tem)
    return avg_depth_dic


if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    print 'Translation unit:', tu.spelling
    # ntd = {}
    # get_dep_inside(cursor = tu.cursor, level = 0, NodeTypeDic=ntd)
    # r = get_avgdep(ntd)
    # print r
    a = get_ASTNodeTypeAvgDepth(tu.cursor)
    print a
        
