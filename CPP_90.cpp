int findNextSmallest(vector<int> numbers) {
    if (numbers.empty()) {
        return 0;
    }
    
    int smallest = *min_element(numbers.begin(), numbers.end());
    for (int num : numbers) {
        if (num > smallest) {
            return num;
        }
    }
    return -1; 
}