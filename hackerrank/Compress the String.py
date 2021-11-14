# Enter your code here. Read input from STDIN. Print output to STDOUT
def compress(string):
    answer = ''
    while string:
        character = string[0]
        index = 0
        for idx in range(len(string)+1):
            if idx == len(string) or string[idx] != character:
                index = idx
                break
        answer += f'({index}, {character}) '
        string = string[index:]
    string = string[:-1]
    print(answer)

if __name__ == '__main__':
    compress('1222311')