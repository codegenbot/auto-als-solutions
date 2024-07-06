Here is the completed code:

int next_smallest(vector<int> lst) {
    vector<int> vec = lst; // copy the input vector
    if (vec.empty()) return -1; // empty vector has no 2nd smallest element
    sort(vec.begin(), vec.end()); // sort the vector in ascending order
    for (int i = 1; i < vec.size(); i++) {
        if (vec[i] != vec[0]) { // found a different element from the first one
            return vec[i]; // this is the 2nd smallest element
        }
    }
    return -1; // all elements are equal to the first one, no 2nd smallest
}