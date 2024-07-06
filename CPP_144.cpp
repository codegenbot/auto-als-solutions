#include<string>
using namespace std;

bool simplify(string x, string n) {
    int numerator1 = 0, denominator1 = 0, numerator2 = 0, denominator2 = 0;
    stringstream ss(x);
    ss >> numerator1 >> '/' >> denominator1;
    stringstream s(n);
    s >> numerator2 >> '/' >> denominator2;

    if (denominator1 != denominator2) {
        return false;
    }

    int commonDivisor = gcd(denominator1, numerator1);
    int newNumerator1 = numerator1 / commonDivisor;
    int newDenominator1 = denominator1 / commonDivisor;

    if ((long long)newNumerator1 * (long long)denominator2 == (long long)numerator2 * (long long)newDenominator1)
        return true;
    else
        return false;
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}