
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")



def get_ast(cursor, level = 0, NodeTypeDic = {}):
    """
    store the depth of each node into depthlist, use max(depthlist) to get the MaxDepthASTNode of each tree
    """
    for c in cursor.get_children():
        # print "The kind of cursor is",c.kind
        if c.kind not in NodeTypeDic:
            # print "new type"
            NodeTypeDic[c.kind] = [level+1]
        else:
            # print "exsited type"
            temp = NodeTypeDic[c.kind]
            # print "the depth list of this type is",temp
            # print type(temp)
            temp.append(level+1)
            NodeTypeDic[c.kind] = temp
        # print "new depth list of this type is",NodeTypeDic[c.kind]
        
        # print c.kind
        # print c.type.kind
        get_ast(c, level+1, NodeTypeDic)

def get_avgdep(DepthListDict={}):
    add = {}
    for i in DepthListDict:
        tem = DepthListDict[i]
        add[i] = sum(tem)/len(tem)
    
    return add



if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    print 'Translation unit:', tu.spelling
    ntd = {}
    get_ast(cursor = tu.cursor, level = 0, NodeTypeDic= ntd)
    # print ntd
    res = get_avgdep(ntd)
    # print res

        
