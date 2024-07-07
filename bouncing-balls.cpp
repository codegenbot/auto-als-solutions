#include <iostream>
using namespace std;

int main() {
    double startingHeight;
    double firstBounceHeight;
    int numBounces;

    cin >> startingHeight >> firstBounceHeight >> numBounces;

    double bouncinessIndex = firstBounceHeight / startingHeight;

    double totalDistance = (1 + bouncinessIndex) * (1 - pow(bouncinessIndex, numBounces)) / (1 - bouncinessIndex);

    cout.precision(4);
    cout << fixed << totalDistance << endl;

    return 0;
}