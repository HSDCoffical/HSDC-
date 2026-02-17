#用户输入值，反馈至本地
import datetime
name=input("请输入用户名：")
print(f"欢迎'{name}'参与本次测试")
print(f"剧情虚构，如果试玩期间有任何不适请立即停止")
#时间戳
start_time=datetime.datetime.now()
print(f"游戏启动时间:{start_time.strftime('%Y-%m-%d %H：%M:%S')}")
#密码设置
CORRECT_PASSWORD = ("0205","0206","0207","0208","0209")
password = input("请输入本次测试的激活码:")
#验证激活码
if password not in CORRECT_PASSWORD:
    print("激活码错误，感谢您的支持，但十分抱歉，请关注下一次测试") 
    exit()

#开始运行剧情板块，用户可根据需要进行跳过
story = {
"第一年":"你出生在一个小县城里，你的父母对你十分喜欢，并且你拥有了第一个名字[小顺]，寓意顺顺利利", 
"第七年":"你步入了小学一年级，并且在很多方面独立，但是父母因为不合离了婚，你进入了孤儿院",  
"第十三年":"你步入了初中，成绩也一落千丈，你开始意识到自己的的不足",
"第十五年":"你开始意识到一切都是重复，并不断的抵触",
"第十八年":"高中的最后一年，你结束了十二年的学习，步入了大学，并且结束了孤儿院的生活",
"第二十五年":"你在工作期间认识到了一个女孩，你们不断的深入，直到结婚",
"第二十九年":"你的妻子怀孕了，这一年，诞生了一条生命，同时，失去了一条生命，妻子因难产而死，但同时你有了一个女儿",
"第三十五年":"你的孩子开了家长会，你的孩子第一次向你问了一个问题'爸爸，妈妈呢？'你开始惭愧",
"第四十七年":"你的孩子成年了，第一次因为'母亲'的问题与你争吵，孩子不断的哭泣，你的心里很不是滋味",
"第五十一年":"你的孩子大学毕业了，去了外地工作，并且开始重视你了",
"第五十三年":"你在一次家务时吐了一口血，你刚开始没有在意，但是病情越来越严重，你去了医院，你的生命进入了倒计时，但是你并没有告诉孩子",
"第五十四年":"你的身体开始越来越瘦，你知道时间不久了，你继续选择隐瞒，女儿打来的电话你总是说没事，工作为主",
"第五十五年":"刚过完年，女儿已经回外地了，一天下午，你躺在阳台，夕阳和云朵很美，你叹息了一下，并且开始微笑，慢慢闭上了眼，你体验了走马灯，并结束了这一生",
"结尾":"你在前一天将存款全部打给了女儿，并且告诉她一定要照顾好自己，我很健康，你留给女儿一封信在一个不起眼的桌子上，至此，你托举了女儿，结束了自己",
"声明":"感谢您参与测试，帮助我们在后续的开发中不断的改进"
}
story_keys = list(story.keys())
current_index = 0#顺序推进剧情
def show_story(key):
    """显示指定剧情内容"""
    print(f"\n====={key}=====")
    print(story[key])
    input("\n按回车继续进程")
while True:
    #推进方式选择部分
    while True:
        choice = input(f"\n请'{name}'选择推进方式：1.顺序推进 2.自由预览 3.退出游戏\n")   
        if choice in ["1","2","3"]: 
            break
        print("输入错误，值不在准许范围之内")  
    if choice =="1":
        #顺序推进
        while current_index < len(story_keys):
            show_story(story_keys[current_index])
            current_index += 1
            #回车会继续进程，并且保证用户可在此期间自行切换
            next_step=("\n按回车继续进程，输入'2'切换为自由预览，输入'3'退出游戏\n")
            if next_step =="2":
            #切换为自由预览
                pass
            elif next_step =="3":  
                print("游戏结束，感谢您参与本次测试")
                break
                
        else:
            print("\n剧情已全部结束，感谢您的游玩测试")
            break
    elif choice =="2":
        #自由预览
        while True:
            print("\n仅可选择以下剧情进行推进:","、".join(story_keys)) 
            user_choice = input("请输入您想查看的剧情年份(如'第一年'):")
            if user_choice in story:
                show_story(user_choice)
                current_index=story_keys.index(user_choice)+1
                #用户输入回车后优先弹出自由预览选项
                preview_choice=input("回车继续(输入退出返回主界面)：")
                if preview_choice  =='退出':
                    break   
            else:
                print(f"输入的值不在检索范围内，请重试")    
 #更新当前的检索对象，保证后续推进的连续性
        else:
            print(f"检索值无效，请重新输入，只能输入:{','.join(story_keys)}")
 #结束目录，感谢用户参与第一次测试     
    elif choice == "3":
            print("游戏结束，感谢您参与本次测试") 
            break
else:
        print("输入无效，请输入1,2或3之类的数值")     