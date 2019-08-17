import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import math
import numpy as np
Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

def get_l14(fname):
    line_length_list = []
    with open(fname) as f:
        for i, l in enumerate(f):
            line_length_list.append(len(l))
    line_count = i+1
    avgLineLength = np.mean(line_length_list)
    stdLineLength = np.std(line_length_list)
    return avgLineLength, stdLineLength


if __name__ == '__main__':
    index = clang.cindex.Index.create()
    # tu = index.parse('test1.cpp')
    # tu = index.parse('test2.cpp')
    get_l14('test2.cpp')