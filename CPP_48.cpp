string text = "";
for (int i = text.length() - 1; i >= 0; --i) {
    if (text[i] != text[0]) return false;
    ++text[0];
}
return true;