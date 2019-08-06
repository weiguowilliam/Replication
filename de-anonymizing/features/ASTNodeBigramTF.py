"""
Todo: correct: (parent node, parent node),(child node, child node) will appear in bigram, which is wrong.

"""


import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

# def get_ast(cursor, BigramDic = {}, level = 0):
#     """
#     Bigram can only be made by a parent node ant its children node. Use BigramDic to store the bigram pair.
#     """
#     for c in cursor.get_children():
#         if level == 0:
#             get_ast(c, BigramDic, level+1)
#         else:
#             parent_spelling = c.spelling
#             for token in c.get_tokens():

def get_ast(cursor, BigramDic = {}, level = 0):
    """
    Bigram can only be made by a parent node ant its children node. Use BigramDic to store the bigram pair.
    When the node is not a part of real code, use its cursor kind to construct the bigram.
    """

    def spell(cursor):
        if cursor.spelling.strip():
            return cursor.spelling,0
        else:
            return cursor.kind,1

    for c in cursor.get_children():
        if level != 0:
            parent_spelling = spell(cursor)[0]
            parent_isKind = spell(cursor)[1]
            child_spelling = spell(c)[0]
            
            # print "(", parent_spelling,",",child_spelling,")"

            if (parent_spelling == child_spelling)&(parent_isKind == 0):# in case of (UNEXPOSED_EXPR,DECL_REF_EXPR)->(a,a)
                # print "    (", parent_spelling,",",child_spelling,")"
                pass
            else:
                if (parent_spelling, child_spelling) not in BigramDic:
                    BigramDic[(parent_spelling, child_spelling)] = 1
                else:
                    BigramDic[(parent_spelling, child_spelling)] += 1


            # if (parent_spelling != child_spelling)&(parent_isKind == 0): 
            #     if (parent_spelling, child_spelling) not in BigramDic:
            #         BigramDic[(parent_spelling, child_spelling)] = 1
            #     else:
            #         BigramDic[(parent_spelling, child_spelling)] += 1
            # else:
            #     print "    (", parent_spelling,",",child_spelling,")"
            
        get_ast(c, BigramDic, level + 1)
                
# def spell(cursor):
# #     # if cursor.spelling.strip():
# #     #     return cursor.spelling
# #     # else:
# #     #     return cursor.kind
# #     # return cursor.kind
# #     # return cursor.spelling
#     return str(" kind "+str(cursor.kind)+" spelling "+str(cursor.spelling))


if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    tu = index.parse('test2.cpp')
    print 'Translation unit:', tu.spelling
    print tu.cursor.kind
    bd = {}
    get_ast(tu.cursor, BigramDic= bd)
    print len(bd)
    print bd
    

    # for c in tu.cursor.get_children():
    #     print c.spelling
    #     print type(c.spelling)
    #     print c.kind
        
    #     if c.spelling.strip():
    #         print "T"
    #     else:
    #         print "F"
    #     print "xxxxxxxxxxxxxxxxxxx"

    # for c in tu.cursor.get_children():
    #     print "*",c.spelling,"*"
    #     print c.kind
    #     for a in c.get_children():
    #         print "*",a.spelling,"*"
    #         print a.kind
    #         print "(",spell(c),",",spell(a),")"
    #     print "XXXXXXXXX"

    # for c in tu.cursor.get_children():
    #     # print "*",c.spelling,"*"
    #     # print c.kind
    #     for a in c.get_children():
    #         # print "*",a.spelling,"*"
    #         # print a.kind
    #         print "(",spell(c),",",spell(a),")"
    #         for b in a.get_children():
    #             # print "*",b.spelling,"*"
    #             # print b.kind
    #             print "  (",spell(a),",",spell(b),")"
    #             for d in b.get_children():
    #                 print "    (",spell(b),",",spell(d),")"
    #                 for e in d.get_children():
    #                     print "      (",spell(d),",",spell(e),")"
            
    #     print "xxxxxxxxxxxxxx"


################ This is a homemade ast tree for test ####################
    # for c in tu.cursor.get_children():
    #     print spell(c)
    #     for a in c.get_children():
    #         print "  ",spell(a)
    #         for b in a.get_children():
    #             print "    ",spell(b)
    #             for d in b.get_children():
    #                 print "      ",spell(d)
    #                 for e in d.get_children():
    #                     print " "*8,spell(e)
    #                     for f in e.get_children():
    #                         print " "*10,spell(f)
    #                         for g in f.get_children():
    #                             print " "*12,spell(g)
    #                             for h in g.get_children():
    #                                print " "*14,spell(h)
#############################################################################

