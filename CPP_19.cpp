```c++
map<string,int> num_map;
num_map["zero"] = 0; num_map["one"] = 1; num_map["two"] = 2; 
num_map["three"] = 3; num_map["four"] = 4; num_map["five"] = 5;
num_map["six"] = 6; num_map["seven"] = 7; num_map["eight"] = 8; 
num_map["nine"] = 9;

string result = "";
for(string s : split(numbers,' ')) {
    for(map<string,int>::iterator it = num_map.begin(); it != num_map.end();++it) {
        if(it->first == s) {
            result += s + " ";
            break;
        }
    }
}
return result.substr(0,result.length()-1);
}

string split(const string& str,char delim)
{
    vector<string> tokens;
    size_t prev = 0, readPos = 0; 
    do {
        readPos = str.find(delim, prev);
        if (readPos == string::npos) readPos = str.length();
        string token = str.substr(prev, readPos - prev);
        if(token.length() > 0)
            tokens.push_back(token);
        prev = readPos + 1;
    } while (readPos < str.length());
    return join(tokens," ");
}

string join(const vector<string>& vec,char delim) {
    string s;
    for(auto& e : vec) {
        if(!s.empty())
            s += delim;
        s+=e;
    }
    return s;