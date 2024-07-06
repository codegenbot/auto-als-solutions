Here is the completed code:

int smallest_change(vector<int> arr){
    int n = arr.size();
    string str;
    for(int i=0; i<n; i++){
        str += to_string(arr[i]);
    }
    
    string rev = str;
    reverse(rev.begin(), rev.end());
    
    int count = 0;
    for(int i=0; i<n; i++){
        if(str[i] != rev[i]){
            count++;
        }
    }
    
    return count;
}