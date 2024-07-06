#include <string>
#include <vector>

using namespace std;

bool simplify(string x, string n) {
    int a = 0, b = 1;
    int c = 0, d = 1;
    
    // Convert fractions to integers
    for (int i = 0; i < x.size(); ++i) {
        if (x[i] == '/') break;
        if (isdigit(x[i])) a = a * 10 + (x[i] - '0');
    }
    for (int i = 0; i < n.size(); ++i) {
        if (n[i] == '/') break;
        if (isdigit(n[i])) c = c * 10 + (n[i] - '0');
    }
    
    // Calculate the greatest common divisor
    int gcd = a;
    while (c != 0) {
        int temp = c;
        c = c % gcd;
        a = gcd;
        gcd = temp;
    }
    
    // Check if the result is an integer
    int res = a / d;
    return res == c / d;
}