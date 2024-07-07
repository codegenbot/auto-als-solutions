#include <iostream>
using namespace std;

double calculateTotalDistance(double startingHeight, double heightAfterFirstBounce, int numberOfBounces) {
    double bouncinessIndex = heightAfterFirstBounce / startingHeight;
    double totalDistance = 0.0;

    for(int i = 1; i <= numberOfBounces; ++i) {
        totalDistance += startingHeight * (1 + bouncinessIndex) * pow(1 - bouncinessIndex, i);
        startingHeight *= (1 + bouncinessIndex) * (1 - pow(bouncinessIndex, i));
    }

    return totalDistance;
}

int main() {
    double startingHeight = 0.0;
    double heightAfterFirstBounce = 0.0;
    int numberOfBounces = 0;

    cin >> startingHeight >> heightAfterFirstBounce >> numberOfBounces;

    cout << fixed << setprecision(6) << calculateTotalDistance(startingHeight, heightAfterFirstBounce, numberOfBounces) << endl;

    return 0;
}