vector<int> largest_smallest_integers(vector<int> lst){
    int a = 0, b = 0;
    for (int i : lst) {
        if (i < 0 && a == 0 || i > a) {
            a = i;
        }
        else if (i > 0 && b == 0 || i < b) {
            b = i;
        }
    }
    return {a, b};
}