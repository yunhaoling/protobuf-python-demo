class ProtobufSerializer:
    def __init__(self):
        pass

    def serialize(self, data):
        return data.SerializeToString()

    def deserialize(self, data, protobuf_type):
        obj = protobuf_type()
        obj.ParseFromString(data)
        return obj
