# 支持中文符号的简易计算器
print(" Python计算器")
print(" 欢迎用户，q回车注销")
print(" 当前：离线模式，未接入云端")
while True:
    # 获取用户输入
    user_input = input("\n 输入算式：").strip()
    
    # 输入q则退出程序
    if user_input.lower() == 'q':
        print(" 计算机已注销")
        break
    
    # 把中文符号替换成Python可识别的运算符
    expr = user_input.replace("×", "*").replace("÷", "/")
    
    try:
        # 计算并保留两位小数
        result = eval(expr)
        print(f" 结果：{user_input} = {result:.2f}")
    except ZeroDivisionError:
        print(" 除数不能为0")
    except:
        print(" 请输入有效的算式")
        