from pprint import pprint

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    producer = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

    def __repr__(self):
        return f'{self.product_id}, {self.name}, {self.producer}, {self.category}, {self.price}, {self.stock}'


if __name__ == '__main__':
    eng = create_engine('mysql+pymysql://root:@localhost:3306/magazin', echo=False)
    Session = sessionmaker(bind=eng)
    with Session() as my_session:
        prod = Product(
            product_id='QWESDFRDS',
            name='Formula',
            producer='Formula 1',
            category='masinute',
            price=100,
            stock=40)

        my_session.add(prod)

        res = my_session.query(Product).all()
        pprint(res)

        res = my_session.query(Product).filter_by(category='masinute').all()
        pprint(res)

