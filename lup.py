def answer_lup(b, l, u, p, n):
    b_new = [0 for i in range(n)]

    for i in range(n):
        '''Преобразовываем b с помощью матрицы перестановок'''
        sum = 0
        for j in range(n):
            sum += p[i][j]*b[j]
        b_new[i] = sum

    y = []
    for i in range(n):
        '''Считаем y'''
        sum = 0
        for j in range(i):
            sum += l[i][j]*y[j]
        y.append((b_new[i] - sum)/l[i][i])        # обязательно ли делить?

    x = [0 for i in range(n)]

    for i in range(n-1,-1,-1):
        '''Считаем вектор-ответ'''
        sum = 0
        for j in range(i, n):
            sum += u[i][j]*x[j]
        x[i] = round(((y[i] - sum)/u[i][i]), 6)

    return x

def lup(arr, b, n):
    p = []
    for i in range(n):
        p.append([])
        for j in range(n):
            p[i].append(0)
        p[i][i] = 1
    for i in range(n):

        a_i_max = abs(arr[i][i])
        h = i

        for j in range(i, n):
            '''Находим ведущий элемент'''
            if abs(arr[j][i]) > a_i_max:
                a_i_max = abs(arr[j][i])
                h = j
        '''Переставляем i-ю строку со сторой, к которой нашли ведущий элемент'''
        arr[i], arr[h] = arr[h], arr[i]
        p[i], p[h] = p[h], p[i]

        for j in range(i+1, n):
            '''Преобразовываем матрицу'''
            arr[j][i] = arr[j][i]/arr[i][i]
            for k in range(i+1, n):
                arr[j][k] -= arr[j][i]*arr[i][k]

    for i in range(n):
        '''Находим L + U'''
        arr[i][i] += 1

    l = []
    u = []
    for i in range(n):
        l.append([])
        u.append([])
        for j in range(n):
            l[i].append(0)
            u[i].append(0)

    for i in range(n):
        '''Находим L'''
        l[i][i] = 1
        for j in range(i):
            l[i][j] = arr[i][j]
    for i in range(n):
        '''Находим U'''
        for j in range(n):
            u[i][j] = arr[i][j] - l[i][j]

    return answer_lup(b, l, u, p, n)