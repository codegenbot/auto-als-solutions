#include <iostream>
#include <cstring>
using namespace std;

int str_len(char *str){
    int len = 0;
    while (*str != '\0'){
        len++;
        str++;
    }
    return len;
}

int new_main(){
    char s[] = "Hello, World!";
    cout << "The length of the string is: " << str_len(s) << endl;
    return 0;
}