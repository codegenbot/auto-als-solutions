int main() {
    string brackets;
    cin >> brackets;

    bool result = true;
    int count = 0;
    
    for(int i=0; i<brackets.length(); i++) {
        if(brackets[i] == '<') {
            count++;
        } else if(brackets[i] == '>') {
            if(count == 0) {
                result = false;
                break;
            }
            count--;
        }
    }

    if(count != 0) {
        result = false;
    }

    cout << result << endl;

    return 0;
}