import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_bigram(cursor, BigramDic = {}, level = 0):
    """
    Bigram can only be made by a parent node ant its children node. Use BigramDic to store the bigram pair.
    When the node is not a part of real code, use its cursor kind to construct the bigram.
    """

    # def spell(cursor):
    #     if cursor.spelling.strip():
    #         return cursor.spelling,0
    #     else:
    #         return str(cursor.kind).split('.')[-1],1
    def spell(cursor):
        if cursor.spelling.strip():
            return cursor.spelling,0
        else:
            return cursor.kind,1

    for c in cursor.get_children():
        if level != 0:
            # parent_spelling = spell(cursor)[0]
            # child_spelling = spell(c)[0]
            parent_spelling = spell(cursor)[0]
            child_spelling = spell(c)[0]
            parent_isKind = spell(cursor)[1]

            if (parent_spelling == child_spelling)&(parent_isKind == 0):# in case of (UNEXPOSED_EXPR,DECL_REF_EXPR)->(a,a)
                pass
            else:

                name = str(parent_spelling)+str(child_spelling)
                if name not in BigramDic:
                # if (parent_spelling, child_spelling) not in BigramDic:
                    # name = str(parent_spelling)+str(child_spelling)
                    # BigramDic[(parent_spelling, child_spelling)] = 1
                    BigramDic[name] = 1
                else:
                    # BigramDic[(parent_spelling, child_spelling)] += 1
                    BigramDic[name] += 1    
            
        get_bigram(c, BigramDic, level + 1)
                


# index = clang.cindex.Index.create()
# tu = index.parse('test4.cpp')
# print 'Translation unit:', tu.spelling
# print tu.cursor.kind
# bd = {}
# get_bigram(tu.cursor, BigramDic= bd)
# print len(bd)
# print bd
    
if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test4.cpp')
    print 'Translation unit:', tu.spelling
    print tu.cursor.kind
    bd = {}
    get_bigram(tu.cursor, BigramDic= bd)
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

