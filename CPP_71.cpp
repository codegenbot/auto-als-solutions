#include <cmath>

using namespace std;

float triangle_area(float a, float b, float c) {
    if (a + b > c && a + c > b && b + c > a) {
        return (a * b * c) ? sqrt(float(a)*float(b)*float(c)/4.0) : -1.0f;
    } else {
        return -1.0f;
    }
}