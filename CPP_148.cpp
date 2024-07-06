#include <stdio.h>
#include <vector>
#include <string>
using namespace std;

vector<string> bf(string planet1, string planet2) {
    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    int idx1 = -1, idx2 = -1;
    for (int i = 0; i < planets.size(); ++i) {
        if (planets[i] == planet1) idx1 = i;
        else if (planets[i] == planet2) idx2 = i;
        if (idx1 != -1 && idx2 != -1) break;
    }
    
    if (idx1 == -1 || idx2 == -1) return {};
    
    int start = min(idx1, idx2);
    int end = max(idx1, idx2);
    
    vector<string> result;
    for (int i = 0; i < planets.size(); ++i) {
        if (i >= start && i <= end) {
            result.push_back(planets[i]);
        }
    }
    
    return result;
}