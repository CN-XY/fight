i=0
j=0
import random
import time
class bin():
    def __init__(self,hp,atk):
        self.HP=hp
        self.atk=atk
        self.maxHP=hp
bin1=bin(random.randint(30,60),random.randint(2,5))
bin2=bin(random.randint(20,50),random.randint(1,4))
print("第"+str(random.randint(1,8))+"列，第"+str(random.randint(1,6))+"行的同学被选中成为玩家"
print()
print("————————————————")
print("游戏开始")
print("————————————————")
class xianshi():
    def __init__(self):
        self.a=0
    def xuanze(self):
        self.a=input("选择下一步行动:1.攻击，2.回血，3.查看敌我情况") 
        number=('0','1','2','3','4','5','6','7','8','9')
        for x in self.a:
            if not x in number:
                print("非数字")
                player.xuanze()
                break
            else:
                self.a=int(self.a)
                if self.a==1:
                    i=bin1.atk+random.randint(0,5)
                    if bin2.HP<1:
                        print("你打败了敌人")
                        time.sleep(1)
                    else:
                        j=random.randint(1,5)
                        if j==2:
                            print("对方躲开了你的攻击")
                        else:
                            bin2.HP -= i
                            print("你对敌人造成了"+str(i)+"点伤害")
                elif self.a==2:
                    i=random.randint(5,10)
                    bin1.HP += i           
                    if bin1.HP<1:
                        print("你被打败了")
                        time.sleep(1)
                    else:
                        print("你回复了"+str(i)+"点血")
                elif self.a==3:
                    print("玩家血量："+str(bin1.HP))
                    print("敌人血量："+str(bin2.HP))
                    print("玩家基础攻击力："+str(bin1.atk))
                    print("敌人基础攻击力："+str(bin2.atk))
                    print("玩家生命上限："+str(bin1.maxHP))
                    print("敌人生命上限："+str(bin2.maxHP))
                    time.sleep(0.5)
                    player.xuanze()
    def atk(self):
        i=random.randint(1,2)
        if i == 1:
            i=bin2.atk+random.randint(1,8)
            j=random.randint(1,5)
            if j==2:
                print("你躲开了敌人的攻击")
            else:
                bin1.HP -= i
                print("敌人对你造成了"+str(i)+"点伤害")
        else:
            i=random.randint(5,10)
            bin2.HP += i
            print("敌人回复了"+str(i)+"点血")
player=xianshi()
while True:
    time.sleep(0.5)
    player.xuanze()
    if bin1.HP>bin1.maxHP:
        bin1.HP=bin1.maxHP
    elif bin2.HP>bin2.maxHP:
        bin2.HP=bin2.maxHP
    if bin2.HP<1:
        print("你赢了!:)")
        break
    elif bin1.HP<1:
        print("你输了!:(")
        break
    time.sleep(0.5)
    player.atk()
input("——————游戏结束——————")
