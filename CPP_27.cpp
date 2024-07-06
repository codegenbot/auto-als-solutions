#include<iostream>
using namespace std;

int main(){
    int i = 0;
    string str,filp_case(string str){
        while(i < str.length()){
            if(str[i] >= 'a' && str[i] <= 'z'){
                str[i] = toupper((char)str[i]); // Convert lowercase to uppercase
            }else if(str[i] >= 'A' && str[i] <= 'Z'){
                str[i] = tolower((char)str[i]); // Convert uppercase to lowercase
            }
            i++;
        }
        return str;
    }
    cin >> str;
    cout << filp_case(str) << endl;
    return 0;
}