vector<int> strange_sort_vector(vector<int> lst) {
    vector<int> result;
    if(lst.empty()) return result;

    std::sort(lst.begin(), lst.end());
    bool isMin = true;
    
    for(int i : lst) {
        if(isMin) {
            result.push_back(*min_element(lst.begin(), lst.end()));
            lst.erase(remove(lst.begin(), lst.end(), *min_element(lst.begin(), lst.end())), lst.end());
        } else {
            result.push_back(*max_element(lst.begin(), lst.end()));
            lst.erase(remove(lst.begin(), lst.end(), *max_element(lst.begin(), lst.end())), lst.end());
        }
        
        isMin = !isMin;
    }

    return result;
}