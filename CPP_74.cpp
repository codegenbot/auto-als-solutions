vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    int sum1 = 0;
    for (const string& s : lst1) {
        sum1 += s.size();
    }
    
    int sum2 = 0;
    for (const string& s : lst2) {
        sum2 += s.size();
    }
    
    if (sum1 < sum2) return lst1;
    else if (sum1 > sum2) return lst2;
    else {
        bool isSame = true;
        for(int i=0; i<lst1.size() && i<lst2.size();i++){
            if(lst1[i]!=lst2[i]){
                isSame=false;
                break;
            }
        }
        
        if(isSame) return lst1;
        else return {"Both lists are the same" };
    }
}

bool issame(vector<string> a, vector<string> b) {
    bool isSame = true;
    for(int i=0; i<a.size() && i<b.size();i++){
        if(a[i]!=b[i]){
            isSame=false;
            break;
        }
    }
    return isSame;
}