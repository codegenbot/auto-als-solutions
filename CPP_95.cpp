bool check_dict_case(map<string,string> dict){
    if(dict.empty()) return false;

    bool all_upper = true;
    bool all_lower = true;

    for(auto &p : dict) {
        string key = p.first;
        for(int i = 0; i < key.length(); i++) {
            if(isupper(key[i])) all_lower = false;
            else if(islower(key[i])) all_upper = false;
        }
    }

    return (all_upper && !all_lower) || (!all_upper && all_lower);
}