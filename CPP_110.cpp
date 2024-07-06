Here is the solution:

string exchange(vector<int> lst1, vector<int> lst2) {
    bool possible = true;
    for (int num : lst1) {
        if (num % 2 != 0) {
            for (int &otherNum : lst2) {
                if (otherNum % 2 == 0) {
                    swap(num, otherNum);
                    possible = false;
                    break;
                }
            }
            if (!possible)
                break;
        }
    }
    return possible ? "YES" : "NO";
}