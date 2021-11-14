def sorting(string):
    lower_case, upper_case, odd, even = [], [], [], []
    for character in string:
        if character.islower():
            lower_case.append(character)
        elif character.isupper():
            upper_case.append(character)
        elif character.isdigit():
            integer = int(character)
            if integer % 2 == 0:
                even.append(character)
            else:
                odd.append(character)
    lower_case.sort()
    upper_case.sort()
    odd.sort()
    even.sort()
    answer = ''.join(lower_case+upper_case+odd+even)
    print(answer)
            

if __name__ == '__main__':
    sorting('Sorting1234')