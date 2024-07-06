int 
{
#define _CRT_SECURE_NO_WARNINGS
std::string user_input;
std::cout << "Enter a string: ";
std::getline(std::cin, user_input);

std::vector<std::string> words = split_words(user_input);
for (const auto& word : words) {
    std::cout << word << std::endl;
}