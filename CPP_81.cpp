```cpp
#include <vector>
#include <string>

bool issame(std::vector<std::string> a, std::vector<std::string> b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    std::vector<std::string> vec1, vec2;
    int n;
    std::cout << "Enter the size of vectors: ";
    std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        std::string str;
        std::cout << "Enter string for vector 1: ";
        std::cin >> str;
        vec1.push_back(str);
        
        std::cout << "Enter string for vector 2: ";
        std::cin >> str;
        vec2.push_back(str);
    }
    
    if (issame(vec1, vec2)) {
        std::cout << "Vectors are same.\n";
    } else {
        std::cout << "Vectors are not same.\n";
    }
    
    return 0;
}