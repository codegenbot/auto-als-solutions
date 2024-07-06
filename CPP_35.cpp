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

int main(){
    int n;
    std::cin >> n;
    std::vector<float> v(n);
    for(float &x : v) {
        std::cin >> x;
    }
    std::cout << max_element(v) << std::endl;
    return 0;
}