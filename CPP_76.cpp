#include <cmath>

using namespace std;

bool is_simple_power(int x, int n) {
    double y = pow(n, log(x) / log(n));
    return (y == static_cast<int>(y));
}