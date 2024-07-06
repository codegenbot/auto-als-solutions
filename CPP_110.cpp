bool hasOdd(vector<int>& v) {
    for (int num : v) {
        if (num % 2 != 0)
            return true;
    }
    return false;
}

string exchange(vector<int> lst1, vector<int> lst2) {
    int oddCount = 0;
    for (int num : lst1) {
        if (num % 2 != 0) {
            oddCount++;
        }
    }
    if (!hasOdd(lst2)) {
        return "YES";
    } else if (oddCount == 0) {
        return "NO";
    } else {
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1[i] % 2 != 0 && oddCount > 0) {
                int j;
                for (j = 0; j < lst2.size(); j++) {
                    if (lst2[j] % 2 != 0) {
                        swap(lst1[i], lst2[j]);
                        oddCount--;
                        break;
                    }
                }
                if (oddCount > 0)
                    return "NO";
            }
        }
    }
    return "YES";
}