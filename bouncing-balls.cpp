#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    double startHeight, firstBounce;
    int numBounces;

    cin >> startHeight >> firstBounce >> numBounces;

    double bounciness = firstBounce / startHeight;

    double totalDistance = 0.0;
    double currentHeight = startHeight; 
    for (int i = 1; i <= numBounces; i++) {
        totalDistance += currentHeight * (1 - pow(2, -bounciness));
        currentHeight *= (pow(2, -bounciness)); 
    }

    cout << fixed << std::setprecision(10) << totalDistance + firstBounce;

    return 0;
}