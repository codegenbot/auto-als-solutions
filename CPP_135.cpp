int can_arrange(vector<int> arr){
    int max_index = -1;
    for(int i=1; i<arr.size(); i++){
        if(arr[i-1] <= arr[i]){
            max_index = i-1;
        }
    }
    return max_index;
}