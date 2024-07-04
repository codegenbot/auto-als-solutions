#include <iostream>
#include <cstdio>
#include <cmath>

int main() {
    double startingHeight, firstBounceHeight;
    int numberOfBounces;
    
    std::cin >> startingHeight >> firstBounceHeight >> numberOfBounces;
    
    double bouncinessIndex = firstBounceHeight / startingHeight;
    double totalDistance = startingHeight;
    double currentHeight = firstBounceHeight;
    
    for (int i = 1; i < numberOfBounces; ++i) {
        totalDistance += 2 * currentHeight;
        currentHeight = currentHeight * bouncinessIndex;
    }
    
    totalDistance += 2 * currentHeight;

    printf("%.12f\n", totalDistance);
    return 0;
}