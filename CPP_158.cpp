#include <string>
#include <vector>
#include <algorithm>

std::string find_max(std::vector<std::string> words){
    std::string max_str = *max_element(words.begin(), words.end(),
        [](const std::string& a, const std::string& b) {
            return count(a.begin(), a.end(), a[0]) > count(b.begin(), b.end(), b[0]);
        });
    return max_str;
}

int main() {
    assert ((find_max({"play", "play", "play"}) == "play"));
    return 0;
}