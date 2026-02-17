try:
    print("   ========欢迎使用成绩判断程序========")
    print("        <<<<<<<<<离线模式>>>>>>>>>")
    name=(input("请输入用户名："))
    print(f"欢迎用户<{name}>")
    score = float (input("请输入成绩:"))
    if not(0 <=score<= 100):
        print("成绩仅支持0~100")    
    #level识别变量
    if score >= 90:
             level = "成绩优秀(A)" 
    elif score >= 80:
             level = "成绩良好(B)"
    elif score >= 70:
             level = "成绩勉强(C)"
    else:
             level = "有待提升(D)"
#成绩单
    print("========成绩单========")         
    print(f"用户名：{name}")
    print(f"成绩: {score}")    
    print(f"判断结果：{level}")
    print(f"祝用户「{name}」学有所成")
except ValueError:
    print("值错误，请重试")
        
         