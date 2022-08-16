from calendar import isleap
def is_leap(year):
    leap = False
    if isleap(year):
        leap = True
    return leap
year = int(input(''))
print(is_leap(year))