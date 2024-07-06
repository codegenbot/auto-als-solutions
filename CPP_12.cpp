string findLongest(vector<string> strings){
    if(strings.empty()) return "";
    string maxStr = strings[0];
    for(auto str : strings){
        if(str.length() > maxStr.length()){
            maxStr = str;
        }
        else if(str.length() == maxStr.length())
            maxStr = str;
    }
    return maxStr;
}