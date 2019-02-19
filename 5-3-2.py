import sqlite3

#DB 생성
conn = sqlite3.connect(r'C:\section5\databases\sqlite1.db') #isolation_level=None : AutoCommit

#커서 바인딩
c = conn.cursor()

#데이터 조회(전체)
c.execute("SELECT * FROM users")

#1개 로우 선택
#print(c.fetchone()) #처음 출력이기 때문에 제일 위의 로우를 출력하고 2번 로우를 가리킴

#지정 로우 선택
#print(c.fetchmany(size=4)) #2번로우 부터 4개의 로우가 출력되고 커서는 6번 로우를 가리킴

#전체 로우 선택
#print(c.fetchall())
#print(c.fetchone()) #로우의 끝까지 갔기 때문에 None이 출력된다

#순회1
#rows = c.fetchall()
#for row in rows:
#    print('usage1 > ',row)

#순회2
#for row in c.fetchall():
#    print('usage2 > ',row)

#순회3
#for row in c.execute("SELECT * FROM users"):
#    print('usage3 > ',row)

#조건 조회1
param1 = (1,)
c.execute("SELECT * FROM users WHERE id=?", param1)
print(c.fetchall())

#조건 조회2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" %param2) #%s, %d, %f, %o
print(c.fetchall())

#조건 조회3
c.execute("SELECT * FROM users WHERE id=:id",{"id":1})
print(c.fetchall())

#조건 조회4
param4 = (1,4)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print(c.fetchall())

#조건 조회5
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2",{"id1":1,"id2":4})
print(c.fetchall())

#dump
with conn:
    #dump 출력
    with open(r'C:\section5\data\test.dump','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' %line)
        print("Dump Write Complete!")
