vector<string> by_length(vector<int> arr){
    vector<int> nums;
    for(auto x:arr){
        if(x>=1 && x<=9)nums.push_back(x);
    }
    sort(nums.begin(),nums.end());
    reverse(nums.begin(),nums.end());
    vector<string> result;
    map<int,string> numNames = {{1,"One"},{2,"Two"},{3,"Three"},{4,"Four"},{5,"Five"},{6,"Six"},{7,"Seven"},{8,"Eight"},{9,"Nine"}; 
    for(auto x:nums)result.push_back(numNames[x]);
    return result;
}