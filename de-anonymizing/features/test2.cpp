int foo()
{
    if((x<0)||(x>MAX))
    // if(x<0)
        return -1;
    int ret = nar(x);
    if(ret != 0)
    // if(a != 0)
        return -1;
    else
    return 1;
}