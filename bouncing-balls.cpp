int main() {
    double startHeight, firstBounce;
    int numBounces;

    cin >> startHeight >> firstBounce >> numBounces;

    double bounciness = firstBounce / startHeight;

    double totalDistance = 0.0;
    double currentHeight = firstBounce; 
    for (int i = 1; i <= numBounces; i++) {
        if(i == 1) continue; // skip the first bounce
        totalDistance += pow(2, -bounciness) * (startHeight + (firstBounce - startHeight)*pow(2, -(i-1)*bounciness)); 
    }

    cout << fixed << setprecision(5) << totalDistance;

    return 0;
}