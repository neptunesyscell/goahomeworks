
# 1) შექმენით სია და დაპრინტეთ სიგრძე
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(my_list))  # სიის სიგრძე გამოიტანს 10-ს

# 2) სიაზე გადავლა for loop-ით
for i in range(len(my_list)):
    print(my_list[i])  # სიის თითოეული ელემენტი გამოიტანს ინდექსით

# 3) .append ფუნქციის გამოყენება
my_list.append(11)  # 11 დაემატება სიის ბოლოს
my_list.append(12)  # 12 დაემატება სიის ბოლოს
print(my_list)  # საბოლოო სია: [1, 2, 3, ..., 10, 11, 12]

# 4) for loop-ით სიაში დამატება
new_list = []
for i in range(5):
    new_list.append(i)  # ცვლადი i ემატება სიას ყოველ ჩაკრავს
print(new_list)  # საბოლოო სია: [0, 1, 2, 3, 4]
