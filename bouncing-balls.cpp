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
    double currentHeight = firstBounce; 
    for (int i = 1; i <= numBounces; i++) {
        totalDistance += currentHeight; 
        currentHeight /= 2; 
    }

    cout << fixed << setprecision(5) << totalDistance + startHeight;

    return 0;
}