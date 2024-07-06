#include <vector>
#include <cassert>

bool issame(const std::vector<float>& a, const std::vector<float>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

vector<vector<float>> split(vector<float> l) {
    vector<vector<float>> result;
    float current = 0.0f;
    for (float num : l) {
        if (num > current) {
            result.push_back({current});
            current = num;
        }
    }
    result.push_back({current});
    return result;
}

int main() {
    vector<float> input = {1, -2, 3, 4, -5, 6};
    vector<vector<float>> output = split(input);
    for (const auto& segment : output) {
        for (float num : segment) {
            std::cout << num << " ";
        }
        std::cout << "\n";
    }
    return 0;
}