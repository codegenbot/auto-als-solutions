vector<int> pluck(vector<int> arr) {
    vector<int> result;
    if(arr.empty()) return result; // if array is empty, return an empty array
    
    int smallest_even = INT_MAX; // initialize with max value
    int index_of_smallest_even = 0;
    
    for(int i=0; i<arr.size(); i++) {
        if(arr[i] % 2 == 0 && arr[i] < smallest_even) {
            smallest_even = arr[i];
            index_of_smallest_even = i;
        }
    }
    
    result.push_back(smallest_even);
    result.push_back(index_of_smallest_even);
    
    return result;
}