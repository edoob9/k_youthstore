import os

BASE_DIR = os.path.dirname(__file__)
# 상위 경로
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(ROOT_DIR, 'app.db')) # DB 주소 : sqlite:///app.db
SQLALCHEMY_TRACK_MODIFICATION = False # DB event 처리 옵션
