actions = {'read': 'R', 'write': 'W', 'execute': 'X'}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if actions[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')
