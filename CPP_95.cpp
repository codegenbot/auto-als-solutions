int main 
{
    std::map<std::string, std::string> dict = {{"Hello", "hello"}, {"WORLD", "world"}};
    std::cout << (check_dict_case(dict) ? "True" : "False") << std::endl;
    using std::size_type;
    assert(check_dict_case(std::map<std::string, std::string>()) == false);
    return 0;
}