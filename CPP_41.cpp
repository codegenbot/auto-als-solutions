int car_race_collision(int n) {
    int collision_count = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i + j == n + 1) {
                collision_count++;
            }
        }
    }
    return collision_count;
}