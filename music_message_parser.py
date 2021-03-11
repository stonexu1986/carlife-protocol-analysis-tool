import struct
import binascii

from common_constant import const
import protobuf.carlife_media_init_pb2

def parse_header(header, message):
	print("parsing music message header:")
	print(header)
	
	msg_data_len, timestamp, service_type = struct.unpack('>III', header)
	
	service_type_hex = hex(service_type)[2:].rjust(8, '0')
	service_type_hex = '0x' + service_type_hex.upper()
	
	message['msg_data_len'] = msg_data_len
	message['service_type'] = service_type_hex
	
	print("music message header parsed: data len:" + str(msg_data_len) + 
		", timestamp:" + str(timestamp) + ", service type:" + service_type_hex)
	
	direction = (service_type >> 15) & 0x00000001
	if direction == 1:
		message['sender'] = const.ACCESSORY_HU
		message['receiver'] = const.ACCESSORY_MD
	else:
		message['sender'] = const.ACCESSORY_MD
		message['receiver'] = const.ACCESSORY_HU


# '0x00030001' : 'MSG_MEDIA_INIT'
def parse_msg_media_init(data, message):
	print("parse_msg_media_init:")
	print(data)
	message['name'] = const.MSG_MEDIA_INIT_SERVICE_NAME
	
	media_init = protobuf.carlife_media_init_pb2.CarLifeMediaInit()
	media_init.ParseFromString(data)
	
	parameters = {}
	parameters['sampleRate'] = str(media_init.sampleRate) + ' Hz'
	parameters['channelConfig'] = str(media_init.channelConfig)
	parameters['sampleFormat'] = str(media_init.sampleFormat)+ ' bits' 
	
	message['parameters'] = parameters
	_print_message_parameters(parameters)
	

# '0x00030003' : 'MSG_MEDIA_PAUSE'
def parse_msg_media_pause(data, message):
	print("parse_msg_media_pause:")
	print(data)
	message['name'] = const.MSG_MEDIA_PAUSE_SERVICE_NAME


# '0x00030004' : 'MSG_MEDIA_RESUME_PLAY'
def parse_msg_media_resume_play(data, message):
	print("parse_msg_media_resume_play:")
	print(data)
	message['name'] = const.MSG_MEDIA_RESUME_PLAY_SERVICE_NAME
	
	
# '0x00030006' : 'MSG_MEDIA_DATA'
def parse_msg_media_data(data, message):
	print("parse_msg_media_data:")
	#print(data)
	message['name'] = const.MSG_MEDIA_DATA_SERVICE_NAME



def _print_message_parameters(parameters):
	print("music message data parsed, parameters:")
	print(parameters)
