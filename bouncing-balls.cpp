#include <iostream>
using namespace std;

double calculateBouncinessIndex(double startHeight, double firstBounceHeight) {
    return firstBounceHeight / startHeight;
}

double calculateTotalDistance(int numBounces, double bouncinessIndex) {
    double totalDistance = 0.0;
    for (int i = 1; i <= numBounces; i++) {
        totalDistance += pow(bouncinessIndex, i);
    }
    return totalDistance;
}

int main() {
    double startHeight, firstBounceHeight;
    int numBounces;

    cout << "Enter the starting height: ";
    cin >> startHeight;
    cout << "Enter the height after the first bounce: ";
    cin >> firstBounceHeight;
    cout << "Enter the number of bounces: ";
    cin >> numBounces;

    double bouncinessIndex = calculateBouncinessIndex(startHeight, firstBounceHeight);
    double totalDistance = calculateTotalDistance(numBounces, bouncinessIndex);

    cout.precision(6);  // Set precision to 6 for floating-point output
    cout << fixed;
    cout << "The total distance traveled is: " << totalDistance << endl;

    return 0;
}