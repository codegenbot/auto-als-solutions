#include <algorithm>
#include <vector>
using namespace std;

int main() {
    vector<int> vec;
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    
    for(int i = 0; i < n; i++) {
        int num;
        cin >> num;
        vec.push_back(num);
    }
    
    assert(std::find(vec.begin(), vec.end(), 10) != vec.end());
    return 0;
}