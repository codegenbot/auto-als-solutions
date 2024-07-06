vector<float> derivative(vector<float> xs) {
    vector<float> result(xs.size() - 1);
    for (int i = 0; i < result.size(); ++i) {
        if (i + 1 < xs.size()) {
            result[i] = (i + 1) * xs[i + 1];
        }
    }
    return result;
}