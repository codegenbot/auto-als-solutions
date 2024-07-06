#include <algorithm>
#include <vector>
using namespace std;

int findElement(const vector<int>& vec, int target) {
    auto result = find(vec.begin(), vec.end(), target);
    if(result == vec.end()) 
        return -1;
    else
        return distance(vec.begin(), result);
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
    if(result == -1) 
        cout << "Element not found.\n";
    else
        cout << "Element found at index: " << result << ".\n";
    return 0;
}