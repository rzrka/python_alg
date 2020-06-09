print(ord('a'))
print(ord('z'))


user_first, user_second = input().split()


print('Место первой буквы: ' + str(ord(user_first) - 96))
print('Место второй буквы: ' + str(ord(user_second) - 96))
if ord(user_second) > ord(user_first):
    print('Между ними ' + str(ord(user_second) - ord(user_first)) + ' букв')
else:
    print('Между ними ' + str((ord(user_second) - ord(user_first))*(-1)) + ' букв')