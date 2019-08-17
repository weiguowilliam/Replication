import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind
import math

Config.set_library_file("/usr/local/Cellar/llvm/8.0.0_1/lib/libclang.dylib")

