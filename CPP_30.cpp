#include <iostream>
#include <vector>

std::vector<float> get_positive(std::vector<float> l) {
    std::vector<float> result;
    for(float i : l) {
        if(i > 0) {
            result.push_back(i);
        }
    }
    return result;
}

bool issame(float a, float b) {
    return (a == b);
}

int main() {
    std::vector<float> numbers = {1.2f, -3.4f, 5.6f};
    std::vector<float> positive_numbers = get_positive(numbers);

    for(float i : positive_numbers) {
        if(issame(i, 0)) {
            continue;
        }
        std::cout << i << " ";
    }

    return 0;
}