#include<string>
using namespace std;

int gcd(int a,int b){
    if(b==0)return a;
    return gcd(b,a%b);
}

bool simplify(string x,string n){
    int numer1 = stoi(split(x)[0]);
    int denom1 = stoi(split(x)[2]);

    int numer2 = stoi(split(n)[0]);
    int denom2 = stoi(split(n)[2]);

    if(denom1*denom2 == 0) return false;

    int greatest = gcd(gcd(numer1,denom1),gcd(numer2,denom2));

    return (numer1/denom1)*(denom2/greatest) == (numer2/greatest);
}

string split(string s){
    size_t found=s.find("/");
    return s.substr(0(found));
}