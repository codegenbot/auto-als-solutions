```
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
        totalDistance += pow(2, -bounciness) * currentHeight; 
        currentHeight *= (pow(2, -bounciness)); 
    }

    cout << fixed << setprecision(5) << totalDistance + firstBounce;

    return 0;
}