#include <algorithm>
#include <numeric>
#include <vector>

bool issame(vector<float> a,vector<float>b){
    return (a==b);
}

vector<float> find_closest_elements(vector<float> numbers) {
    sort(numbers.begin(), numbers.end());
    float minDiff = numeric_limits<float>::max();
    pair<float, float> closestPair;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        float diff = numbers[i + 1] - numbers[i];
        if (diff < minDiff) {
            minDiff = diff;
            closestPair.first = numbers[i];
            closestPair.second = numbers[i + 1];
        }
    }

    return {closestPair.first, closestPair.second};
}

int main() {
    assert(find_closest_elements({1.1, 2.2, 3.1, 4.1, 5.1}) == vector<float>{2.2, 3.1});
    // rest of your code
}