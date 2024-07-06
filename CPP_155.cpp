#include <iostream>
#include <vector>

// Function declaration for issame
bool issame(std::vector<int> a, std::vector<int> b);

std::vector<int> even_odd_count(int num) {
    vector<int> result(2, 0);
    while (num != 0) {
        int digit = num % 10;
        if (digit % 2 == 0)
            result[0]++;
        else
            result[1]++;
        num /= 10;
    }
    return result;
}

// Define the issame function
bool issame(std::vector<int> a, std::vector<int> b) {
    return (a == b);
}