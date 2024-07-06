```cpp
#include <iostream>
using namespace std;

bool right_angle_triangle(float a, float b, float c) {
    if (a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a)
        return true;
    else
        return false;
}

int main() {
    float side1, side2, side3;
    cout << "Enter the sides of triangle: ";
    cin >> side1 >> side2 >> side3;
    
    if (side1 + side2 > side3 && right_angle_triangle(side1, side2, side3)) 
        cout << "This is a valid Right Angle Triangle." << endl;
    else
        cout << "This is not a valid Right Angle Triangle." << endl;

    return 0;
}