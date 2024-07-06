map<string,int> numMap = {{"zero",0},{"one",1},{"two",2},{"three",3},{"four",4},{"five",5},{"six",6},{"seven",7},{"eight",8},{"nine",9}};

string sort_numbers(string numbers){
    string result;
    vector<string> nums;
    size_t pos;
    string token;

    // tokenize the input string
    while((pos = numbers.find(" ")) != string::npos) {
        token = numbers.substr(0, pos);
        if(numMap.count(token)) {
            nums.push_back(token);
        }
        numbers.erase(0, pos + 1);
    }

    if(numMap.count(numbers)) {
        nums.push_back(numbers);
    }

    // sort the vector of strings
    sort(nums.begin(), nums.end());

    // concatenate the sorted string
    for(size_t i = 0; i < nums.size(); ++i) {
        result += nums[i];
        if(i < nums.size() - 1) {
            result += " ";
        }
    }

    return result;
}