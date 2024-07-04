#include <iostream>
#include <cstdio>

int main() {
    double startingHeight, firstBounceHeight;
    int numberOfBounces;
    
    std::cin >> startingHeight >> firstBounceHeight >> numberOfBounces;
    
    double bouncinessIndex = firstBounceHeight / startingHeight;
    double totalDistance = startingHeight;
    double currentHeight = firstBounceHeight;
    
    for (int i = 1; i < numberOfBounces; ++i) {
        totalDistance += 2 * currentHeight;
        currentHeight *= bouncinessIndex;
    }
    
    totalDistance += currentHeight; // Add the last bounce

    printf("%.12f\n", totalDistance);
    return 0;
}