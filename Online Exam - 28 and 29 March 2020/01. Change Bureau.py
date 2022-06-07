bitcoins = int(input())
chinese_uan = float(input())
commission = float(input())

lev = bitcoins * 1168           #leva
dollars = chinese_uan * 0.15
dollars *= 1.76                 #leva
euro = lev + dollars            #leva
euro /= 1.95                    #euro
commission /= 100
commission *= euro

result = euro - commission
print(f'{result:.2f}')