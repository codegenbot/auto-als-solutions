#include <iostream>
#include <cmath>
#include <iosstream>

using namespace std;

int main() {
    double startHeight, firstBounce;
    int numBounces;

    cin >> startHeight >> firstBounce >> numBounces;

    double bounciness = firstBounce / startHeight;

    double totalDistance = 0.0;
    double currHeight = firstBounce;  
    for (int i = 1; i <= numBounces; i++) {
        totalDistance += currHeight;
        currHeight *= pow(2, -bounciness);
    }

    cout << fixed << setprecision(5) << totalDistance + startHeight;

    return 0;
}