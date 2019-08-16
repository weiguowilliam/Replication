import os
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import pandas as pd
import pickle
Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")
sys.path.append(os.path.abspath("/Users/weiguo/Desktop/Replication/de-anonymizing"))
from features.ASTNodeBigramTF import get_bigram
from features.MaxDepthASTNode import get_MaxDepthNode
from features.ASTNodeTypeTF import get_ASTNodeTypeTF
from features.ASTNodeTypeAvgDep import get_ASTNodeTypeAvgDepth
from cppKeywords import get_cppKeywords

def syntactic_2_extractor_nb(num_user = 2, num_file_per_author = 9):

    path = "/Users/weiguo/Desktop/traindata"
    i = 0
    num_file_dict = {}
    for r, d, f in os.walk(path):
        
        for file in f:
            if str(file) != '.DS_Store':
                num_file_dict[file] = {}
                f_path = os.path.join(r, file)
                index = clang.cindex.Index.create()
                tu = index.parse(f_path)

                #get bigram feature
                # get_bigram(tu.cursor, num_file_dict[file])
                bgd = get_bigram(tu.cursor)
                num_file_dict[file].update(bgd)
                
                
                #get max depth feature
                num_file_dict[file]['maxdepthnode'] = get_MaxDepthNode(tu.cursor)
                
                #get file class(author)
                file_class_tem = str(file)[0:-4]
                file_class = file_class_tem.split('_')[-1]
                num_file_dict[file]['class'] = file_class
                
                #get node type frequency:
                ntd = get_ASTNodeTypeTF(tu.cursor)
                num_file_dict[file].update(ntd)

                #get node type average depth
                avg_depth_dic = get_ASTNodeTypeAvgDepth(tu.cursor)
                num_file_dict[file].update(avg_depth_dic)

                #get cppKeywords frequency(syntactic)
                keywords_dic = get_cppKeywords(tu.cursor)
                num_file_dict[file].update(keywords_dic)


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
    b = syntactic_2_extractor_nb(num_user=3)
    b_frame = pd.DataFrame.from_dict(b,orient='index')
    b_frame.to_csv('/Users/weiguo/Desktop/Replication/de-anonymizing/data/bigram0814.csv')
    
    