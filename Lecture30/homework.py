from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = 'localhost' # 127.0.0.1
port = '5432'
user = 'postgres'
password = 'password'
database = 'newdb'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer, nullable=True)

    def __init__(self, name, price, quantity_in_stock):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock


class CartItems(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(Float, nullable=True)

    def __init__(self, order_date, total_amount):
        self.order_date = order_date
        self.total_amount = total_amount

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_item = Column(Integer, ForeignKey('product.id'), nullable=False)

    def __init__(self, order_id, product_id, quantity, price_per_item):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price_per_item = price_per_item

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()




