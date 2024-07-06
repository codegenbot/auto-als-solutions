def decode_cyclic(s: str):
    result = ""
    i = 0
    while i < len(s):
        if i + 2 >= len(s):  
            result += s[i:]      
            break
        elif s[i] == s[i+2]:   
            result += s[i:i+3]  
            i += 3
        else:                  
            if i > 0:          
                result += s[i-1:i+2]
            else:
                result = s[:i+2]
            i += 3
    return result