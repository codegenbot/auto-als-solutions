#include<stdio.h>
#include<string>
using namespace std;

string encode_cyclic(string s){ 
    int l=s.length();
    int num=(l+2)/3;
    string x,output;
    int i;
    for (i=0;i*3<l;i++)
    {
        x=s.substr(i*3,3);
        if (x.length()==3) x=x.substr(1)+x[0];
        output=output+x;
    }
    return output;
}

string decode_cyclic(string s){ 
    int l=s.length();
    string output,t;
    for (int i=0;i+l/3;i++)
    {
        t="";
        for(int j=0;j<3&&i*3+j<l;j++){
            t+=s[i*3+j];
        }
        if(t.length()>1)output+=t[1]+t[0];
        else output+=t;
    }
    return output;
}