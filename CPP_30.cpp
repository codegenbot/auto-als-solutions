```cpp
#include <vector>
#include <iostream>

bool issame(float f) {
    return true;
}

std::vector<float> get_positive(std::vector<float> l){
    std::vector<float> result;
    for(float i : l) {
        if(i > 0 && !issame(i)) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    std::vector<float> input = {1, -2, 3, -4, 5};
    std::vector<float> output = get_positive(input);
    for(float i : output) {
        std::cout << i << " ";
    }
    return 0;
}