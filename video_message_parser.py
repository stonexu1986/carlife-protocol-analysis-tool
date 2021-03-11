import struct
import binascii

from common_constant import const


def parse_header(header, message):
	print("parsing video message header:")
	print(header)
	
	msg_data_len, timestamp, service_type = struct.unpack('>III', header)
	
	service_type_hex = hex(service_type)[2:].rjust(8, '0')
	service_type_hex = '0x' + service_type_hex.upper()
	
	message['msg_data_len'] = msg_data_len
	message['timestamp'] = timestamp
	message['service_type'] = service_type_hex
	
	print("video message header parsed: data len:" + str(msg_data_len) + 
		", timestamp:" + str(timestamp) + ", service type:" + service_type_hex)
	
	direction = (service_type >> 15) & 0x00000001
	if direction == 1:
		message['sender'] = const.ACCESSORY_HU
		message['receiver'] = const.ACCESSORY_MD
	else:
		message['sender'] = const.ACCESSORY_MD
		message['receiver'] = const.ACCESSORY_HU


# '0x00020001' : 'MSG_VIDEO_DATA'
def parse_msg_video_data(data, message):
	print("parse_msg_video_data:")
	#print(data)
	message['name'] = const.MSG_VIDEO_DATA_SERVICE_NAME


# '0x00020002' : 'MSG_VIDEO_HEARTBEAT'
def parse_msg_video_heartbeat(data, message):
	print("parse_msg_video_heartbeat:")
	#print(data)
	message['name'] = const.MSG_VIDEO_HEARTBEAT_SERVICE_NAME


