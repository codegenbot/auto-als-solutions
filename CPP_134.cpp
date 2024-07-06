int lastSpaceIndex = txt.find_last_of(' ');
return (lastSpaceIndex != string::npos && isalpha(txt.back()));