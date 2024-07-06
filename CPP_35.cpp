#include <algorithm>

int findMax(int arr[], int size) {
    return *std::max_element(arr, arr + size);
}