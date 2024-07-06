bool check_dict_case(map<string,string> dict){
    bool all_upper = true;
    bool all_lower = true;

    for (auto& pair : dict) {
        string key = pair.first;
        if (!all_upper && !all_lower) {
            return false;
        }
        for (char& c : key) {
            if (isupper(c)) {
                all_upper = true;
                break;
            }
            else if (islower(c)) {
                all_lower = true;
                break;
            }
        }
    }

    if(dict.empty())
        return false;

    return all_upper || all_lower;
}