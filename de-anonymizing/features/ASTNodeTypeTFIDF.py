
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

# def get_DocumentFrequency(dic_path):

#     node_tf_dict_tem = {}
#     for r,d,f in os.walk(path):
#         for file in f:
#             if str(file) != '.DS_Store':
#                 node_tf_dict_tem[file] = {}
#                 f_path = os.path.join(r, file)
#                 index = clang.cindex.Index.create()
#                 tu = index.parse(f_path)
#                 node_tf_dict_tem[file] = get_ASTNodeTypeTF(tu.cursor)
    
#     all_file_length = len(node_tf_dict_tem)

#     node_tf_dict = {}
#     for files in node_tf_dict_tem:
#         for feature in node_tf_dict_tem[files]:
#             if feature not in node_tf_dict:
#                 node_tf_dict[feature] = 1
#             else:
#                 node_tf_dict[feature] += 1
    