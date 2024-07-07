bool any_int(float a, float b, float c) {
    int ai = (int)a;
    int bi = (int)b;
    int ci = (int)c;

    return ((a == ai + bi + ci) || (b == ai + bi + ci) || (c == ai + bi + ci));
}

int main() {
    float a, b, c;
    std::cout << "Enter three floating point numbers: ";
    std::cin >> a >> b >> c;
    if(any_int(a, b, c)) {
        std::cout << "At least one of the input values is an integer." << std::endl;
    } else {
        std::cout << "None of the input values are integers." << std::endl;
    }
    return 0;
}