#include <iostream>
using namespace std;

double calculateTotalDistance(double initialHeight, double firstBounceHeight, int numberOfBounces) {
    double bouncinessIndex = firstBounceHeight / initialHeight;
    double totalDistance = 0.0;

    for (int i = 1; i <= numberOfBounces; i++) {
        totalDistance += (2 * bouncinessIndex - 1) * pow(2, -i);
    }

    return totalDistance;
}

int main() {
    double initialHeight, firstBounceHeight;
    int numberOfBounces;

    cin >> initialHeight >> firstBounceHeight >> numberOfBounces;

    cout << fixed << setprecision(5) << calculateTotalDistance(initialHeight, firstBounceHeight, numberOfBounces);

    return 0;
}