Here is the completed code:

```cpp
int starts_one_ends(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        if ((i == 1 || i == n) && n >= 2) {
            count++;
        }
        else if ((i > 1 && i < n) && n >= 3) {
            count++;
        }
    }
    return count;
}