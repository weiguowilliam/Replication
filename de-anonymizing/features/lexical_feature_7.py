import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import math

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")



def get_l7(cursor):
    key_dic = {"alignas",	"alignof",	"and"	,"and_eq"	,"asm",	"auto",	"bitand"	,"bitor",	"bool",	"break"	,"case",
"catch",	"char"	,"char16_t",	"char32_t",	"class",	"compl"	,"const"	,"constexpr"	,"const_cast"	,"continue",	"decltype",
"default",	"delete",	"do",	"double"	,"dynamic_cast",	"else",	"enum",	"explicit"	,"export"	,"extern"	,"false",
"float"	,"for",	"friend",	"goto",	"if",	"inline",	"int"	,"long"	,"mutable"	,"namespace"	,"new"	,"noexcept",	"not",
"not_eq"	,"nullptr",	"operator",	"or",	"or_eq",	"private"	,"protected"	,"public"	,"register",	"reinterpret_cast",
"return",	"short",	"signed"	,"sizeof"	,"static"	,"static_assert",	"static_cast"	,"struct",	"switch",	"template",
"this",	"thread_local",	"throw"	,"true",	"try"	,"typedef"	,"typeid"	,"typename",	"union",	"unsigned",	"using"	,"virtual",
"void",	"volatile",	"wchar_t"	,"while"	,"xor"	,"xor_eq"}

    unique_dic= {}
    for token in cursor.get_tokens():
        str_token = token.spelling
        
        if str_token in key_dic:
            if str_token not in unique_dic:
                unique_dic[str_token] = 1

    
    unique_len = len(unique_dic)

    def get_file_length(cur):
        cursor_content=""
        for token in cur.get_tokens():
            str_token = token.spelling
            cursor_content = cursor_content+str_token
        return len(cursor_content)

    file_len = get_file_length(cursor)

    if unique_len == 0:
        return 0
    else:
        return math.log(float(unique_len)/file_len)

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test2.cpp')
    print get_l7(tu.cursor)
