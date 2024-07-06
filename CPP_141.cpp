string file_name_check(string file_name){
    int count = 0;
    bool found_dot = false;
    string first_part, second_part;

    for(int i=0; i<file_name.size(); i++){
        if(isdigit(file_name[i])){
            count++;
            if(count > 3) return "No";
        }
        else if(file_name[i] == '.'){
            found_dot = true;
        }
        else if(found_dot){
            second_part += file_name[i];
        }
        else{
            first_part += file_name[i];
        }
    }

    if(!found_dot || first_part.empty() || (second_part != "txt" && second_part != "exe" && second_part != "dll"))
        return "No";
    
    return "Yes";
}