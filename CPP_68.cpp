```cpp
#include <vector>
#include <algorithm>

struct pair {
    int first;
    int second;
};

bool compare(const struct pair& a, const struct pair& b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second < b.second;
}

std::vector<int> pluck(std::vector<int> arr) {
    std::vector<struct pair> nodes;
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] % 2 == 0) {
            nodes.push_back({arr[i], i});
        }
    }

    if (nodes.empty()) {
        return {};
    }

    std::sort(nodes.begin(), nodes.end(), compare);

    for (size_t i = 1; i < nodes.size(); ++i) {
        if (compare({nodes[i-1].first, nodes[i-1].second}, {nodes[i].first, nodes[i].second}) == false) {
            return {};
        }
    }

    int result = nodes[0].first;
    for(int i = 0; i < arr.size(); ++i){
        if(arr[i] == result){
            return {result};
        }
    }
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
    std::vector<int> output = pluck(arr);
    if(output.size() > 0)
    {
        std::cout << "The output is: " << output[0] << std::endl;
    }
    else
    {
        std::cout << "No output" << std::endl;
    }

    
    return 0;
}