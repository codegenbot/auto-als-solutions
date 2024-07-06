vector<string> by_length(vector<int> arr){
    vector<int> temp;
    for(int i : arr){
        if(i >= 1 && i <= 9)
            temp.push_back(i);
    }
    sort(temp.begin(), temp.end());
    reverse(temp.begin(), temp.end());
    vector<string> res;
    for(int i : temp){
        switch(i){
            case 1: res.push_back("One"); break;
            case 2: res.push_back("Two"); break;
            case 3: res.push_back("Three"); break;
            case 4: res.push_back("Four"); break;
            case 5: res.push_back("Five"); break;
            case 6: res.push_back("Six"); break;
            case 7: res.push_back("Seven"); break;
            case 8: res.push_back("Eight"); break;
            case 9: res.push_back("Nine"); break;
        }
    }
    return res;
}