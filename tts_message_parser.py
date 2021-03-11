import struct
import binascii

from common_constant import const
import protobuf.carlife_tts_init_pb2

def parse_header(header, message):
	print("parsing TTS message header:")
	print(header)
	
	msg_data_len, timestamp, service_type = struct.unpack('>III', header)
	
	service_type_hex = hex(service_type)[2:].rjust(8, '0')
	service_type_hex = '0x' + service_type_hex.upper()
	
	message['msg_data_len'] = msg_data_len
	message['service_type'] = service_type_hex
	
	print("TTS message header parsed: data len:" + str(msg_data_len) + 
		", timestamp:" + str(timestamp) + ", service type:" + service_type_hex)
	
	direction = (service_type >> 15) & 0x00000001
	if direction == 1:
		message['sender'] = const.ACCESSORY_HU
		message['receiver'] = const.ACCESSORY_MD
	else:
		message['sender'] = const.ACCESSORY_MD
		message['receiver'] = const.ACCESSORY_HU



# '0x00040001' : 'MSG_NAVI_TTS_INIT'
def parse_msg_navi_tts_init(data, message):
	print("parse_msg_navi_tts_init:")
	print(data)
	message['name'] = const.MSG_NAVI_TTS_INIT_SERVICE_NAME
	
	tts_init = protobuf.carlife_tts_init_pb2.CarLifeTTSInit()
	tts_init.ParseFromString(data)
	
	parameters = {}
	parameters['sampleRate'] = str(tts_init.sampleRate) + ' Hz'
	parameters['channelConfig'] = str(tts_init.channelConfig)
	parameters['sampleFormat'] = str(tts_init.sampleFormat)+ ' bits' 
	
	message['parameters'] = parameters
	_print_message_parameters(parameters)
	

# '0x00040002' : 'MSG_NAVI_TTS_END'
def parse_msg_navi_tts_end(data, message):
	print("parse_msg_navi_tts_end:")
	print(data)
	message['name'] = const.MSG_NAVI_TTS_END_SERVICE_NAME


# '0x00040003' : 'MSG_NAVI_TTS_DATA'
def parse_msg_navi_tts_data(data, message):
	print("parse_msg_navi_tts_data:")
	#print(data)
	message['name'] = const.MSG_NAVI_TTS_DATA_SERVICE_NAME



def _print_message_parameters(parameters):
	print("tts message data parsed, parameters:")
	print(parameters)
