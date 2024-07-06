int main() {
    cout << "{";
    for (const string& s : select_words("Mary had a little lamb", 4)) {
        cout << "\"" << s << "\", ";
    }
    cout << "}" << endl;
    return 0;
}