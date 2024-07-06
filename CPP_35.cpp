#include <algorithm>
#include <cmath>

int findMaxAndMin(int n) {
    int max = std::numeric_limits<int>::min();
    int min = std::numeric_limits<int>::max();

    for (int i = 0; i < n; i++) {
        int temp;
        std::cin >> temp;

        if (std::abs(temp) > max)
            max = std::abs(temp);
        if (std::abs(temp) < min)
            min = std::abs(temp);
    }

    return *std::max_element(std::vector<int>({min, max}));
}