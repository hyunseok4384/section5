import sys
import io
from tinydb import TinyDB, Query, where
import simplejson as json
import urllib.request as req
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

savename1 = r"C:\section5\data\photos.json"
savename2 = r"C:\section5\data\comments.json"
url1 = "https://jsonplaceholder.typicode.com/photos"
url2 = "https://jsonplaceholder.typicode.com/comments"

if not os.path.exists(savename1):
    req.urlretrieve(url1,savename1)
if not os.path.exists(savename2):
    req.urlretrieve(url2, savename2)

db = TinyDB(r"C:\section5\databases\examdb1.db")

photos = db.table("photos")
comments = db.table("comments")

with open(r"C:\section5\data\photos.json","r") as f:
    r = json.loads(f.read())
    for i in r:
        photos.insert(i)

with open(r"C:\section5\data\comments.json","r") as f:
    t = json.loads(f.read())
    for j in t:
        comments.insert(j)

for photo in photos:
    print("[",photo['title'],"]")
    print("[",photo['url'],"]")
    for com in comments:
        if com['id'] == photo['id']:
            print('comments : ',com['body'])
