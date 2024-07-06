#include <algorithm>
#include <vector>
using namespace std;

int main() {
    vector<int> vec;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    vec.resize(n);
    
    cout << "Enter the elements: ";
    for(int i = 0; i < n; i++)
        cin >> vec[i];
    
    bool found = false;
    for(auto it = vec.begin() + 1; it != vec.end(); ++it) {
        if(*it == vec[0]) {
            found = true;
            break;
        }
    }

    assert(found);
    return 0;
}