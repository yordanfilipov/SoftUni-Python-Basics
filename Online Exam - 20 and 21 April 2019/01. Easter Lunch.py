easter_breads = int(input())
egg_crunches = int(input())
cookies_kg = int(input())

easter_bread = 3.20
eggs = 4.35 + (12 * 0.15)
cookies = 5.40
egg_color = 0.15

easter_breads *= easter_bread   #add to sum
cookies *= cookies_kg           #add to sum
egg_crunches *= eggs            #add

sum = easter_breads + cookies + egg_crunches

print(f'{sum:.2f}')