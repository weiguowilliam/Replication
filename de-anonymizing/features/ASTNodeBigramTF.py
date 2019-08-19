import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_bigram(file_cursor):
    # def spell(cursor):
    #     if cursor.spelling.strip():
    #         return cursor.spelling,0
    #     else:
    #         return cursor.kind,1
    def spell(cursor):
        if cursor.spelling.strip():
            return cursor.kind, cursor.spelling
        else:
            return cursor.kind,"BLANK"

    def get_bi_inside(cursor, BigramDic = {}, level = 0):
        """
        Bigram can only be made by a parent node ant its children node. Use BigramDic to store the bigram pair.
        When the node is not a part of real code, use its cursor kind to construct the bigram.
        """

        for c in cursor.get_children():
            if level != 0:
                parent_kind, parent_code = spell(cursor)
                child_kind, child_code = spell(c)
                
                if (parent_kind == CursorKind.UNEXPOSED_EXPR) and (child_kind == CursorKind.DECL_REF_EXPR):# in case of (UNEXPOSED_EXPR,DECL_REF_EXPR)->(a,a)
                    pass
                else:
                    name = "Bigram" + str(parent_kind) + str(child_kind) + str(parent_code) + str(child_code)
                    if name not in BigramDic:
                        BigramDic[name] = 1
                    else:
                        BigramDic[name] += 1    
                    
            get_bi_inside(c, BigramDic, level + 1)

    # def get_bi_inside(cursor, BigramDic = {}, level = 0):
    #     """
    #     Bigram can only be made by a parent node ant its children node. Use BigramDic to store the bigram pair.
    #     When the node is not a part of real code, use its cursor kind to construct the bigram.
    #     """

    #     for c in cursor.get_children():
    #         if level != 0:
    #             parent_spelling = spell(cursor)[0]
    #             child_spelling = spell(c)[0]
    #             parent_isKind = spell(cursor)[1]

    #             if (parent_spelling == child_spelling)&(parent_isKind == 0):# in case of (UNEXPOSED_EXPR,DECL_REF_EXPR)->(a,a)
    #                 pass
    #             else:

    #                 name = "Bigram" + str(parent_spelling)+str(child_spelling)
    #                 if name not in BigramDic:
    #                     BigramDic[name] = 1
    #                 else:
    #                     BigramDic[name] += 1    
                
    #         get_bi_inside(c, BigramDic, level + 1)

    def get_bi_tf(rd = {}):
        tf_d = {i:0 for i in rd}
        sum_node = 0
        for i in rd:
            sum_node += rd[i]
        for i in tf_d:
            tf_d[i] = float(rd[i])/sum_node
        return tf_d

    def trans(d,s):
        d_out = {}
        i = 0
        for raw_feature in d:
            new_feature = str(s) + str(i)
            d_out[new_feature] = d[raw_feature]
            i += 1
        return d_out

    bd_tem = {}
    get_bi_inside(cursor = file_cursor, BigramDic=bd_tem, level = 0)
    bd_out = get_bi_tf(rd = bd_tem)
    # bd_trans = trans(bd_out,"bigram")
    return bd_out




if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    a = get_bigram(tu.cursor)
    print len(a)
    print a 
    


################ This is a homemade ast tree for test ####################
    # def spelll(cursor):
    #     return "( "+str(cursor.spelling) + " , "+str(cursor.kind)

    # for c in tu.cursor.get_children():
    #     print spelll(c)
    #     for a in c.get_children():
    #         print "  ",spelll(a)
    #         for b in a.get_children():
    #             print "    ",spelll(b)
    #             for d in b.get_children():
    #                 print "      ",spelll(d)
    #                 for e in d.get_children():
    #                     print " "*8,spelll(e)
    #                     for f in e.get_children():
    #                         print " "*10,spelll(f)
    #                         for g in f.get_children():
    #                             print " "*12,spelll(g)
    #                             for h in g.get_children():
    #                                print " "*14,spelll(h)
#############################################################################

