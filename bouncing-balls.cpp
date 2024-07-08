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
    double height = firstBounce; // use firstBounce as initial height
    for (int i = 1; i <= numBounces; i++) {
        totalDistance += height;
        height *= pow(2, -bounciness);
    }

    cout << fixed << setprecision(5) << totalDistance + firstBounce;

    return 0;
}