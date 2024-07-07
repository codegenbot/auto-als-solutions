using namespace std;
vector<string> by_length(vector<int> arr){
    vector<string> result;
    map<int,string> numNames = {{1,"One"},{2,"Two"},{3,"Three"},{4,"Four"},{5,"Five"},{6,"Six"},{7,"Seven"},{8,"Eight"},{9,"Nine"}; 
    for(auto x:arr)result.push_back(to_string(x));
    return result;
}