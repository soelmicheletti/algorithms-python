def kmp(pat, txt):
    lps = [0]
    l = 0
    idx = 1
    while idx < len(pat):
        if pat[l] == pat[idx]:
            l += 1
            lps.append(l)
            idx += 1
        else:
            if l == 0:
                lps.append(0)
                idx += 1
            else:
                l = lps[l-1]
    res = []

    i = 0
    j = 0

    while i < len(txt):
        if pat[j] == txt[i]:
            i += 1
            j += 1
            if j == len(pat):
                res.append(i - len(pat))
                j = lps[j-1]
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
    return res
