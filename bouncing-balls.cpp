```cpp
for (int i = 1; i <= numBounces; i++) {
    totalDistance += pow(2, -bounciness) * 2 * currentHeight; 
    currentHeight *= (pow(2, -bounciness)); 
}