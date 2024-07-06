std::string flip_case(std::string str){
    std::string result = "";
    for(char c: str){
        if(isalpha(c)){
            if(islower(c))
                result += toupper(c);
            else
                result += tolower(c);
        }else{
            result += c;
        }
    }
    return result;