from itertools import combinations
def find_a(N, s, K):
    answer = 0
    s_list = list(s.split(' '))
    com_list = list(combinations(s_list, K))
    count = 0
    for value in com_list:
        if 'a' in value:
            count += 1
    answer = count/len(com_list)
    print(answer)

if __name__ == '__main__':
    find_a(4, 'a a c d', 2)