#include <string>
#include <sstream>

using namespace std;

bool simplify(string x, string n) {
    int numerator1 = 0, denominator1 = 0;
    int numerator2 = 0, denominator2 = 0;

    // Extract numerator and denominator from both fractions
    size_t pos = x.find('/');
    numerator1 = stoi(x.substr(0, pos));
    denominator1 = stoi(x.substr(pos + 1));

    pos = n.find('/');
    numerator2 = stoi(n.substr(0, pos));
    denominator2 = stoi(n.substr(pos + 1));

    // Calculate the least common multiple of both denominators
    int lcm = (denominator1 * denominator2) / __gcd(denominator1, denominator2);

    // Calculate the new numerators and denominators
    int numerator3 = numerator1 * (lcm / denominator1);
    int denominator3 = lcm;

    int numerator4 = numerator2 * (lcm / denominator2);
    int denominator4 = lcm;

    // Check if both fractions are equal
    return numerator3 == numerator4;
}

// Function to calculate the greatest common divisor of two numbers
int __gcd(int a, int b) {
    if (b == 0)
        return a;
    else
        return __gcd(b, a % b);
}