vector<int> remove_duplicates(vector<int> numbers) {
    vector<int> unique_numbers;
    for (int num : numbers) {
        if (count(unique_numbers.begin(), unique_numbers.end(), num) == 0)
            unique_numbers.push_back(num);
    }
    return unique_numbers;
}