#include <string>
#include <sstream>

using namespace std;

bool simplify(string x, string n) {
    int a = 0, b = 1, c = 0, d = 1;
    stringstream s(x);
    char temp;
    s >> a >> temp >> b;
    s.clear();
    s.str(n);
    s >> c >> temp >> d;
    if (b*d == a*c)
        return true;
    else
        return false;
}