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
    
    int result = find(vec.begin(), vec.end(), 10);
    if(result == vec.end()) 
        cout << "Element not found.\n";
    else
        cout << "Element found at index: " << distance(vec.begin(), result) << ".\n";
    return 0;
}