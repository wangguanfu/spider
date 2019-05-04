from peewee import *

db = MySQLDatabase("spider", host="localhost", port=3306,
                   user="root", password='root')


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db
        table_name = "persons"  # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


if __name__ == '__main__':
    db.create_tables([Pet])

    # 数据的怎删改查
    from datetime import date

    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
    uncle_bob.save()  # bob is now stored in the database

    grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
    herb = Person.create(name='Herb', birthday=date(1950, 5, 5))

    grand = Person.get(Person.name == 'Grandma')
    print(grand.name)

    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

    query = (Pet
             .select(Pet, Person)
             .join(Person)
             .where(Pet.animal_type == 'cat'))

    for pet in query:
        print(pet.name, pet.owner.name)

