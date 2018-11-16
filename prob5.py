file_name = input('Enter artwork filename: ')
with open(file_name) as art:
    lines = art.readlines()
    output = ''
    for line in lines:
        for i in range(0, len(line) - 1, 2):
            for j in range(int(line[i])):
                output += line[i+1]
        output += '\n'
    print(output[0:-1])