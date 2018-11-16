number = input('Enter number (15 or 16 digits): ').upper()
result = 0
for i in range(15):
    num = number[i]
    r = result
    if(i % 3 == 0):
        result += int(num)
    elif(i % 3 == 1):
        n = int(num) * 2
        result += int(n/10) + n % 10
    else:
        n = int(num) * 3
        result += int(n/10) + n % 10
remainder = result % 11
if(remainder == 0):
    digit = 0
elif(remainder == 1):
    digit = 'X'
else:
    digit = 11 - remainder
if len(number) == 15:
    print('Check digit is: {}'.format(digit))
else:
    print('Number {} check'.format('passes' if str(digit) == number[-1] else 'fails'))