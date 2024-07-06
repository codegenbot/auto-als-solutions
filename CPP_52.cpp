bool below_threshold(vector<int> l, int t) {
    for (int num : l) {
        if (num >= t) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<int> numbers = {1, 2, 3};
    int threshold = 3;
    if (below_threshold(numbers, threshold)) {
        cout << "All numbers are below the threshold." << endl;
    } else {
        cout << "At least one number is not below the threshold." << endl;
    }
    return 0;
}