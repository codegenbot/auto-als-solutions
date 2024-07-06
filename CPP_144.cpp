#include <sstream>
using namespace std;

bool simplify(string x, string n) {
    int a = 0, b = 1, c = 0, d = 1;
    istringstream iss1(x), iss2(n);
    iss1 >> a >> b;
    iss2 >> c >> d;
    
    long gcd = abs(a*d - c*b);
    long lcm = abs(a*d)/gcd * ((a>0)?1:-1) * ((d>0)?1:-1);

    return (lcm/b == a && lcm%d == c);
}