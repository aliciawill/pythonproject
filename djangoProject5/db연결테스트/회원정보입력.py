import mySQL연결 as my2

if __name__ == '__main__':
    # id = input('아이디 입력>> ')
    # pw = input('패스워드 입력>> ')
    # name = input('이름 입력>> ')
    # tel = input('전화번호 입력>> ')

    # my2.insert(id, pw, name, tel)
    # my2.delete(id)
    # my2.update(id, tel)
    # record = my2.select(id)
    #record에는 DB에서 검색한 하나의 행이 들어있음.
    records = my2.select_all()

    #for-each
    for record in records:
        print('받은 id는 ', record[0])
        print('받은 pw는 ', record[1])
        print('받은 name은 ', record[2])
        print('받은 tel은 ', record[3])
        print('----------------------')