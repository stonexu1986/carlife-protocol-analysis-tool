
import protobuf.CarlifeProtocolVersion_pb2 as CarlifeProtocolVersion_pb2

protocol_version = CarlifeProtocolVersion_pb2.CarlifeProtocolVersion()
protocol_version.majorVersion = 2
protocol_version.minorVersion = 0

serializeToString = protocol_version.SerializeToString()
print(serializeToString)

new_protocol_version = CarlifeProtocolVersion_pb2.CarlifeProtocolVersion()
new_protocol_version.ParseFromString(serializeToString)

print(new_protocol_version.majorVersion)
print(new_protocol_version.minorVersion)
