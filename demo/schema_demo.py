import base64

from google.protobuf import descriptor, descriptor_pb2, message_factory
from google.protobuf.message_factory import MessageFactory
from google.protobuf.descriptor_pool import DescriptorPool


from generated_code.demo import addressbook_pb2


# TODO: What's definition of the schema in a protobuf context
#   - To locate a specific message type: it should be proto + class name


def schema_to_str(proto_file):
    """
    Args:
        proto_file (FileDescriptor): FileDescriptor to encode.
    Returns:
        str: Encoded FileDescriptor
    """
    return proto_file.serialized_pb
    # TODO: confluent use base64 to encode a FileDescriptor
    # return base64.standard_b64encode(proto_file.serialized_pb).decode('ascii')


def str_to_schema(raw_schema):
    file_descriptor_proto = descriptor_pb2.FileDescriptorProto.FromString(raw_schema)

    descriptor_pool = DescriptorPool()
    descriptor_pool.Add(file_descriptor_proto)

    name = file_descriptor_proto.name
    descriptor_person = descriptor_pool.FindMessageTypeByName('tutorial.Person')
    descriptor_addressbook = descriptor_pool.FindMessageTypeByName('tutorial.AddressBook')
    descriptor_phonenumber = descriptor_pool.FindMessageTypeByName('tutorial.Person.PhoneNumber')

    person_class = MessageFactory().GetPrototype(descriptor_person)
    addressbook_class = MessageFactory().GetPrototype(descriptor_addressbook)
    phonenumber_class = MessageFactory().GetPrototype(descriptor_phonenumber)

    # A different way to extract types from the proto
    # messages_type_dic = message_factory.GetMessages([file_descriptor_proto])
    # # messages_type_dic only contain 'tutorial.Person' and 'tutorial.AddressBook'
    # assert len(messages_type_dic) == 2
    # assert 'tutorial.Person' in messages_type_dic
    # assert 'tutorial.AddressBook' in messages_type_dic
    # person_class = messages_type_dic['tutorial.Person']
    # addressbook_class = messages_type_dic['tutorial.AddressBook']
    # person_instance = person_class()
    # addressbook_instance = addressbook_class()
    # return person_class, addressbook_class

    return person_class, addressbook_class, phonenumber_class


protobuf_class = addressbook_pb2.AddressBook

schema_str = schema_to_str(protobuf_class.DESCRIPTOR.file)
person_class, addressbook_class, phonenumber_class = str_to_schema(schema_str)

msg = person_class()
print(type(msg))
