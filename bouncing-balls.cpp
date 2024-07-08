```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    double startHeight, firstBounce;
    int numBounces;

    cin >> startHeight >> firstBounce >> numBounces;

    double bounciness = pow((firstBounce / startHeight), -0.5);
    totalDistance = 0.0;
    currentHeight = firstBounce; 
    for (int i = 1; i <= numBounces; i++) {
        totalDistance += currentHeight; 
        currentHeight *= pow((pow(2, -bounciness)), 2); 
    }

    cout << fixed << setprecision(5) << totalDistance + startHeight;

    return 0;
}