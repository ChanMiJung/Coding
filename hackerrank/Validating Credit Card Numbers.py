import re
def confirm(N, cards):
    for card in cards:
        isValid = True
        if re.search('[^0-9\-]', card) is not None or card[0] not in ['4', '5', '6']:
            isValid = False

        if isValid:
            card_digit = re.sub('-', '', card)
            if len(card_digit) != 16:
                isValid = False
            else:
                if '-' in card:
                    card_list = card.split('-')
                    for value in card_list:
                        if len(value) != 4:
                            isValid = False
                            break
                if isValid:
                    for idx in range(13):
                        if card_digit[idx:idx+4].count(card_digit[idx]) == 4:
                            isValid = False
                            break
            
        
        if isValid:
            print('Valid')
        else:
            print('Invalid')
            

if __name__ == '__main__':
    confirm(6, ['0525362587961578 ','44244x4424442444','4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456','5123 - 3567 - 8912 - 3456'])