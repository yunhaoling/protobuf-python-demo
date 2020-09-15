import base64

from google.protobuf import descriptor_pb2
from google.protobuf import descriptor
from google.protobuf.message_factory import MessageFactory
from google.protobuf.descriptor_pool import DescriptorPool


from generated_code.demo import addressbook_syntax_proto3_pb2

def schema_to_str(proto_file):
    """
    Base64 encodes a FileDescriptor
    Args:
        proto_file (FileDescriptor): FileDescriptor to encode.
    Returns:
        str: Base64 encoded FileDescriptor
    """
    return proto_file.serialized_pb
    #return base64.standard_b64encode(proto_file.serialized_pb).decode('ascii')

def str_to_schema(raw_schema):
    file_descriptor_proto = descriptor_pb2.FileDescriptorProto.FromString(raw_schema)
    
    descriptor_pool = DescriptorPool()
    descriptor_pool.Add(file_descriptor_proto)

    # message_descriptors = []
    # for message_type in file_descriptor_proto.message_type:
    #     print(message_type)
    #     # The following line would raise error asking to import 
    #     message_descriptors.append(descriptor.MakeDescriptor(message_type))
    
    name = file_descriptor_proto.name
    file_descriptor = descriptor_pool.FindFileByName(name)
    descriptor1 = descriptor_pool.FindMessageTypeByName('tutorial.Person')
    descriptor2 = descriptor_pool.FindMessageTypeByName('tutorial.AddressBook')
    descriptor3 = descriptor_pool.FindMessageTypeByName('tutorial.Person.PhoneNumber')

    return descriptor1, descriptor2, descriptor3


protobuf_class = addressbook_syntax_proto3_pb2.AddressBook
assert protobuf_class.DESCRIPTOR.full_name == 'tutorial.AddressBook'

schema_str = schema_to_str(protobuf_class.DESCRIPTOR.file)
descriptor1, descriptor2, descriptor3 = str_to_schema(schema_str)

msg_class = MessageFactory().GetPrototype(descriptor1)

msg = msg_class()
print(type(msg))