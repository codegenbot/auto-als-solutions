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
    std::vector<std::string> a, b;
    
    int n;
    std::cout << "Enter the number of strings: ";
    std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        std::string s;
        std::cout << "Enter string " << i + 1 << ": ";
        std::getline(std::cin, s);
        
        if (i == 0) {
            a.push_back(s);
        } else {
            b.push_back(s);
        }
    }
    
    bool result = issame(a, b);
    
    if (result) {
        std::cout << "The two lists of strings are the same." << std::endl;
    } else {
        std::cout << "The two lists of strings are not the same." << std::endl;
    }
    
    return 0;
}