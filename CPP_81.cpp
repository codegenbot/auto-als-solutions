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
    int n1, n2;
    std::vector<std::string> v1, v2;

    // Read user input
    std::cout << "Enter number of strings for vector 1: ";
    std::cin >> n1;

    for (int i = 0; i < n1; i++) {
        std::string temp;
        std::cout << "Enter string " << i + 1 << ": ";
        std::getline(std::cin, temp);
        v1.push_back(temp);
    }

    std::cout << "Enter number of strings for vector 2: ";
    std::cin >> n2;

    for (int i = 0; i < n2; i++) {
        std::string temp;
        std::cout << "Enter string " << i + 1 << ": ";
        std::getline(std::cin, temp);
        v2.push_back(temp);
    }

    if (issame(v1, v2)) {
        std::cout << "Vectors are same." << std::endl;
    } else {
        std::cout << "Vectors are not same." << std::endl;
    }

    return 0;
}