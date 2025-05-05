# 13. Composition Assignment:

class Engine:
  def start(self):
    print("Engine started")

class Car:
  def __init__(self, engine: Engine):
    self.engine = engine

  def start_engine(self):
    self.engine.start()

engine = Engine()
car = Car(engine)
car.start_engine()