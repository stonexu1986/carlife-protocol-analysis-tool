import struct
import binascii

from common_constant import const
import protobuf.carlife_tts_init_pb2

def parse_header(header, message):
	print("parsing VR message header:")
	print(header)
	
	msg_data_len, timestamp, service_type = struct.unpack('>III', header)
	
	service_type_hex = hex(service_type)[2:].rjust(8, '0')
	service_type_hex = '0x' + service_type_hex.upper()
	
	message['msg_data_len'] = msg_data_len
	message['service_type'] = service_type_hex
	
	print("VR message header parsed: data len:" + str(msg_data_len) + 
		", timestamp:" + str(timestamp) + ", service type:" + service_type_hex)
	
	direction = (service_type >> 15) & 0x00000001
	if direction == 1:
		message['sender'] = const.ACCESSORY_HU
		message['receiver'] = const.ACCESSORY_MD
	else:
		message['sender'] = const.ACCESSORY_MD
		message['receiver'] = const.ACCESSORY_HU



# '0x00058001' : 'MSG_VR_DATA'
def parse_msg_vr_data(data, message):
	print("parse_msg_vr_data:")
	print(data)
	message['name'] = const.MSG_VR_DATA_SERVICE_NAME
	

# '0x00050002' : 'MSG_VR_AUDIO_INIT'
def parse_msg_vr_audio_init(data, message):
	print("parse_msg_vr_audio_init:")
	print(data)
	message['name'] = const.MSG_VR_AUDIO_INIT_SERVICE_NAME
	
	audio_init = protobuf.carlife_tts_init_pb2.CarLifeTTSInit()
	audio_init.ParseFromString(data)
	
	parameters = {}
	parameters['sampleRate'] = str(audio_init.sampleRate) + ' Hz'
	parameters['channelConfig'] = str(audio_init.channelConfig)
	parameters['sampleFormat'] = str(audio_init.sampleFormat)+ ' bits' 
	
	message['parameters'] = parameters
	_print_message_parameters(parameters)


# '0x00050003' : 'MSG_VR_AUDIO_DATA'
def parse_msg_vr_audio_data(data, message):
	print("parse_msg_vr_audio_data:")
	#print(data)
	message['name'] = const.MSG_VR_AUDIO_DATA_SERVICE_NAME
	

# '0x00050004' : 'MSG_VR_AUDIO_STOP'
def parse_msg_vr_audio_stop(data, message):
	print("parse_msg_vr_audio_stop:")
	print(data)
	message['name'] = const.MSG_VR_AUDIO_STOP_SERVICE_NAME


# '0x00050005' : 'MSG_VR_MODULE_STATUS'
def parse_msg_vr_module_status(data, message):
	print("parse_msg_vr_module_status:")
	print(data)
	message['name'] = const.MSG_VR_MODULE_STATUS_SERVICE_NAME


# '0x00050006' : 'MSG_VR_AUDIO_INTERRUPT'
def parse_msg_vr_audio_interrupt(data, message):
	print("parse_msg_vr_audio_interrupt:")
	print(data)
	message['name'] = const.MSG_VR_AUDIO_INTERRUPT_SERVICE_NAME


def _print_message_parameters(parameters):
	print("vr message data parsed, parameters:")
	print(parameters)
