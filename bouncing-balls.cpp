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

    for (int i = 1; i <= numberOfBounces; ++i) {
        totalDistance += 2 * currentHeight;
        currentHeight *= bouncinessIndex;
    }

    // Subtract the extra currentHeight added in the loop
    totalDistance -= currentHeight; 

    printf("%.14f\n", totalDistance);
    return 0;
}