int smallest_change(vector<int> arr) {
    int n = arr.size();
    int left = 0, right = n - 1;
    int changes = 0;

    while (left < right) {
        if (arr[left] != arr[right]) {
            // count the number of elements to be changed
            int minChange = 1;
            for (int i = left + 1; i <= right; i++) {
                if (arr[i] == arr[right]) {
                    minChange = i - left;
                    break;
                }
            }
            changes += minChange;
            left += minChange;
        } else {
            left++;
            right--;
        }
    }

    return changes;
}