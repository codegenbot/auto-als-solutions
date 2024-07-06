#include <vector>
#include <algorithm>

std::pair<std::vector<float>, std::vector<float>> find_closest_elements(std::vector<float> sorted_points_a, std::vector<float> sorted_points_b) {
    std::vector<float> closest_points;
    float min_distance = INT_MAX;

    for (int i = 0; i < sorted_points_a.size() - 1; i++) {
        for (int j = 0; j < sorted_points_b.size() - 1; j++) {
            float distance = pow(sorted_points_a[i] - sorted_points_a[i + 1], 2) + pow(sorted_points_b[j] - sorted_points_b[j + 1], 2);
            if (distance < min_distance) {
                min_distance = distance;
                closest_points = {{sorted_points_a[i], sorted_points_a[i + 1]}, {sorted_points_b[j], sorted_points_b[j + 1]}};
            }
        }
    }

    return closest_points;
}

bool issame(vector<float> a, vector<float> b) {
    return (a.size() == b.size() && equal(a.begin(), a.end(), b.begin()));
}