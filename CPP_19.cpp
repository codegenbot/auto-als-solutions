#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

std::string sort_numbers(std::string numbers) {
    std::vector<std::string> numVec;
    std::string temp;

    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            numVec.push_back(temp);
            temp = "";
        } else {
            temp += numbers[i];
        }
    }
    numVec.push_back(temp);

    std::sort(numVec.begin(), numVec.end());

    std::string result = "";
    for (const auto& str : numVec) {
        result += str + " ";
    }

    return result;
}