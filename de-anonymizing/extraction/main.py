import os
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import pandas as pd
import pickle
import math
Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")
sys.path.append(os.path.abspath("/Users/weiguo/Desktop/Replication/de-anonymizing"))
#syntactic features
from features.ASTNodeBigramTF import get_bigram
from features.MaxDepthASTNode import get_MaxDepthNode
from features.ASTNodeTypeTF import get_ASTNodeTypeTF
from features.ASTNodeTypeAvgDep import get_ASTNodeTypeAvgDepth
from features.cppKeywords import get_cppKeywords
from features.utils import *
from features.LeavesTF import get_LeavesTF
from features.LeavesAvgDep import get_LeavesAD
#lexical features
from features.WordUnigram import get_L1
from features.lexical_feature_2 import get_l2
from features.lexical_feature_3 import get_l3
from features.lexical_feature_4 import get_l4
from features.lexical_feature_5 import get_l5
from features.lexical_feature_6 import get_l6
from features.lexical_feature_7 import get_l7
from features.lexical_feature_8 import get_l8
from features.lexical_feature_9 import get_l9
from features.lexical_feature_10 import get_l10
from features.lexical_feature_12 import get_l12
from features.lexical_feature_14 import get_l14
#layout features
from features.layout_1 import get_lay1
from features.layout_6 import get_lay6

def syntactic_2_extractor_nb(num_user = 2, num_file_per_author = 9):

    path = "/Users/weiguo/Desktop/traindata"
    
    feature_idf_dict = get_DocumentFrequency(dic_path = path)
    leaves_idf_dict = get_lf(dic_path = path)
        
    i = 0
    num_file_dict = {}
    for r, d, f in os.walk(path):
        
        for file in f:
            if str(file) != '.DS_Store':
                num_file_dict[file] = {}
                f_path = os.path.join(r, file)
                index = clang.cindex.Index.create()
                tu = index.parse(f_path)

            #syntactic features
                #get bigram feature
                bgd = get_bigram(tu.cursor)
                num_file_dict[file].update(bgd)
                   
                #get max depth feature
                num_file_dict[file]['maxdepthnode'] = get_MaxDepthNode(tu.cursor)
                
                #get file class(author)
                file_class_tem = str(file)[0:-4]
                file_class = file_class_tem.split('_')[-1]
                num_file_dict[file]['class'] = file_class
                
                #get node type frequency,tfidf:
                ntf,ntfidf = get_ASTNodeTypeTF(tu.cursor, feature_idf_dict)
                num_file_dict[file].update(ntf)
                num_file_dict[file].update(ntfidf)

                #get node type average depth
                avg_depth_dic = get_ASTNodeTypeAvgDepth(tu.cursor)
                num_file_dict[file].update(avg_depth_dic)

                #get cppKeywords frequency(syntactic)
                keywords_dic = get_cppKeywords(tu.cursor)
                num_file_dict[file].update(keywords_dic)

                #get leavesTF,tfidf
                leavestf_dic, leavestfidf_dic = get_LeavesTF(file_cursor = tu.cursor, idf_dic = leaves_idf_dict)
                num_file_dict[file].update(leavestf_dic)
                num_file_dict[file].update(leavestfidf_dic)

                #get leaves Avg Depth
                leavesad_dic = get_LeavesAD(file_cursor = tu.cursor)
                num_file_dict[file].update(leavesad_dic)
            
            #lexical features
                #get WordUnigramTF
                l1_dic = get_L1(file_cursor = tu.cursor)
                num_file_dict[file].update(l1_dic)
                #get l2
                l2_dic = get_l2(tu.cursor)
                num_file_dict[file].update(l2_dic)
                #get l3
                num_file_dict[file]['l3feature'] = get_l3(tu.cursor)
                #get l4
                num_file_dict[file]['l4feature'] = get_l4(tu.cursor)
                #get l5
                num_file_dict[file]['l5feature'] = get_l5(tu.cursor)
                #get l6
                num_file_dict[file]['l6feature'] = get_l6(tu.cursor)
                #get l7
                num_file_dict[file]['l7feature'] = get_l7(tu.cursor)
                #get l8
                num_file_dict[file]['l8feature'] = get_l8(tu.cursor)
                #get l9
                num_file_dict[file]['l9feature'] = get_l9(tu.cursor)
                #get l10
                num_file_dict[file]['l10feature'] = get_l10(tu.cursor)
                #get l12, l13
                num_file_dict[file]['l12feature'] = get_l12(tu.cursor)[0]
                num_file_dict[file]['l13feature'] = get_l12(tu.cursor)[1]
                #get l14, l15
                num_file_dict[file]['l14feature'] = get_l14(fname = f_path)[0]
                num_file_dict[file]['l15feature'] = get_l14(fname = f_path)[1]
            
            #layout features
                #lay1, lay2, lay3, lay4, lay5
                num_file_dict[file]['lay1feature'] = get_lay1(path = f_path, f_cursor = tu.cursor)[0]
                num_file_dict[file]['lay2feature'] = get_lay1(path = f_path, f_cursor = tu.cursor)[1]
                num_file_dict[file]['lay3feature'] = get_lay1(path = f_path, f_cursor = tu.cursor)[2]
                num_file_dict[file]['lay4feature'] = get_lay1(path = f_path, f_cursor = tu.cursor)[3]
                num_file_dict[file]['lay5feature'] = get_lay1(path = f_path, f_cursor = tu.cursor)[4]
                num_file_dict[file]['lay6feature'] = get_lay6(path = f_path)





        #test for num_user
        i += 1
        if i > num_user:
            break

    num_file_all_dict = {i:{} for i in num_file_dict}
    for file in num_file_dict:
        num_file_all_dict[file] = num_file_dict[file]
        for other_file in num_file_dict:
            if other_file != file:
                for item in num_file_dict[other_file]:
                    if item not in num_file_dict[file]:
                        num_file_all_dict[file][item] = 0

    for file in num_file_all_dict:
        file_sample = file
        item_len = num_file_all_dict[file_sample]
        break

    trans_dict = {}
    i = 0
    for old_feature in num_file_all_dict[file_sample]:
        if (old_feature != 'class'):
            new_feature_name = "feature" + str(i)
            trans_dict[old_feature] = new_feature_name
            i += 1
    trans_dict['class'] = 'class'
    out_dict = {i:{} for i in num_file_all_dict}

    for file in out_dict:
        for old_feature in num_file_all_dict[file]:
            new_feature = trans_dict[old_feature]
            out_dict[file][new_feature] = num_file_all_dict[file][old_feature]
    
    return out_dict




if __name__ == '__main__':
    b = syntactic_2_extractor_nb(num_user=50)
    b_frame = pd.DataFrame.from_dict(b,orient='index')
    b_frame.to_csv('/Users/weiguo/Desktop/Replication/de-anonymizing/data/bigram_50.csv')
    
    