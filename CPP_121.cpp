```cpp
int sumOdd(int x) {
    int sum = 0;
    for (int i = 1; i <= 10; ) { 
        int y;
        std::cin >> y;
        if (y % 2 != 0) {
            sum += y;
        }
        ++i;
    }
    return sum;
}

int main() {
    std::cout << sumOdd(0) << std::endl;
}