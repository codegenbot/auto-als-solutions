Here is the completed code:

string file_name_check(string file_name){
    int count = 0;
    bool has_dot = false;
    for(int i = 0; i < file_name.length(); i++){
        if(file_name[i] >= '0' && file_name[i] <= '9'){
            count++;
            if(count > 3) return "No";
        }
        else if(file_name[i] == '.'){
            has_dot = true;
        }
        else if(!has_dot && !isalpha(file_name[i])){
            return "No";
        }
    }
    if(!has_dot) return "No";
    string extension = file_name.substr(file_name.find('.') + 1);
    if(extension != "txt" && extension != "exe" && extension != "dll") return "No";
    return "Yes";
}