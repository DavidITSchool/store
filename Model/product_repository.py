from pprint import pprint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Model.product_domain import Product

from Config.config import DB_USERNAME, DB_PASSWORD, DB_URL


class DBProductRepository:
    def __init__(self):
        print(DB_USERNAME)
        print(DB_PASSWORD)
        print(DB_URL)
        self.engine = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}', echo=False)
        self.session = sessionmaker(bind=self.engine)()

    # CREATE
    def add_product(self, product_id, name, producer, category, price, stock):
        prod = Product(
            product_id=product_id,
            name=name,
            producer=producer,
            category=category,
            price=price,
            stock=stock)

        self.session.add(prod)
        self.session.commit()

    # READ
    def get_product(self, product_id):
        return self.session.query(Product).filter_by(product_id=product_id).first()

    # READ
    def get_all_products(self):
        return self.session.query(Product).all()

    # TODO(andrei): Add update and delete functions


if __name__ == '__main__':
    repo = DBProductRepository()

    pprint(repo.get_all_products())
    # repo.add_product(
    #     product_id='KHSJDHRTF',
    #     name='Whatever',
    #     producer='Whatever Company',
    #     category='puzzle',
    #     price=100,
    #     stock=20
    # )
    pprint(repo.get_product(product_id='KHSJDHRTF'))
