
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import os
import math

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_lf(dic_path):
    def get_leaves_inside(cur,ld={}):
        if any(True for _ in cur.get_children()) == False:
            # print "ffff"
            if cur.spelling.strip():
                leave = cur.spelling
                if leave not in ld:
                    ld[leave] = 1
                # else:
                #     ld[leave] += 1 
        else:
            # print "t"
            for c in cur.get_children():
                get_leaves_inside(c, ld)
    
    
    lod = {}
    for r,d,f in os.walk(dic_path):
        for file in f:
            if str(file) != '.DS_Store':
                dic_tem = {}
                f_path = os.path.join(r, file)
                index = clang.cindex.Index.create()
                tu = index.parse(f_path)
                get_leaves_inside(tu.cursor, dic_tem)
                lod[file] = dic_tem
        

    
    feature_occ_tf = {}
    file_len = len(lod)
    for file in lod:
        for feature in lod[file]:
            if str(feature) not in feature_occ_tf:
                feature_occ_tf[str(feature)] = lod[file][feature]
            else:
                feature_occ_tf[str(feature)] += lod[file][feature]
    
    out_dic = {}
    for feature in feature_occ_tf:
        out_dic[feature] = math.log(float(file_len)/feature_occ_tf[feature])

    return out_dic


def get_DocumentFrequency(dic_path):

    def get_occ(file_cursor, NodeTypeDic = {}):
        for c in file_cursor.get_children():
            if c.kind not in NodeTypeDic:
                NodeTypeDic[c.kind] = 1
            # else:
            #     NodeTypeDic[c.kind] += 1
            get_occ(c,NodeTypeDic)
    

    node_orr_dic = {}
    
    for r,d,f in os.walk(dic_path):
        for file in f:
            if str(file) != '.DS_Store':
                dic_tem = {}
                f_path = os.path.join(r, file)
                index = clang.cindex.Index.create()
                tu = index.parse(f_path)
                get_occ(tu.cursor, dic_tem)
                node_orr_dic[file] = dic_tem
        
    
    feature_occ_tf = {}
    file_num = len(node_orr_dic)
    for file in node_orr_dic:
        for feature in node_orr_dic[file]:
            if str(feature) not in feature_occ_tf:
                feature_occ_tf[str(feature)] = node_orr_dic[file][feature]
            else:
                feature_occ_tf[str(feature)] += node_orr_dic[file][feature]

    dic_out = {}
    for feature in feature_occ_tf:
       dic_out[feature] = math.log(float(file_num)/feature_occ_tf[feature]) 
    
    return dic_out

def trans(d,s):
        d_out = {}
        for raw_feature in d:
            new_feature = str(s) + str(raw_feature)
            d_out[new_feature] = d[raw_feature]
        return d_out
        
if __name__ == '__main__':
    # get_lf("/Users/weiguo/Desktop/traindata",2)
    a = get_DocumentFrequency(dic_path = "/Users/weiguo/Desktop/traindata")




    
    

        