int main() {
    string output;
    output = words_in_sentence("here is");
    assert(output == "is");
    return 0;
}

string words_in_sentence(string sentence){
    string word;
    int count = 0;
    for(int i=0; i<sentence.size(); i++){
        if(sentence[i] == ' '){
            count++;
            continue;
        }
        bool isPrime = true;
        for(int j=2; j*j<=count+1; j++){
            if((count+1)%j==0){
                isPrime = false;
                break;
            }
        }
        if(isPrime) word += sentence.substr(i-count, count)+ " ";
        count++;
    }
    return word;
}