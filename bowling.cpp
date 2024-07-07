Here is the solution:

int bowling(string s) {
    int score = 0;
    for(int i = 0; i < 10; ++i){
        if(s[i] == 'X' || (s[i] == '/' && s[i+1] == 'X')){
            score += 30;
            continue;
        }
        else{
            int sum = 0;
            int j = i + 1;
            while(j < 10 && s[j] != '/'){
                if(s[j] == 'X'){
                    score += 10;
                    break;
                }
                else{
                    sum += (s[j]-'0');
                }
                j++;
            }
            if(sum == 10) {
                score += 10;
            }
            else {
                score += sum + s[i]-'0';
            }
        }
    }
    return score;
}