from generated_code.demo import addressbook_nested_pb2


def person_demo():
    person = addressbook_nested_pb2.Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_nested_pb2.Person.HOME
    food = person.favorites.add()
    food.name = "burger"
    food.calories = 1000
    food_2 = person.favorites.add()
    food_2.name = "fries"
    food_2.calories = 1000

    serialized_data = person.SerializeToString()
    assert type(serialized_data) == bytes
    assert serialized_data == b'\n\x08John Doe\x10\xd2\t\x1a\x10jdoe@example.com"\x0c\n\x08555-4321\x10\x01*\x0b\n\x06burger\x10\xe8\x07*\n\n\x05fries\x10\xe8\x07'

    deserialized_person = addressbook_nested_pb2.Person()
    deserialized_person.ParseFromString(serialized_data)

    assert deserialized_person.name == "John Doe"
    assert deserialized_person.email == "jdoe@example.com"
    assert len(deserialized_person.phones) == 1
    assert deserialized_person.phones[0].number == "555-4321"
    assert deserialized_person.phones[0].type == addressbook_nested_pb2.Person.HOME
    assert len(deserialized_person.favorites) == 2
    assert deserialized_person.favorites[0].name == "burger"
    assert deserialized_person.favorites[0].calories == 1000
    assert deserialized_person.favorites[1].name == "fries"
    assert deserialized_person.favorites[1].calories == 1000


if __name__ == "__main__":
    person_demo()