#include <algorithm>
#include <vector>
using namespace std;

int findElement(const vector<int>& vec, int target) {
    return distance(vec.begin(), find(vec.begin(), vec.end(), target));
}

int main() {
    vector<int> vec;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    vec.resize(n);
    
    cout << "Enter the elements: ";
    for(int i = 0; i < n; i++)
        cin >> vec[i];
    
    int result = findElement(vec, 10);
    if(result != -1) {
        cout << "The element 10 is at position: " << result << endl;
    } else {
        cout << "The element 10 does not exist in the vector." << endl;
    }
    
    return 0;
}