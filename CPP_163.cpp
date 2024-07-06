```cpp
#include <vector>
#include <algorithm>

std::vector<int> generate_integers(int a, int b) {
    std::vector<int> result;
    for (int i = std::min(a, b); i <= std::max(a, b); i++) {
        if (i % 2 == 0) {
            result.push_back(i);
        }
    }
    return result;
}

bool issame(const std::vector<int>& a,const std::vector<int>&b){
    return (a==b);
}

int main() {
    int a, b;
    std::cout << "Enter two integers: ";
    std::cin >> a >> b;
    if(issame(generate_integers(a, b), generate_integers(17, 89))){
        std::cout << "The vectors are the same.\n";
    }else{
        std::cout << "The vectors are not the same.\n";
    }
    return 0;
}