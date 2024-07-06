#include <vector>
#include <algorithm>

using namespace std;

string sort_numbers(string numbers) {
    vector<string> numVector;
    string word;
    
    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            numVector.push_back(word);
            word = "";
        } else {
            word += numbers[i];
        }
    }
    numVector.push_back(word);

    sort(numVector.begin(), numVector.end());

    string result;
    for (int i = 0; i < numVector.size(); i++) {
        if (i == 0)
            result = numVector[i];
        else
            result += " " + numVector[i];
    }

    return result;
}