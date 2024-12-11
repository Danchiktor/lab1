RED = '\u001b[41m'
GREEN = '\u001b[42m'
END = '\u001b[0m'
print(f'{YELLOW}{" "*9}{END}')
print(f'{GREEN}{" "*9}{END}')
print(f'{RED}{" "*9}{END}')


print("")

WHITE = '\u001b[47m'
print(f'{RED}{" "*1}{WHITE}{" "*5}{RED}{" "*1}{END}')
print(f'{WHITE}{" "*1}{RED}{" "*1}{WHITE}{" "*3}{RED}{" "*1}{WHITE}{" "*1}{END}')
print(f'{WHITE}{" "*2}{RED}{" "*3}{WHITE}{" "*2}{END}')


plot_list = [[0 for i in range(10)] for i in range(10)]
result_list = [abs(i) for i in range(10)]
print(result_list)

step = abs(result_list[0] - result_list[9]) / 9
for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][0] = step * (8 - i ) + step
# print(step)
for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result_list[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list [i][k + 1] = 1
#
for i in range(9):
    line = ""
    for j in range(10):
        if j == 0:
            line += '\t' + str(plot_list[i][j]) + '\t'
        if plot_list[i][j] == 0:
            line += "--"
        if plot_list[i][j] == 1:
            line += "##"
        # else:
        #     line += "--"
    print(line)
print("        0 1 2 3 4 5 6 7 8 9 ")


file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()
list2=[]

sr_znChet = 0
sr_znNechet = 0
for i in range(len(list)):
    if (i + 1) % 2 == 0:
        sr_znChet += abs(list[i])
    if (i + 1) % 2 == 1:
        sr_znNechet += abs(list[i])
sr_znChet /= 125
sr_znNechet /= 125
print("  Среднее по модулю четных чисел -",str(sr_znChet)[:4],f'{RED}{"  " *round(10*sr_znChet)}{END}')
print("Среднее по модулю нечетных чисел -",str(sr_znNechet)[:4],f'{YELLOW}{"  " *round(10*sr_znNechet)}{END}')