Here's the completed code:

int max_element(vector<int> l){
    int m = l[0];
    for(int i=1;i<l.size();i++){
        if(l[i]>m)
            m=l[i];
    }
    return m;
}