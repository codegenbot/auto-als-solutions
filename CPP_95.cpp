int main 
{
    map<string, string> dict = {{"Hello", "hello"}, {"WORLD", "world"}};
    cout << (check_dict_case(dict) ? "True" : "False") << endl;
    assert(check_dict_case({}) == false);
    return 0;