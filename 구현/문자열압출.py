def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        prev = s[0:i]
        count = 1
        compressed = ""
        for j in range(i, len(s), i):
            if prev == s[j: j+i]:
                count += 1
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                count = 1
                prev = s[j:j+i]
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
    return answer