int lengthOfLastWord(char* s) 
{
    int a=strlen(s);
    int b=0,c=0;
    for(int i=0;i<a;i++)
    {
        if(s[i]==' ' || s[i]==a-1)
            b=0;
        else
        {
            b++;
            c=b;
        }
    }
    return c;    
}