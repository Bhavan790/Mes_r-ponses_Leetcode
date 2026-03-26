int res(int x)
{
    int a=0,b;
    while(x!=0)
    {
        b=x%10;
        a=(b*b)+a;
        x=x/10;
    }
    return a;
}
bool isHappy(int n) 
{
    int r=n;
    while(1)
    {
        r=res(r);
        if(r==1)
            return true;
        else if( r<1 || r==89)
            return false;
    }
}