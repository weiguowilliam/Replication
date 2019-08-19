import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

import math

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_cppKeywords(file_cursor):
    #keyword list:
    key_dic = {"alignas",	"alignof",	"and"	,"and_eq"	,"asm",	"auto",	"bitand"	,"bitor",	"bool",	"break"	,"case",
"catch",	"char"	,"char16_t",	"char32_t",	"class",	"compl"	,"const"	,"constexpr"	,"const_cast"	,"continue",	"decltype",
"default",	"delete",	"do",	"double"	,"dynamic_cast",	"else",	"enum",	"explicit"	,"export"	,"extern"	,"false",
"float"	,"for",	"friend",	"goto",	"if",	"inline",	"int"	,"long"	,"mutable"	,"namespace"	,"new"	,"noexcept",	"not",
"not_eq"	,"nullptr",	"operator",	"or",	"or_eq",	"private"	,"protected"	,"public"	,"register",	"reinterpret_cast",
"return",	"short",	"signed"	,"sizeof"	,"static"	,"static_assert",	"static_cast"	,"struct",	"switch",	"template",
"this",	"thread_local",	"throw"	,"true",	"try"	,"typedef"	,"typeid"	,"typename",	"union",	"unsigned",	"using"	,"virtual",
"void",	"volatile",	"wchar_t"	,"while"	,"xor"	,"xor_eq"}

    output_dic= {}
    for token in file_cursor.get_tokens():
        str_token = token.spelling
        feature_name = "cppKeywords" + str_token
        if str_token in key_dic:
            if feature_name not in output_dic:
                output_dic[feature_name] = 1
            else:
                output_dic[feature_name] += 1

    for token in key_dic:
        str_token = "cppKeywords" + token
        if str_token not in output_dic:
            output_dic[str_token] = 0

    tf_d = {i:0 for i in output_dic}
    sum_node = 0
    for i in output_dic:
        sum_node += output_dic[i]
    for i in tf_d:
        try:
            tf_d[i] = float(output_dic[i])/sum_node
        except:
            print file_cursor.spelling
    return tf_d
    

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    print get_cppKeywords(tu.cursor)
    print len(get_cppKeywords(tu.cursor))
