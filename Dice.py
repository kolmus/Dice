from random import randint

def roll_the_dice(dice):
    mod_dice = dice.upper()

    allowed = [
        'D3',
        'D4',
        'D6',
        'D8',
        'D10',
        'D12',
        'D20',
        'D100',
    ]
    if len(mod_dice.split('D')) == 2: # looking for D
        if mod_dice.split('D')[0] == '': # looking for anything before D
            num_roll = 1
        else:
            try:
                num_roll = int(mod_dice.split('D')[0]) # checking if it is int before D ald fix error
            except ValueError:
                return 'Incorrect value. Try again!'

        hid_val = mod_dice.split('D')[1] # everything after D - made for more readable code

        if len(hid_val.split('+')) == 2: # checking if secend element include +
            type_dice = 'D' + hid_val.split('+')[0]
            add_val = hid_val.split('+')[1]
            modyficator = '+'

        elif len(hid_val.split('-')) == 2: # checking if second element include -
            type_dice = 'D' + hid_val.split('-')[0]
            add_val = hid_val.split('-')[1]
            modyficator = '-'

        elif len(hid_val.split('+')) == 1 and len(hid_val.split('-')) == 1: # run when there is no added value
            type_dice = 'D' + hid_val
            add_val = 0
            modyficator = None
        else:
            return 'Incorrect value. Try again! + - albo brak znaku'+", ".join([hid_val, str(num_roll), mod_dice])

        if type_dice not in allowed:
            return f'Incorrect dice. You can use {", ".join(allowed)}'

        result = 0
        for i in range(num_roll):
            result += randint(1, int(type_dice[1:]))

        if modyficator == '+':
            result += int(add_val)
        elif modyficator == '-':
            result -= int(add_val)
        return result

    else:
        return 'Incorrect value. Try again! nie ma d'



hit = input('\n  Type your dice: ')
print(f'\nYour result is:   {roll_the_dice(hit)}\n')
