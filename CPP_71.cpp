#include <cmath>

using namespace std;

float triangle_area(float a, float b, float c) {
    if (a + b > c && a + c > b && b + c > a)
        return 0.5 * sqrt((b - a) * (b - a) * (c - a) * (c - a));
    else
        return -1;
}