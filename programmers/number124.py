def convert(n):
    T = "124"
    if n <= 3:
        return T[n-1]
    else:
        q, r = divmod(n-1, 3)
        return convert(q) + T[r]
    
def solution(n):
    answer = convert(n)
    return answer