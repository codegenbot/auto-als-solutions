#include <vector>
#include <string>
#include <stack>

using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    stack<string> parenStack;
    string currentParenString = "";

    for (char c : paren_string) {
        if (c == '(') {
            currentParenString += c;
            parenStack.push(currentParenString);
            currentParenString = "";
        } else if (c == ')') {
            currentParenString += c;
            stack<string> tempStack(parenStack);
            while (!tempStack.empty()) {
                string top = tempStack.top();
                tempStack.pop();
                if (top.back() == '(') {
                    tempStack.push(top);
                    break;
                }
                result.push_back(top);
            }
        } else {
            currentParenString += c;
        }
    }

    return result;
}