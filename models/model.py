from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 전역변수로 선언한 이유 -> 다른 모듈에서 불러다가 사용하려고
db = SQLAlchemy()

class SampleMyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_date = db.Column(db.DateTime(), nullable=False) # 생성 일자를 null값 허용해야할지 고민

    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.created_date = datetime.datetime.now()


    @property
    # @property 붙여서 함수지만 변수 참조할 때처럼 사용 가능하게
    def serialize(self):  # DB row-> debug -> .json format
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_date': self.created_date
        }

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file_name = db.Column(db.String(128), nullable=False)
    image_path = db.Column(db.String(128), nullable=False)
    up_date = db.Column(db.DateTime(), nullable=False)
    # https://velog.io/@inourbubble2/SQLAlchemy%EC%9D%98-backref%EC%99%80-backpopulates%EC%9D%98-%EC%B0%A8%EC%9D%B4
    result = db.relationship('Result', backref='result', uselist=Ture) # (image:result)one to many relation
    # db.relationship를 사용하는데 실제 db에 나타나는 필드는 아니다
    # db.relationship의 첫 번째 인자는 db.ForeignKey와는 다르게 객체 이름
    # backref는 Posts 객체에 삽입되는 가상 필드 이름

# image table -> DL -> result
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # primary key
    prob = db.Column(db.String(50))
    pred_class = db.Column(db.String(50))
    created_date = db.Column(db.DateTime(), nullable=False)

    image_id = db.Column(db.Integer,
                     db.ForeignKey(Image.id, ondelete='CASCADE'))  # 자동삭제 연동설정 적용

'''
참조할 때 backref = 'result, result_heatmap' 두개를 설정할 수 있는가?
class Result_heatmap(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # primary key
    prob = db.Column(db.String(50))
    pred_class = db.Column(db.String(50))
    created_date = db.Column(db.DateTime(), nullable=False)
    image_id = db.Column(db.Integer,
                     db.ForeignKey(Image.id, ondelete='CASCADE'))  # 자동삭제 연동설정 적용
'''