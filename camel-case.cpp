#include <vector>
#include <iostream>
#include <string>

std::string camelCase(std::string str) {
    std::vector<std::string> parts;
    size_t pos = 0;

    while ((pos = str.find('-')) != std::string::npos) {
        parts.push_back(str.substr(0, pos));
        str.erase(0, pos + 1);
    }

    if (!str.empty())
        parts.push_back(str);

    for (size_t i = 0; i < parts.size(); ++i) {
        if (i > 0)
            parts[i][0] = toupper(parts[i][0]);
    }

    std::string result;
    for (const auto& part : parts) {
        result += part;
        if (i + 1 < parts.size())
            result += " ";
        ++i;
    }
    
    return result;
}

int main() {
    int numCases;
    cin >> numCases;

    for(int i = 0; i < numCases; i++) {
        std::string str;
        cin >> str;
        cout << camelCase(str) << endl;
    }

    return 0;
}