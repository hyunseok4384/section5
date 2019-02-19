import sys
import io
import simplejson as json
from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#파일 DB 생성
db = TinyDB(r'C:\section5\databases\database1.db')

#db.insert({'name':'kim', 'email':'test1@daum.net'}) #json(dict)
#db.insert_multiple([{'name':'lee', 'email':'test2@daum.net'},{'name':'park', 'email':'test3@daum.net'}]) #jsonArray(dict)[{},{},{}]

SQL = Query()

el = db.get(SQL.name == 'kim')

#id 값 출력
#print(el)
#print(el.doc_id) #다큐먼트 ID출력(TinyDB에서 자동적으로 시퀀스 넘버 만들어준다)

#데이터 수정
#db.update({'email':'test1@google.com'}, doc_ids=[1,3])

#데이터 수정 및 추가
#db.upsert({'email':'test1@naver.com', 'login':True}, SQL.name == 'park') #update + insert

#데이터 삭제
#db.remove(doc_ids=[1,3])
#db.remove(SQL.name == 'park')

#전체 조회
print(db.all())
