#include <vector>
#include <iostream>

int max_element(std::vector<float> l){
    float max = l[0];
    for(int i=1; i<l.size(); i++){
        if(l[i] > max)
            max = l[i];
    }
    return static_cast<int>(max);
}

int main() {
    int n;
    std::cin >> n;
    std::vector<float> l(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> l[i];
    }
    std::cout << max_element(l) << std::endl;
    return 0;
}