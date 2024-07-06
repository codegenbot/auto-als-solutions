#include <initializer_list>
#include <vector>
#include <algorithm>

bool compare(const std::pair<int, int>& a, const std::pair<int, int>& b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second < b.second;
}

bool isSame(const std::vector<int> &v1, const std::vector<int> &v2) {
    if(v1.size() != v2.size())
        return false;

    for(int i = 0; i < v1.size(); i++)
        if(v1[i] != v2[i])
            return false;

    return true;
}

std::vector<int> pluck(std::vector<int> arr) {
    std::vector<std::pair<int, int>> nodes;
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] % 2 == 0) {
            nodes.push_back({arr[i], i});
        }
    }

    if (nodes.empty()) {
        return {};
    }

    std::sort(nodes.begin(), nodes.end(), compare);

    std::vector<int> result;
    for (size_t i = 1; i < nodes.size(); ++i) {
        if (compare({nodes[i-1].first, nodes[i-1].second}, {nodes[i].first, nodes[i].second}) != false) {
            return {};
        }
    }

    return {nodes[0].first};
}

int main() {
    std::vector<int> arr;
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> x;
        arr.push_back(x);
    }
    std::vector<int> result = pluck(arr);
    if(result.size() > 0)
    {
        std::cout << "The output is: " << *result.begin() << std::endl;
    }
    else
    {
        std::cout << "No output" << std::endl;
    }

    assert(isSame(pluck({7, 9, 7, 1}), {}));
    
    return 0;
}