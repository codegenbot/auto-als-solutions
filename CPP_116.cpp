vector<int> sort_array(vector<int> arr) {
    vector<int> result = arr;
    sort(result.begin(), result.end(), [](int a, int b) {
        bitset<32> ba = a; // Convert a to bitset
        bitset<32> bb = b; // Convert b to bitset
        if (ba.count() == bb.count()) {
            return a < b;
        }
        return ba.count() < bb.count();
    });
    return result;
}