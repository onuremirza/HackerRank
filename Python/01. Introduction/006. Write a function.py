def is_leap(y):
    leap = False    
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

year = int(input())
print(is_leap(year))