vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    
    for(auto str : lst){
        if(str.length() % 2 == 0) // Check if string length is even
            result.push_back(str);
    }
    
    sort(result.begin(), result.end(), 
         [](const string &a, const string &b){
             int len = min(a.size(), b.size());
             for(int i=0; i<len; i++){
                 if(a[i] < b[i]) return true;
                 else if(a[i] > b[i]) return false;
             }
             return a.size() < b.size();
         });
    
    return result;
}