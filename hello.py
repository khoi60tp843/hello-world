wrong_attempts = 0
n = -1  # Khởi tạo một giá trị âm để vào vòng lặp

while wrong_attempts < 5:
    n = float(input("Enter a positive number: "))

    if n > 0:
        print("Success! You entered:", n)
        break  # Đúng rồi thì thoát vòng lặp
    else:
        wrong_attempts = wrong_attempts + 1
        print("Not a positive number!")

if wrong_attempts == 5:
    print("Program terminated. Maximum 5 wrong attempts reached.")