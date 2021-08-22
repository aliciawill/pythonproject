# python과 mysql연결해주는 라이브러리가 필요
import pymysql as my

def select_all():
    #python과 mysql을 연결하여 통로에 해당하는 부품을 가지고 온다.
    #con부품을 통해 db완 관련된 여러 처리를 할 수 있음.
    con = my.connect(host="localhost", user='root', password='1234', db='shoes')
    print(con.host)
    print(con.host_info)

    #cursor: 연결 통로를 통해 SQL문이나, 검색된 데이터를 전달할 때
    #연결 통로의 SQL,데이터를 가르키면서 실행을 하거나 꺼내올 수 있는 부품.
    cursor = con.cursor()
    print(cursor)

    #sql문을 만들어보자.
    sql = "select * from member"
        # select * from member

    #sql문을 mysql에 전송
    result = cursor.execute(sql)
    print('sql문 실행 요청됨!!!')
    print('result의 값은 ', result)

    records = cursor.fetchall()
    print('record의 값은 ', records)


    con.commit() #insert된 것을 반영!!
    con.close() #python과 mysql연결을 끊는다.
    return records

def select(id):
    #python과 mysql을 연결하여 통로에 해당하는 부품을 가지고 온다.
    #con부품을 통해 db완 관련된 여러 처리를 할 수 있음.
    con = my.connect(host="localhost", user='root', password='1234', db='shoes')
    print(con.host)
    print(con.host_info)

    #cursor: 연결 통로를 통해 SQL문이나, 검색된 데이터를 전달할 때
    #연결 통로의 SQL,데이터를 가르키면서 실행을 하거나 꺼내올 수 있는 부품.
    cursor = con.cursor()
    print(cursor)

    #sql문을 만들어보자.
    sql = "select * from member where id = '" + id + "'"
        # select * from member where id = '100'

    #sql문을 mysql에 전송
    result = cursor.execute(sql)
    print('sql문 실행 요청됨!!!')
    print('result의 값은 ', result)

    record = cursor.fetchone()
    print('record의 값은 ', record)


    con.commit() #insert된 것을 반영!!
    con.close() #python과 mysql연결을 끊는다.
    return record

def update(id, tel):
    #python과 mysql을 연결하여 통로에 해당하는 부품을 가지고 온다.
    #con부품을 통해 db완 관련된 여러 처리를 할 수 있음.
    con = my.connect(host="localhost", user='root', password='1234', db='shoes')
    print(con.host)
    print(con.host_info)

    #cursor: 연결 통로를 통해 SQL문이나, 검색된 데이터를 전달할 때
    #연결 통로의 SQL,데이터를 가르키면서 실행을 하거나 꺼내올 수 있는 부품.
    cursor = con.cursor()
    print(cursor)

    #sql문을 만들어보자.
    sql = "update member set tel = '" + tel + "' where id = '" + id + "'"
        # update member set tel = '888' where id = 'apple'

    #sql문을 mysql에 전송
    cursor.execute(sql)
    print('sql문 실행 요청됨!!!')

    con.commit() #insert된 것을 반영!!
    con.close() #python과 mysql연결을 끊는다.


def delete(id):
    #python과 mysql을 연결하여 통로에 해당하는 부품을 가지고 온다.
    #con부품을 통해 db완 관련된 여러 처리를 할 수 있음.
    con = my.connect(host="localhost", user='root', password='1234', db='shoes')
    print(con.host)
    print(con.host_info)

    #cursor: 연결 통로를 통해 SQL문이나, 검색된 데이터를 전달할 때
    #연결 통로의 SQL,데이터를 가르키면서 실행을 하거나 꺼내올 수 있는 부품.
    cursor = con.cursor()
    print(cursor)

    #sql문을 만들어보자.
    sql = "delete from member where id = '" + id + "'"
        # delete from member where id = '100'

    #sql문을 mysql에 전송
    cursor.execute(sql)
    print('sql문 실행 요청됨!!!')

    con.commit() #insert된 것을 반영!!
    con.close() #python과 mysql연결을 끊는다.

def insert(id, pw, name, tel):
    #python과 mysql을 연결하여 통로에 해당하는 부품을 가지고 온다.
    #con부품을 통해 db완 관련된 여러 처리를 할 수 있음.
    con = my.connect(host="localhost", user='root', password='1234', db='shoes')
    print(con.host)
    print(con.host_info)

    #cursor: 연결 통로를 통해 SQL문이나, 검색된 데이터를 전달할 때
    #연결 통로의 SQL,데이터를 가르키면서 실행을 하거나 꺼내올 수 있는 부품.
    cursor = con.cursor()
    print(cursor)

    #sql문을 만들어보자.
    sql = "insert into member values ('"+ id + "', '" + pw + "', '" + name + "', '"+ tel + "')"
        # insert into member values ('root', '1234', 'root', '019')

    #sql문을 mysql에 전송
    cursor.execute(sql)
    print('sql문 실행 요청됨!!!')

    con.commit() #insert된 것을 반영!!
    con.close() #python과 mysql연결을 끊는다.


