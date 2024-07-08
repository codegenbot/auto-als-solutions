#include <iostream>
#include <string>

std::string validateTweet(std::string tweet) {
    if (tweet.empty()) {
        return "You didn't type anything";
    } else if (tweet.length() > 140) {
        return "Too many characters";
    } else {
        return "Your tweet has " + std::to_string(tweet.length()) + " characters";
    }
}

int main() {
    int n;
    std::cin >> n;
    
    for(int i = 0; i < n; ++i) {
        std::string tweet;
        std::getline(std::cin, tweet);
        std::cout << validateTweet(tweet) << "\n";
    }
    
    return 0;
}