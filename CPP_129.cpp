```c
#include <vector>
#include <utility>

bool isEqual(std::vector<int> a, std::vector<int> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (a[i] != b[i])
            return false;
    return true;
}

int pathFinder(std::vector<std::vector<char>> grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    // Your implementation here
}