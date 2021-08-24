a = [str(i) for i in range(10)]
a.extend([chr(i) for i in range(65,90+1)])
n = [i for i in range(35+1)]

dic = dict(zip(a,n))
dic_re = dict(zip(n,a))


def N_to_decimal(num, N, c, dic):

    if c == 0:
        return dic[num[0]]

    return dic[num[0]]*(N**c) + N_to_decimal(num[1:], N, c-1, dic)


def decimal_to_N(num, N, dic_re):

    if num // N == 0:
        return str(dic_re[num%N])

    return decimal_to_N(num//N, N, dic_re) + str(dic_re[num%N])


def decimal_to_N_for(num, N):
    d = []
    x = int(num)
    while(True):
        d.append(dic_re[x % N])
        x = x // N
        if x == 0:
            break
    
    d = d[::-1]
    d = "".join(d)
    return d



# num, N = input().split()
# N = int(N)

# print(N_to_decimal(num, N, len(num)-1, dic))

num, B = map(int,input().split())

print(decimal_to_N(num, B, dic_re))