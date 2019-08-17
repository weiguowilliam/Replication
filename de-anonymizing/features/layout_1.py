import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import math
import numpy as np
Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_lay1(path,f_cursor):
    input_file = open(path,'r')
    file_contents = input_file.read()
    count_tab = 0
    for f in file_contents:
        if f == '\t':
            count_tab += 1

    count_space = 0
    for s in file_contents:
        if s == ' ':
            count_space += 1
    
    count_EmptyLine = 0
    fileHandler = open (path, "r")
    listOfLines = fileHandler.readlines()
    for i in listOfLines:
        if len(i.strip()) == 0:
            count_EmptyLine += 1

    length_included = 0
    for c in file_contents:
        length_included += 1
#layout 5
    Brace_num = 0
    BraceNew = 0
    preceeder = " "
    for c in file_contents:
        if (c == '{'):
            Brace_num += 1
            if (preceeder == "\n"):
                BraceNew += 1
        preceeder = c
    Brace_e = Brace_num - BraceNew
    if  BraceNew >= Brace_e:
        Brace = 1
    else:
        Brace = 0

    def get_file_length(cur):
        cursor_content=""
        for token in cur.get_tokens():
            str_token = token.spelling
            cursor_content = cursor_content+str_token
        return len(cursor_content)

    file_length = get_file_length(f_cursor)

    def get_return(c):
        if c == 0:
            return 0
        else:
            return math.log(float(c)/file_length)

    length_empty = count_EmptyLine + count_space + count_tab
    length_nempty = length_included - length_empty
    whiteSpaceRatio = float(length_empty)/length_nempty
    
    lnTab = get_return(count_tab)
    lnSpace = get_return(count_space)
    lnEmpytLine = get_return(count_EmptyLine)
    
    return lnTab, lnSpace, lnEmpytLine, whiteSpaceRatio, Brace

if __name__ == '__main__':
    index = clang.cindex.Index.create()
    tu = index.parse('test1.cpp')
    get_lay1('test1.cpp',tu.cursor)