# given a regular expression, with char, * and .
# * means match zero or more chars
# . means mathc exactly one any chars.
# return if str is match the pattern.



def match(pattern, str):
    if len(pattern) == 0 and len(str) == 0:
        return True
    
    if len(pattern) == 0 or len(str) == 0:
        return False
    
    if pattern[0] != '.' and pattern[0] != '*':
        if str[0] == pattern[0]:
            return match(pattern[1:], str[1:])
        else:
            return False
    elif pattern[0] == '.':
        return match(pattern[1:], str[1:])
    else:
        return match(pattern, str[1:]) or match(pattern[1:], str[1:]) or match(pattern[1:], str)