int main() {
    vector<int> arr = {9, 4, 8};
    vector<string> result1 = by_length(arr);
    vector<string> result2={"Nine", "Four", "Eight"};
    assert(issame(result1, result2)); 
    return 0;
}