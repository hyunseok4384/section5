import sys
import io
import simplejson as json
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#파일 DB 생성
db = TinyDB(r'C:\section5\databases\database.db',default_table='users')

#메모리 DB 생성
#db = TinyDB(storages=MemoryStorage, default_table='users')

#테이블 선택
users = db.table("users")
todos = db.table("todos")

#테이블 데이터 삽입
#users.insert({'name':'kim', 'email':'test@google.com'})
#todos.insert({'name':'homework', 'complete':False})


#테이블 데이터 전체 삽입1
with open(r'C:\section5\data\users.json','r') as infile:
    r = json.loads(infile.read())
    for u in r:
        users.insert(u)

#테이블 데이터 전체 삽입2
with open(r'C:\section5\data\todos.json','r') as infile:
    r = json.loads(infile.read())
    for t in r:
        todos.insert(t)


#전체 데이터 출력
print(users.all())
print(todos.all())

#테이블 목록
print(db.tables())

#전체 데이터 삭제
#users.purge() #db.purge_table('users')
#todos.purge() #db.purge_table('todos')

#깔끔하게 다 지우기(테이블까지 다 지워짐)
#db.purge_tables()

db.close()
