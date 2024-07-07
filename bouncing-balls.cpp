#include <iostream>
using namespace std;

int main() {
    double startHeight, firstBounceHeight;
    int numBounces;

    cin >> startHeight >> firstBounceHeight >> numBounces;

    // Calculate bounciness index (height of first bounce / starting height)
    double bouncinessIndex = firstBounceHeight / startHeight;

    // Calculate total distance traveled
    double totalDistance = 0.0;
    for(int i = 1; i <= numBounces; ++i) {
        totalDistance += pow(2, -1) * (pow(bouncinessIndex, i));
    }

    cout << fixed << setprecision(4);
    cout << startHeight << endl;
    cout << firstBounceHeight << endl;
    cout << totalDistance << endl;

    return 0;
}