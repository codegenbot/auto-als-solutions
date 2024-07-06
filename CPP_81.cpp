#include <vector>
#include <string>

bool issame(std::vector<std::string> a, std::vector<std::string> b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

int main() {
    std::vector<std::string> vec1, vec2;
    int n;
    std::cout << "Enter the number of strings: ";
    std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        std::string str;
        std::cout << "Enter string " << i + 1 << ": ";
        std::getline(std::cin, str);
        vec1.push_back(str);
    }
    
    for (int i = 0; i < n; i++) {
        std::string str;
        std::cout << "Enter string " << i + 1 << ": ";
        std::getline(std::cin, str);
        vec2.push_back(str);
    }
    
    if (issame(vec1, vec2)) {
        std::cout << "The two vectors are the same.\n";
    } else {
        std::cout << "The two vectors are not the same.\n";
    }
    return 0;
}