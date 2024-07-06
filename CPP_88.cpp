#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> sort_array(vector<int> array){
    int first = array.empty() ? 0 : array[0];
    int last = array.empty() ? 0 : array.back();
    vector<int> result = array;
    
    if ((first + last) % 2 == 1)
        sort(result.begin(), result.end());
    else
        sort(result.begin(), result.end(), greater<int>());
    
    return result;
}