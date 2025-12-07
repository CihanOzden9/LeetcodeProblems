

def solution(s):
    
    def expand(left, right):
        # merkezden genişle
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    res = ""
    for i in range(len(s)):
        # Tek merkezli (örnek: "aba")
        tmp1 = expand(i, i)
        # Çift merkezli (örnek: "abba")
        tmp2 = expand(i, i + 1)

        # Daha uzun olanı seç
        if len(tmp1) > len(res):
            res = tmp1
        if len(tmp2) > len(res):
            res = tmp2

    return res