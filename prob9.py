text = input('Enter plain or cipher text: ').upper()
text += ' ' * ((5 - len(text) % 5) % 5)
key = '{0:030b}'.format(int(input('Enter key: ')))
reduced = [ord(n) - 32 for n in text]
binary = ['{0:06b}'.format(n) for n in reduced]
cipher = ''
count = -1
for i in range(0, len(binary), 5):
    combined = binary[i] + binary[i+1] + binary[i+2] + binary[i+3] + binary[i+4]
    xored = ''
    count+=1
    for j in range(len(combined)):
      a = bool(combined[j] == '0') 
      b = bool((key[count % len(key)] == '0'))
      c = bool((a and not b) or (b and not a))
      xored +=  '1' if (c) else '0'
      count+=1
    # print(xored)
    for j in range(0, len(xored), 6):
        # print(xored[j:(j+6)])
        cipher += chr(int(xored[j:(j+6)], 2)+32)
print(cipher)
