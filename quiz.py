'''Написати програму quiz.py, яка показує користувачу випадкове завдання 
та очікує від нього відповідь. 
Якщо відповідь правильна - привітати, та запропонувати наступне завдання. 
Якщо відповідь не правильна - запропонувати розв'язати те ж завдання ще раз. 
Щоб вийти з програми - варто написати q.
'''

print('''Вітаю!
Я допоможу тобі навчитись розв\'язувати математичні завдання! 
Напиши \'q\', щоб вийти або 'n' - щоб перейти до наступного завдання.
''')

from random import randint

vOperationsTuple = ('+', '-', '*', '/')

v1stOperand = randint(1, 100)
v2ndOperand = randint(1, 100)
vOperation  = randint(0, 3)
vAnswer     = 0
vNewTask    = False

while True:
    if vNewTask:
        v1stOperand = randint(1, 100)
        v2ndOperand = randint(1, 100)
        vOperation  = randint(0, 3)
        vAnswer     = 0    

    if vOperation == 0:
        vAnswer = v1stOperand + v2ndOperand
    elif vOperation == 1:
        vAnswer = v1stOperand - v2ndOperand
    elif vOperation == 2:
        vAnswer = v1stOperand * v2ndOperand
    elif vOperation == 3:
        vAnswer = v1stOperand / v2ndOperand

    vUserResult = input('Result {} {} {} = '.format(v1stOperand, vOperationsTuple[vOperation], v2ndOperand))

    if vUserResult == 'q':
        print('\nThat\'s all Folks!')
        break
    elif vUserResult == 'n':
        vNewTask = True

        print('\nSo sad, but as you wish!\n')
        continue
    else:
        vNewTask      = False
        vResult_Error = False
        vResult_Neg   = False

        vResult = vUserResult.strip()

        if vResult.find(',') > 0:
            vResult = vResult.replace(',', '.')  

        if vResult.find('-') == 0:
            vResult     = vResult.replace('-', '')
            vResult_Neg = True
    
        vResult_List = vResult.split('.')
    
        if len(vResult_List) == 1:
            if vResult.isnumeric():
                vResult = int(vResult_List[0])
            else:
                vResult_Error = True
        else:
            if len(vResult_List) == 2:
                vResult_Left  = vResult_List[0]
                vResult_Right = vResult_List[1]

                if vResult_Left.isnumeric() and vResult_Right.isnumeric():
                    vResult_Left  = int(vResult_Left)
                    vResult_Right = int(vResult_Right)

                    vResult = vResult_Left + vResult_Right / (10 ** len(str(vResult_Right)))
                else:
                    vResult_Error = True
            else:
                vResult_Error = True

        if not vResult_Error:  
            if vResult_Neg:
                vResult = -1 * vResult

            if vResult == vAnswer:
                print('Correctly!\n')

                vNewTask = True
            else:
                print('Unfortunately! Let\'s try again!\n')                 
        else:
            print('Wrong format! Let\'s try again!\n')  
