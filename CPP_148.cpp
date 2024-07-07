#include <vector>
#include <string>

using namespace std;

vector<string> bf(string planet1, string planet2) {
    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    
    if (find(planets.begin(), planets.end(), planet1) == planets.end() || 
        find(planets.begin(), planets.end(), planet2) == planets.end()) {
        return {};
    }
    
    int index1 = distance(planets.begin(), find(planets.begin(), planets.end(), planet1));
    int index2 = distance(planets.begin(), find(planets.begin(), planets.end(), planet2));

    if (index1 > index2) {
        swap(index1, index2);
    }

    vector<string> result;
    for (int i = index1 + 1; i < index2; i++) {
        result.push_back(planets[i]);
    }
    
    return result;
}