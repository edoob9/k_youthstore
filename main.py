from flask import Flask
from models import model
from common import config

def create_app():
    app = Flask(__name__)

    from controller import main_controller
    from controller import deeplearning_controller
    from controller import db_controller

    app.register_blueprint(main_controller.bp)
    app.register_blueprint(deeplearning_controller.bp)
    app.register_blueprint(db_controller.bp)

    return app


# 데이터베이스 연동 및 테이블 생성
def set_database(app):
    app.config.from_object(config) # 시스템 설정파일에서 DB 설정에 대해서 정의해준 파일 config.py를 이용
    db = model.db
    db.init_app(app)    # DB 생성 -> sqlalchemy를 app에 적용
    db.app = app        # DB 와 flask app 연동
    db.create_all()     # DB 없으면 새로 생성

    return app


if __name__ == '__main__':
    app = create_app()
    app = set_database(app)
    app.run(host='0.0.0.0', port=8888, debug=True)  # debug=True : 소스코드를 변경 자동으로 감지 Flask서버 재시작
