import time
import string

# def my_age(birth_year):
#     this_year = int(time.strftime("%Y"))
#     age = this_year-birth_year
#     return age
# print(my_age(2009))

# dig = input('Enter number:')
def count_digits(a):
    sum = 0
    for s in range(10):
        sum += a.count(str(s))
    return sum
ans = count_digits('applep5e')
print(ans)

def count_punctuation(word):
    sum = 0
    if len(word) > len(string.punctuation):
        for cha in string.punctuation:
            sum += word.count(cha)

    else:
        for char in word:
            if char in string.punctuation:
                sum +=1
    return sum
print(count_punctuation("..+ghh]"))

def valid_password(a):
    b = len(a)>7
    c = count_digits(a) > 0
    d = count_punctuation(a) >0

    result = dict()

    result['is_valid'] = b and c and d
    if result['is_valid']:
        message = "Your password is valid"
    else:
        message = "Your password is not valid"
    result['errors'] = []

    if not b:
        result['errors'].append('Your password should have at least 8 character')

    if not c:
        result['errors'].append('Your password should have at least 1 number')

    if not d:
        result['errors'].append('Your password should have at least 1 special character')

    return result
print(valid_password('Aer2lkj/hg'))