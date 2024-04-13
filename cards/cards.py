from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from orm.icv_orm import Base, engine, Session

# 定义Card对象:
class Card(Base):
    __tablename__ = 'cards'
    id = Column(String(255), primary_key=True,nullable=False)
    raw = Column(String(255),nullable=False)
    r_num = Column(String(255),nullable=False)
    r_ide=Column(String(255),nullable=False)
    r_type=Column(String(255),nullable=False)
    inter_range=Column(String(255),nullable=False)
    over_range=Column(String(255),nullable=False)
    park_range=Column(String(255),nullable=False)
    char_range=Column(String(255),nullable=False)
    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# 创建数据表
Base.metadata.create_all(engine)
# 创建Card对象的操作
def create_card(id, raw, r_num, r_ide, r_type, inter_range, over_range, park_range, char_range):
    session = Session()
    new_card = Card(id=id, raw=raw, r_num=r_num, r_ide=r_ide, r_type=r_type, inter_range=inter_range,over_range=over_range, park_range=park_range, char_range=char_range)
    session.add(new_card)
    session.commit()
    session.close()
    
def get_card(id):
    session = Session()
    card = session.query(Card).filter_by(id=id).first()
    session.close()
    return card

def get_all_cards():
    session = Session()
    cards = session.query(Card).all()
    session.close()
    return cards

def update_card(id, raw, r_num, r_ide, r_type, inter_range, over_range, park_range, char_range):
    session = Session()
    card = session.query(Card).filter_by(id=id).first()
    card.raw = raw
    card.r_num = r_num
    card.r_ide = r_ide
    card.r_type = r_type
    card.inter_range = inter_range
    card.over_range = over_range
    card.park_range = park_range
    card.char_range = char_range
    session.commit()

        
def delete_card(id):
    session = Session()
    card = session.query(Card).filter_by(id=id).first()
    session.delete(card)
    session.commit()
    session.close()