Here is the completed code:

int smallest_change(vector<int> arr) {
    int left = 0, right = arr.size() - 1, changes = 0;
    while (left < right) {
        if (arr[left] != arr[right]) {
            changes++;
            int i = 0;
            for (; i < arr.size(); i++) {
                if (arr[i] == arr[right]) {
                    swap(arr[left], arr[i]);
                    break;
                }
            }
            left++;
            right--;
        } else {
            left++;
            right--;
        }
    }
    return changes;
}