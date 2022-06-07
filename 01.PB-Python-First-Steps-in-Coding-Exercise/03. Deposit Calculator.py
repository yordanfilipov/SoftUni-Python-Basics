deposit = float(input())
session = int(input())
yearly_Percent = float(input())

increase = deposit * (yearly_Percent / 100)
monthly_Increase = increase / 12
sum = deposit + (session * monthly_Increase)

print(sum)
