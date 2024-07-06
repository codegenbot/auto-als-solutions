int fruit_distribution(string s, int n) {
    size_t pos = 0;
    string numStr;
    int totalApplesAndOranges = 0;

    // Find the number of apples and oranges in the string
    while ((pos = s.find(" and ")) != string::npos) {
        numStr = s.substr(0, pos);
        if (numStr.find("apples") != string::npos || numStr.find("oranges") != string::npos) {
            size_t start = 0;
            if (numStr.find("apples") == 0)
                start = numStr.find(" ") + 1;
            else
                start = numStr.find(" ") + 5; // "and" is 3 characters long

            string temp = numStr.substr(start, pos - start);
            int count = stoi(temp);
            if (numStr.find("apples") != string::npos)
                totalApplesAndOranges += count;
            else
                totalApplesAndOranges -= count; // subtract oranges
        }
        s.erase(0, pos + 5); // erase " and "
    }

    // Check the remaining part of the string for any apples or oranges
    if (s.find("apples") != string::npos || s.find("oranges") != string::npos) {
        size_t start = 0;
        if (s.find("apples") == 0)
            start = s.find(" ") + 1;
        else
            start = s.find(" ") + 5; // "and" is 3 characters long

        string temp = s.substr(start);
        int count = stoi(temp);
        if (s.find("apples") != string::npos)
            totalApplesAndOranges += count;
        else
            totalApplesAndOranges -= count; // subtract oranges
    }

    return n - totalApplesAndOranges;
}