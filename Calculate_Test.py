def calculate():
    print("簡易的な電卓です。終了の際は'='をにゅうりょくしてね")
    result = float(input("数値を入力してください"))

    while True:
        operation = ("操作を選択(+, -, /, =):")

        if operation == '=' :
            print(f"計算結果: {result}")
            break
        elif operation in ('+', '-', '*', '/'):
            number = float(input("数値を入力:"))
            
            if operation == '+':
                result += number
            elif operation == '-':
                result -= number
            elif operation == '*':
                result *= number
            elif operation == '/':
                if number != 0:
                    result /= number
                else:
                    print("0では割れません")

                    continue
            else:
                print("無効な操作")

calculate()           