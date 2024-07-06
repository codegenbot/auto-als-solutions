vector<vector<int>> get_row(vector<vector<int>> lst, int x) {
    vector<vector<int>> result;
    for (int i = 0; i < lst.size(); ++i) {
        if(lst[i].size() > 0 && lst[i][x] != 0){
            result.push_back(lst[i]);
        }
    }
    return result;
}