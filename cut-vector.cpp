std::pair<std::vector<int>, std::vector<int>> cutVector(std::vector<int> v) {
    int minDiff = INT_MAX;
    int cutIndex = -1;

    for (int i = 0; i < v.size() - 1; i++) {
        int sumLeft = 0, sumRight = 0;

        for (int j = 0; j <= i; j++) {
            sumLeft += v[j];
        }

        for (int j = i + 1; j < v.size(); j++) {
            sumRight += v[j];
        }

        if (abs(sumLeft - sumRight) < minDiff) {
            minDiff = abs(sumLeft - sumRight);
            cutIndex = i;
        } else if (abs(sumLeft - sumRight) == 0 && cutIndex == -1) {
            minDiff = abs(sumLeft - sumRight);
            cutIndex = i;
        }
    }

    std::vector<int> left(v.begin(), v.begin() + cutIndex + 1);
    std::vector<int> right(v.begin() + cutIndex, v.end());

    return std::make_pair(left, right);
}