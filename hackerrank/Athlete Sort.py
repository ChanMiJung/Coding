def sorting(N, M, ath_list, K):
    ath_list.sort(key=lambda x : x[K])
    for value in ath_list:
        answer = ' '.join(list(map(str, value)))
        print(answer)
            

if __name__ == '__main__':
    sorting(5, 3, [[10, 2, 5],[7, 1, 0],[9, 9, 9], [1, 23, 12],[6, 5, 9]], 1)