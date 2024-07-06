Here is the completed code:

string file_name_check(string file_name){
    int count = 0;
    bool has_dot = false;
    for(int i=0; i<file_name.length(); i++){
        if(file_name[i] >= '0' && file_name[i] <= '9'){
            count++;
            if(count > 3) return "No";
        }
        else if(file_name[i] == '.'){
            has_dot = true;
        }
        else if(i > 0 && !has_dot){
            if(!isalpha(file_name[i])) return "No";
        }
    }
    if(!has_dot) return "No";
    size_t pos = file_name.find('.');
    string ext = file_name.substr(pos+1);
    if(ext != "txt" && ext != "exe" && ext != "dll") return "No";
    return "Yes";
}