file_name = input('Enter artwork filename: ')
with open(file_name) as art:
    lines = art.readlines()
    lines[-1] += '\n'
    output = ''
    for line in lines:
        current_letter = ''
        count = 1
        for i in range(len(line)):
            if(i == 0):
                current_letter = line[i]
            elif(current_letter != line[i]):
                output += str(count) + current_letter
                count = 1
                current_letter = line[i]
            elif(count == 9):
                output += str(count) + current_letter
                count = 1
            else:
                count += 1
        output += '\n'
    print(output[0:-1])
            
            