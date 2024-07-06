string findLongest(vector<string> strings){
    if(strings.empty()) return "";
    string maxString = strings[0];
    for(auto str : strings){
        if(str.length() > maxString.length()){
            maxString = str;
        }
        else if(str.length() == maxString.length())
            maxString = str;
    }
    return maxString;
}