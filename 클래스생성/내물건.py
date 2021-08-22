#사용할 부품을 찍어낼 틀을 만들자(class)
#class 대문자로시작이름:
class Phone:
    #self는 해당 클래스(Phone)의 기능이다.
    #전화기 틀로 찍어낼 전화기 객체가 하는 역할을 함수로 정의한다.
    def text_send(self):
        print('문자를 보내다.')

    def internet(self):
        print('인터넷 하다.')

    def game_fun(self):
        print('재미있는 게임을 하다.')

#틀로 객체를 찍어내보자. 전화기를 만들어봅시다. 내폰, 엄마폰 2개
#변수명 = 클래스이름()
#변수명 == 객체

class Tv:
    def on(self):
        print('켜다')

    def off(self):
        print('끄다')

    def change_ch(self, name, no):
        print(name + '이/가 ' + str(no) + '번 채널로 바꾸다')
        

if __name__ == '__main__':
    my_phone = Phone() #내폰
    mom_phone = Phone() #엄마폰

    my_phone.game_fun() #.은 접근연산자
    mom_phone.text_send()

    tv1 = Tv()
    tv2 = Tv()

    tv1.on()
    tv2.off()
