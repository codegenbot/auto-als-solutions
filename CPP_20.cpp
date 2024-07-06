#include <vector>
#include <algorithm>

// Your existing function
bool issame(float a, float b) {
    return (a == b);
}

// Function to find the closest pair of elements
int find_closest_elements(std::vector<int> vec) {
    int min_diff = INT_MAX;
    for(int i = 0; i < vec.size(); ++i) {
        for(int j = i+1; j < vec.size(); ++j) {
            if(abs(vec[i] - vec[j]) < min_diff)
                min_diff = abs(vec[i] - vec[j]);
        }
    }
    return min_diff;
}

int main() {
    std::vector<int> vec;
    
    // Read input from user
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    for(int i = 0; i < n; ++i) {
        int x;
        std::cout << "Enter element " << (i+1) << ": ";
        std::cin >> x;
        vec.push_back(x);
    }
    
    // Find and print the closest pair of elements
    int min_diff = find_closest_elements(vec);
    std::cout << "The closest pair has a difference of: " << min_diff << std::endl;

    return 0;
}