Here is the completed code:

```cpp
bool iscuber(int a){
    int i = cbrt(a);
    return (i*i*i == a);
}