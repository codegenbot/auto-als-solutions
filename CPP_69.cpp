#include <vector>
#include <map>

using namespace std;

int search(vector<int> lst) {
    map<int, int> frequency;
    for (int num : lst) {
        frequency[num]++;
    }
    
    int result = -1;
    for (auto& pair : frequency) {
        if (pair.second >= pair.first && pair.first > 0) {
            result = pair.first;
            break;
        }
    }
    
    return result;
}