Here is the solution:

string exchange(vector<int> lst1, vector<int> lst2) {
    int even = 0;
    for (int x : lst1) {
        if (x % 2 == 0)
            even++;
    }
    if (even == lst1.size())
        return "YES";
    else
        return "NO";
}