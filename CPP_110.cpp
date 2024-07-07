bool hasOdd(int x) {
    return (x & 1);
}

string exchange(vector<int> lst1, vector<int> lst2) {
    int oddCount = 0;
    for (int i = 0; i < lst1.size(); i++) {
        if (hasOdd(lst1[i])) {
            oddCount++;
        }
    }

    if (oddCount > (lst2.size() - oddCount)) {
        return "NO";
    }

    return "YES";
}