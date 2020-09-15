from generated_code.demo import addressbook_syntax_proto3_pb2


def person_demo():
    person = addressbook_syntax_proto3_pb2.Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_syntax_proto3_pb2.Person.HOME

    serialized_data = person.SerializeToString()
    assert type(serialized_data) == bytes
    assert serialized_data == b'\n\x08John Doe\x10\xd2\t\x1a\x10jdoe@example.com"\x0c\n\x08555-4321\x10\x01'

    deserialized_person = addressbook_syntax_proto3_pb2.Person()
    deserialized_person.ParseFromString(serialized_data)

    assert deserialized_person.name == "John Doe"
    assert deserialized_person.email == "jdoe@example.com"
    assert len(deserialized_person.phones) == 1
    assert deserialized_person.phones[0].number == "555-4321"
    assert deserialized_person.phones[0].type == addressbook_syntax_proto3_pb2.Person.HOME


def addressbook_demo():
    address_book = addressbook_syntax_proto3_pb2.AddressBook()

    person_john = address_book.people.add()
    person_john.id = 1234
    person_john.name = "John Doe"
    person_john.email = "jdoe@example.com"
    phone_john = person_john.phones.add()
    phone_john.number = "555-4321"
    phone_john.type = addressbook_syntax_proto3_pb2.Person.HOME

    person_alice = address_book.people.add()
    person_alice.id = 5678
    person_alice.name = "Alice Bob"
    phone_alice = person_alice.phones.add()
    phone_alice.number = "666-8765"
    phone_alice.type = addressbook_syntax_proto3_pb2.Person.MOBILE

    serialized_data = address_book.SerializeToString()
    assert type(serialized_data) == bytes
    assert serialized_data == b'\n-\n\x08John Doe\x10\xd2\t\x1a\x10jdoe@example.com"\x0c\n\x08555-4321\x10\x01\n\x1a\n\tAlice Bob\x10\xae,"\n\n\x08666-8765'

    deserialized_address_book = addressbook_syntax_proto3_pb2.AddressBook()
    deserialized_address_book.ParseFromString(serialized_data)

    assert len(deserialized_address_book.people) == 2

    deserialized_john = deserialized_address_book.people[0]
    
    assert deserialized_john.name == "John Doe"
    assert deserialized_john.email == "jdoe@example.com"
    assert len(deserialized_john.phones) == 1
    assert deserialized_john.phones[0].number == "555-4321"
    assert deserialized_john.phones[0].type == addressbook_syntax_proto3_pb2.Person.HOME

    deserialized_alice = deserialized_address_book.people[1]

    assert deserialized_alice.name == "Alice Bob"
    assert not deserialized_alice.email
    assert len(deserialized_alice.phones) == 1
    assert deserialized_alice.phones[0].number == "666-8765"
    assert deserialized_alice.phones[0].type == addressbook_syntax_proto3_pb2.Person.MOBILE


if __name__ == "__main__":
    person_demo()
    addressbook_demo()
