f_users = 'users.txt' #"""d:\\tutorials\\python\\barantcev-training\\barantcev-training\\Learn Python Book\\users.txt"""

print('Hi. What is you name?')
user_name = input()
print('Hi. What is you hobby?')
user_hobby = input()

try:
    with open(f_users) as f_obj:
        lines = f_obj.readlines()
        last_string = lines[len(lines) - 1]
        id = int(last_string.split()[0])
        with open(f_users, 'a') as f_obj:
            f_obj.write(str(id + 1) + ' Name: ' + user_name.title() + ' Hobby: ' + user_hobby.title() + '\n')
except:
    with open(f_users, 'w') as f_obj:
        f_obj.write(str(1) + ' Name: ' + user_name.title() + ' Hobby: ' + user_hobby.title() + '\n')

