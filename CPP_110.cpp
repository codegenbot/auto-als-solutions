Here is the solution:

string exchange(vector<int> lst1, vector<int> lst2) {
    int oddCount = 0;
    for (int num : lst1) {
        if (num % 2 != 0) {
            oddCount++;
        }
    }
    for (int i = 0; i < lst2.size(); i++) {
        if (lst1.size() - oddCount <= 0) return "NO";
        int val = lst2[i];
        for (int j = 0; j < lst1.size(); j++) {
            if (val % 2 == 0 && lst1[j] % 2 != 0) {
                swap(lst1[j], val);
                break;
            }
        }
    }
    return "YES";
}