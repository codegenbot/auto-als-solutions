```cpp
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

bool simplify(string x, string n) {
    int a = 0, b = 1, c = 0, d = 1;
    stringstream s(x);
    s >> a >> b;
    s.clear();
    s.str(n);
    s >> c >> d;
    if (b*d == a*c && __gcd(b,d) != 1)
        return true;
    else
        return false;
}