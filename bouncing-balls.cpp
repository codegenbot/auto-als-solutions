#include <iostream>
#include <iomanip>

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

    std::cout << std::fixed << std::setprecision(15) << totalDistance << std::endl;
    return 0;
}