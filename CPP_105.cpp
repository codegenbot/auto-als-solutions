using namespace std;
vector<string> by_length(vector<int> arr){
    vector<string> result;
    map<int,string> numNames = {{1,"One"},{2,"Two"},{3,"Three"},{4,"Four"},{5,"Five"},{6,"Six"},{7,"Seven"},{8,"Eight"},{9,"Nine"}; 
    for(auto x:arr){
        if(x>=1 && x<=9)result.push_back(numNames[x]);
    }
    sort(result.begin(),result.end());
    reverse(result.begin(),result.end());
    return result;
}