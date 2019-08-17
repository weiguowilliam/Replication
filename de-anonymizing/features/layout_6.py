def get_lay6(path):
    input_file = open(path,'r')
    file_contents = input_file.read()
    
    preceeder = "a"
    count_tab = 0
    count_space = 0
    for f in file_contents:
        if preceeder == '\n':
            if f == '\t':
                count_tab += 1
            if f == ' ':
                count_space += 1
        preceeder = f
    
    if count_tab >= count_space:
        return 1
    else:
        return 0
    
if __name__ == '__main__':
    print get_lay6('test1.cpp')

