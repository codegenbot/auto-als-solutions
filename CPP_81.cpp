#include <vector>
#include <string>

using namespace std;

vector<string> numerical_letter_grade(vector<float> grades) {
    vector<string> result;
    
    for (float g : grades) {
        if (g >= 4.0)
            result.push_back("A+");
        else if (g >= 3.7)
            result.push_back(g > 3.3 ? "A-" : "A");
        else if (g >= 3.3)
            result.push_back("A-");
        else if (g >= 3.0)
            result.push_back(g > 2.9 ? "B+" : "B");
        else if (g >= 2.7)
            result.push_back(g > 2.6 ? "B-" : "B");
        else if (g >= 2.0)
            result.push_back(g > 1.9 ? "C+" : "C");
        else if (g >= 1.7)
            result.push_back(g > 1.6 ? "C-" : "C");
        else if (g >= 1.0)
            result.push_back(g > 0.9 ? "D+" : "D");
        else
            result.push_back("E");
    }
    
    return result;
}