#include <string>
using namespace std;

bool prime_length(string str){
    int len = str.length();
    bool is_prime = true;
    if(len <= 1)
        return false;
    for(int i=2; i*i<=len; i++){
        if(len%i==0)
            is_prime = false;
    }
    return is_prime;

}

int main(){
    assert (prime_length("0") == false);
    return 0;
}