"""
 Полиморфизм - Это механизм, позволяющий выполнить один и тот же код по-разному.
 Duck-typing (утиная типизация) - Наличие поведения для использования в полиморфизме.
 В ЯП со статической типизацией для полиморфизма важно кто ты (какой тип), для python важно что ты умеешь (поведение).
"""


class SQLiteDatabase:
    def connect(self):
        print("Connecting to database SQLiteDatabase")

    def get_users(self):
        print("get user with SQL")


class MongoDatabase:
    def connect(self):
        print("Connecting to database MongoDatabase")

    def get_users(self):
        print("get user with NoSQL")


class Server:
    def get_users(self, db):
        db.connect()
        users = db.get_users()
        return users


def get_db_from_config():
    print("read config")
    return SQLiteDatabase()


if __name__ == '__main__':
    server = Server()
    server.get_users(get_db_from_config())
    print("---------------------------------------------")


class Animal:
    def make_noise(self):
        print("shh")


class Cat(Animal):
    def make_noise(self):
        print("meow")


class Dog(Animal):

    def make_noise(self):
        print("gavvv")


class Car:
    def make_noise(self):
        print("bi-bi")


def noise(animal):
    animal.make_noise()  # Что умеет: Make_noise


if __name__ == '__main__':
    noise(Car())
