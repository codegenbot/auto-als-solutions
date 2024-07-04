#include <iostream>
#include <cstdio>

int main() {
    double startingHeight, firstBounceHeight;
    int numberOfBounces;
    
    std::cin >> startingHeight >> firstBounceHeight >> numberOfBounces;
    
    double bouncinessIndex = firstBounceHeight / startingHeight;
    double totalDistance = startingHeight + firstBounceHeight;
    double currentHeight = firstBounceHeight;
    
    for (int i = 1; i < numberOfBounces; ++i) {
        currentHeight *= bouncinessIndex;
        totalDistance += 2 * currentHeight;
    }
    
    printf("%.12f\n", totalDistance);
    return 0;
}