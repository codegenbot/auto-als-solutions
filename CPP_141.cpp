Here is the completed code:

string file_name_check(string file_name){
    int count = 0;
    bool has_dot = false;
    for(int i=0; i<file_name.length(); i++){
        if(isdigit(file_name[i])){
            count++;
            if(count > 3) return "No";
        }
        else if(file_name[i] == '.'){
            has_dot = true;
        }
        else if(i > 0 && !isalpha(file_name[i-1]) && file_name[i-1] != '.') return "No";
    }
    if(!has_dot || count > 3) return "No";
    size_t pos = file_name.find('.');
    string suffix = file_name.substr(pos+1);
    if(suffix != "txt" && suffix != "exe" && suffix != "dll") return "No";
    return "Yes";
}