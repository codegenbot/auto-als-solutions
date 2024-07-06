#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;

float triangle_area(float a, float b, float c) {
    if ((a + b > c) && (a + c > b) && (b + c > a)) {
        float s = (a + b + c) / 2.0;
        return round((sqrt(s*(s-a)*(s-b)*(s-c))) * 100.0) / 100.0;
    } else {
        return -1.0;
    }
}

int main() {
    float a, b, c;
    cout << "Enter the sides of the triangle: ";
    cin >> a >> b >> c;
    float area = triangle_area(a, b, c);
    if (area == -1.0)
        cout << "Not a valid triangle";
    else
        cout << "The area of the triangle is: " << area;
    return 0;
}