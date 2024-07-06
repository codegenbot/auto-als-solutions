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
    vector<int> vec1, vec2;
    int num;

    cout << "Enter elements for list 1: ";
    while (cin >> num) {
        vec1.push_back(num);
    }

    cout << "Enter elements for list 2: ";
    while (cin >> num) {
        vec2.push_back(num);
    }

    cout << "The answer is: " << exchange(vec1, vec2);

    return 0;
}