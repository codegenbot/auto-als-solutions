string words_in_sentence(string sentence){
    string result = "";
    int count = 0;
    for(int i=1; i<=1000000; i++){
        if(isPrime(i)){
            count++;
        }
        else break;
    }
    for (auto &word : split(sentence, ' ')) {
        if(count-- > 0 && word.length() == isPrime(count+1)){
            result += word + " ";
        }
    }
    return result.substr(0, result.size()-1);
}

string split(string str, char delimeter) {
    string arr[100];
    int i = 0;
    int x = 0;
    while (str.length() > 0) {
        x = str.find(delimeter);
        if (x == 0)
            break;
        arr[i] = str.substr(0, x);
        str = str.substr(x + 1);
        i++;
    }
    arr[i] = str;
    string result = "";
    for(int j=0; j<i+1;j++){
        result += arr[j];
        if(j < i)
            result += " ";
    }
    return result;
}

bool isPrime(int n) {
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}