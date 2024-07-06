#include <iostream>
#include <vector>

float max_element(std::vector<float> l){
    float max = l[0];
    for(int i=1; i<l.size(); i++){
        if(l[i] > max)
            max = l[i];
    }
    return max;
}

int main() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    std::vector<float> v(n);
    for (int i = 0; i < n; ++i) {
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> v[i];
    }

    float max = max_element(v);

    std::cout << "Maximum element is: " << max << std::endl;
    return 0;
}