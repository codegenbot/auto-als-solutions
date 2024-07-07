#include <string>
using namespace std;

string word;
word = words_in_sentence("here is");
return 0;

string words_in_sentence(string sentence){
    string result = "";
    int count = 1;
    for(int i=0; i<sentence.size(); i++){
        if(sentence[i] == ' '){
            count++;
            continue;
        }
        bool isPrime = true;
        for(int j=2; j*j<=count; j++){
            if((count)%j==0){
                isPrime = false;
                break;
            }
        }
        if(isPrime) result += sentence.substr(i-count+1, 1)+ " ";
        count++;
    }
    return result;
}