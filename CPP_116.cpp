Here is the completed code:

vector<int> sort_array(vector<int> arr){
    vector<int> result;
    for(int i: arr) {
        int ones = 0;
        int num = i;
        while(num > 0) {
            if((num & 1) == 1)
                ones++;
            num >>= 1;
        }
        result.push_back({ones, i});
    }
    sort(result.begin(), result.end());
    vector<int> res;
    for(auto x: result) {
        res.push_back(x.second);
    }
    return res;
}