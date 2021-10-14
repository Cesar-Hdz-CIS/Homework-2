user_input = input()

input_list = user_input.split()
print(input_list)

if input_list[0] == 'March':
    print(input_list[0])
elif input_list[0] == 'January':
    print(input_list[0])
else:
    print('wrong')