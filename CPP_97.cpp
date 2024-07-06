int multiply(int a, int b) {
    int unitsA = a % 10;
    int tensA = (a / 10) % 10;
    int unitsB = b % 10;
    int tensB = (b / 10) % 10;

    return (unitsA * unitsB) + ((tensA * unitsB) + (tensA * tensB) * 10);
}