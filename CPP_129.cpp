#include <vector>
#include <queue>

int minPath(const std::vector<std::pair<int, int>>& grid, int totalLength) {
    if (grid.empty()) return -1;

    int res[totalLength];
    for(int i = 0; i < totalLength; i++) res[i] = 0;
    
    std::queue<std::pair<int, int>> Q;
    for (const auto& p : grid) {
        Q.push({p.first, p.second});
    }
    
    while (!Q.empty()) {
        int x = Q.front().first;
        int y = Q.front().second;
        Q.pop();
        
        if (res[y] == 0) res[y] = (x == 0)?1:(int)2;
        for (const auto& p : grid) {
            if (p.second != 3 && x == p.first) {
                Q.push({p.first, p.second});
            }
            if (p.first > x || p.second > y) continue;
            if (res[p.second] == res[y]) break;
            if (res[p.second] == 0) {
                Q.push({p.first, p.second});
                res[p.second] = (x == 0)?1:(int)2;
            }
        }
    }
    
    int totalSteps = 0;
    for(int i = totalLength - 1; i >= 0; i--) {
        if(res[i] == 1) totalSteps++;
        else if(res[i] > 1) break;
    }
    
    return totalSteps;
}