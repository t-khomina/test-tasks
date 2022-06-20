# Верните список, содержащий результат обхода квадратной матрицы по спирали: против часовой стрелки, начиная с верхнего левого угла.
# На вход подаётся размер матрицы, за которым следуют разделённые пробелами строки матрицы.
# Размерность матрицы больше 0.
n = int(input()) 
a = []
for i in range(n):
    row = input().split()
    for i in range(n):
        row[i] = int(row[i])
    a.append(row)
list = []
k = 0
i = 0
j = 0
while True:
    for i in range(k, n-k):
        list.append(a[i][j])
    for j in range(k + 1, n-k):
        list.append(a[i][j])
    #n = n - 1
    for i in range(n-2-k, k-1, -1):
        list.append(a[i][j])
    for j in range(n-2-k, k, -1):
        list.append(a[i][j])
    k = k + 1
    #print(list, 'k =', k)
    if k >= n:
        #print('Цикл окончен, k =', k)
        break
print(*list)
