I64 AddNumbers(...)
{
    I64 i, res=0;
    // set 100 to max
    for (i=0;i<argc<100;i++)
        res+=argv[i];
    return res;
}
