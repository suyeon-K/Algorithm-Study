N, K = map(int, input().split())

coins_list = []

for _ in range(N):
    n = int(input())
    if n <= K:
        coins_list.append(n)

def calc_coin(i, coins_list, charge_money):
    if i == -1:
        return 0
    coin_cnt = charge_money//coins_list[i]
    return coin_cnt + calc_coin(i-1, coins_list, charge_money%coins_list[i])

print(calc_coin(len(coins_list)-1, coins_list, K))