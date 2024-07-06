vector<int> sort_array(vector<int> array){
    int sum = array[0] + array[array.size()-1];
    vector<int> result;
    if(sum % 2 == 1)
        sort(array.begin(), array.end());
    else
        sort(array.rbegin(), array.rend());
    for(int i : array) {
        result.push_back(i);
    }
    return result;
}