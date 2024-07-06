#include <cmath>
#include <cstdlib>

float triangle_area(float a, float b, float c) {
    if (a + b > c && a + c > b && b + c > a)
        return std::round(std::sqrt((a * (b * b) + (c * c) - (b * 2 * c)) / 4.0)) / 100.0;
    else
        return -1.0;
}