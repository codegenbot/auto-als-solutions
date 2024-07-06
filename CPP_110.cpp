Here is the completed code:

string exchange(vector<int> lst1, vector<int> lst2) {
    bool allEven = true;
    for (int num : lst1) {
        if (num % 2 != 0) {
            allEven = false;
            break;
        }
    }
    if (!allEven) {
        for (auto& num : lst2) {
            int found = false;
            for (int& n : lst1) {
                if (n == num) {
                    found = true;
                    break;
                }
            }
            if (!found) return "NO";
        }
    }
    return allEven ? "YES" : "NO";
}