from masks import get_mask_account, get_mask_card_number


def mask_account_card(name_of_card: str) -> str:
    '''Маскировка названия карты или счета'''
    mask_of_name = ''
    list_in_func = name_of_card.split(' ')
    if list_in_func[0] == 'Счет':
        list_in_func[-1] = get_mask_account(int(list_in_func[-1]))
#        mask_of_name = ' '.join(list_in_func)
#        mask_of_name = "Счет " + get_mask_account(int(list_in_func[1]))
    else:
        list_in_func[-1] = get_mask_card_number(int(list_in_func[-1]))
#        mask_of_name = ' '.join(list_in_func)
    return ' '.join(list_in_func)


if __name__ == "__main__":
#    print(get_mask_card_number(1564487911112386))
    print(mask_account_card('Visa Gold 5999414228426353'))
    print(mask_account_card('Счет 73654108430135874305'))
