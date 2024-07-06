map<string,int> numMap;
numMap["zero"] = 0; numMap["one"] = 1; numMap["two"] = 2; 
numMap["three"] = 3; numMap["four"] = 4; numMap["five"] = 5; 
numMap["six"] = 6; numMap["seven"] = 7; numMap["eight"] = 8;
numMap["nine"] = 9;

string sort_numbers(string numbers){
    vector<string> nums;
    string temp;
    for(int i=0;i<numbers.size();i++){
        if(numbers[i] == ' ')
            continue;
        else{
            temp += numbers[i];
            if(i==numbers.size()-1)
                nums.push_back(temp);
            else
                while(i+1<numbers.size()&&numbers[i+1]!=' ')
                    i++;
        }
    }
    sort(nums.begin(),nums.end());
    string result = "";
    for(int i=0;i<nums.size();i++)
        result += nums[i] + " ";
    return result;
}