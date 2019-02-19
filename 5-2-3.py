import sys
import io
import simplejson as json
from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#파일 DB 생성
db = TinyDB(r'C:\section5\databases\database.db',default_table='users')

#테이블 선택
users = db.table("users")
todos = db.table("todos")

Users = Query()
Todos = Query()

#Users 여러가지 조회 방법
print(users.search(Users.id == 7))
print(users.search(Users['id'] == 7))
print(users.search(where('id') == 7))
print(users.search(Query()['id'] == 7))
print(users.search(where('address')['zipcode'] == '92998-3874')) #where의 반환이 딕셔너리
print(users.search(where('address').zipcode == '92998-3874'))

#고급 쿼리
print(users.search(Users.email.exists())) #email있는거 다 가지고 옴
print(users.search(Users['email'].exists()))
print(users.search(Users.aaa.exists()))

#Not
print('not', users.search(~(Users.username == 'Bret'))) #'Bret'이름을 제외한 나머지가 출력

#OR
print('or', users.search((Users.username == 'Bret') | (Users.username == 'Antonette'))) #'Bret''Antonette'출력

#AND
print('and', users.search((Users.username == 'Bret') & (Users.id == 1)))

#기타 함수
print('len', len(users))
print('len', len(todos))

print('contains', users.contains(Users.username == 'Bret')) #있는지 없는지 여기서는 True
print('count', users.count(Users.username == 'Bret')) #몇개 있는지 여기서는 1
