bool will_it_fly(vector<int> q, int w) {
    string str = "";
    for(int i : q) {
        str += to_string(i);
    }
    
    if(str != reverse(string(str)).substr(0, str.length())) {
        return false;
    } else {
        return std::accumulate(q.begin(), q.end(), 0) <= w;
    }
}