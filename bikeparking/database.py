# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from bikeparking.model import *

class DBManager:
    __engine = None
    __session = None

    @staticmethod
    def init(db_address, db_port, db_id, db_password, db_name, db_log_flag=True):
        DBManager.__engine = create_engine('mysql://' + db_id + ':' + db_password + '@' + db_address + ':' + db_port + '/' + db_name, echo=db_log_flag)
        DBManager.__session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=DBManager.__engine))

        global dao

        dao = DBManager.__session

    @staticmethod
    def init_db():
        from bikeparking.model import Base
        Base.metadata.create_all(bind=DBManager.__engine)

dao = None