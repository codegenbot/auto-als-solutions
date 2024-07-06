int i = 0;
string filp_case(string str){
    while(i < str.length()){
        if(str[i] >= 'a' && str[i] <= 'z'){
            str[i] -= 32; // Convert lowercase to uppercase
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] += 32; // Convert uppercase to lowercase
        }
        i++;
    }
    return str;
}