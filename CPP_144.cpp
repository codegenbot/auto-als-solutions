#include<string>
using namespace std;

bool simplify(string x,string n){
    int numerator1 = 0, denominator1 = 0;
    int numerator2 = 0, denominator2 = 0;

    size_t pos1 = x.find('/');
    size_t pos2 = n.find('/');

    string num1 = x.substr(0, pos1);
    string den1 = x.substr(pos1 + 1);
    string num2 = n.substr(0, pos2);
    string den2 = n.substr(pos2 + 1);

    numerator1 = stoi(num1) * stoi(den2);
    denominator1 = stoi(den1) * stoi(num2);

    numerator2 = stoi(num1) * stoi(num2);
    denominator2 = stoi(den1) * stoi(den2);

    if (gcd(numerator1, denominator1) == 1)
        return true;
    else
        return false;

}

int gcd(int a, int b){
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}