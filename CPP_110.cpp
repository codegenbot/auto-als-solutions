```cpp
#include <vector>
#include <string>

bool hasOdd(vector<int>& vec) {
    for (int num : vec) {
        if (num % 2 != 0)
            return true;
    }
    return false;
}

string exchange(vector<int> lst1, vector<int> lst2) {
    while (!hasOdd(lst1)) {
        bool found = false;
        for (int i = 0; i < lst2.size(); i++) {
            if (lst2[i] % 2 != 0) {
                swap(lst1.back(), lst2[i]);
                found = true;
                break;
            }
        }
        if (!found)
            return "NO";
    }
    return "YES";
}

int main() {
    vector<int> lst1, lst2;
    int n1, n2;

    cout << "Enter the number of elements in list 1: ";
    cin >> n1;

    for (int i = 0; i < n1; i++) {
        cout << "Enter element " << i+1 << ": ";
        cin >> lst1.push_back();
    }

    cout << "Enter the number of elements in list 2: ";
    cin >> n2;

    for (int i = 0; i < n2; i++) {
        cout << "Enter element " << i+1 << ": ";
        cin >> lst2.push_back();
    }
    
    cout << exchange(lst1, lst2) << endl;
}