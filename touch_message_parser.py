import struct
import binascii

from common_constant import const

import protobuf.carlife_touch_action_pb2
import protobuf.carlife_car_hard_key_code_pb2

hard_keycode_table = {
	const.KEYCODE_HOME_ID : 				const.KEYCODE_HOME_NAME,
	const.KEYCODE_PHONE_CALL_ID : 			const.KEYCODE_PHONE_CALL_NAME,
	const.KEYCODE_PHONE_END_ID : 			const.KEYCODE_PHONE_END_NAME,
	const.KEYCODE_PHONE_END_MUTE_ID : 		const.KEYCODE_PHONE_END_MUTE_NAME,
	const.KEYCODE_HFP_ID : 					const.KEYCODE_HFP_NAME,
	const.KEYCODE_SELECTOR_NEXT_ID : 		const.KEYCODE_SELECTOR_NEXT_NAME,
	const.KEYCODE_SELECTOR_PREVIOUS_ID :	const.KEYCODE_SELECTOR_PREVIOUS_NAME,
	const.KEYCODE_SETTING_ID : 				const.KEYCODE_SETTING_NAME,
	const.KEYCODE_MEDIA_ID : 				const.KEYCODE_MEDIA_NAME,
	const.KEY_CODE_RADIO_ID : 				const.KEY_CODE_RADIO_NAME,
	const.KEYCODE_SRC_ID : 					const.KEYCODE_SRC_NAME,
	const.KEYCODE_BACK_ID : 				const.KEYCODE_BACK_NAME,
	const.KEYCODE_SEEK_SUB_ID : 			const.KEYCODE_SEEK_SUB_NAME,
	const.KEYCODE_SEEK_ADD_ID : 			const.KEYCODE_SEEK_ADD_NAME,
	const.KEYCODE_VOLUME_SUB_ID : 			const.KEYCODE_VOLUME_SUB_NAME,
	const.KEYCODE_VOLUME_ADD_ID : 			const.KEYCODE_VOLUME_ADD_NAME,
	const.KEYCODE_MUTE_ID : 				const.KEYCODE_MUTE_NAME,
	const.KEYCODE_OK_ID : 					const.KEYCODE_OK_NAME,
	const.KEYCODE_MOVE_LEFT_ID : 			const.KEYCODE_MOVE_LEFT_NAME,
	const.KEYCODE_MOVE_RIGHT_ID : 			const.KEYCODE_MOVE_RIGHT_NAME,
	const.KEYCODE_MOVE_UP_ID : 				const.KEYCODE_MOVE_UP_NAME,
	const.KEYCODE_MOVE_DOWN_ID : 			const.KEYCODE_MOVE_DOWN_NAME,
	const.KEYCODE_MOVE_UP_LEFT_ID : 		const.KEYCODE_MOVE_UP_LEFT_NAME,
	const.KEYCODE_MOVE_UP_RIGHT_ID : 		const.KEYCODE_MOVE_UP_RIGHT_NAME,
	const.KEYCODE_MOVE_DOWN_LEFT_ID : 		const.KEYCODE_MOVE_DOWN_LEFT_NAME,
	const.KEYCODE_MOVE_DOWN_RIGHT_ID :	 	const.KEYCODE_MOVE_DOWN_RIGHT_NAME,
	const.KEYCODE_TEL_ID :	 				const.KEYCODE_TEL_NAME,
	const.KEYCODE_MAIN_ID : 				const.KEYCODE_MAIN_NAME,
	const.KEYCODE_MEDIA_START_ID : 			const.KEYCODE_MEDIA_START_NAME,
	const.KEYCODE_MEDIA_STOP_ID :		 	const.KEYCODE_MEDIA_STOP_NAME,
	const.KEYCODE_VR_START_ID : 			const.KEYCODE_VR_START_NAME,
	const.KEYCODE_VR_STOP_ID : 				const.KEYCODE_VR_STOP_NAME,
	const.KEYCODE_NUMBER_0_ID : 			const.KEYCODE_NUMBER_0_NAME,
	const.KEYCODE_NUMBER_1_ID : 			const.KEYCODE_NUMBER_1_NAME,
	const.KEYCODE_NUMBER_2_ID :				const.KEYCODE_NUMBER_2_NAME,
	const.KEYCODE_NUMBER_3_ID : 			const.KEYCODE_NUMBER_3_NAME,
	const.KEYCODE_NUMBER_4_ID : 			const.KEYCODE_NUMBER_4_NAME,
	const.KEYCODE_NUMBER_5_ID : 			const.KEYCODE_NUMBER_5_NAME,
	const.KEYCODE_NUMBER_6_ID : 			const.KEYCODE_NUMBER_6_NAME,
	const.KEYCODE_NUMBER_7_ID : 			const.KEYCODE_NUMBER_7_NAME,
	const.KEYCODE_NUMBER_8_ID : 			const.KEYCODE_NUMBER_8_NAME,
	const.KEYCODE_NUMBER_9_ID : 			const.KEYCODE_NUMBER_9_NAME,
	const.KEYCODE_NUMBER_10_ID : 			const.KEYCODE_NUMBER_10_NAME,
	const.KEYCODE_NUMBER_11_ID : 			const.KEYCODE_NUMBER_11_NAME,
	const.KEYCODE_NUMBER_DEL_ID : 			const.KEYCODE_NUMBER_DEL_NAME,
	const.KEYCODE_NUMBER_CLEAR_ID : 		const.KEYCODE_NUMBER_CLEAR_NAME,
	const.KEYCODE_NUMBER_PLUS_ID : 			const.KEYCODE_NUMBER_PLUS_NAME,
}


def parse_header(header, message):
	print("parsing touch message header:")
	print(header)
	
	msg_data_len, reserved, service_type = struct.unpack('>HHI', header)
	
	service_type_hex = hex(service_type)[2:].rjust(8, '0')
	service_type_hex = '0x' + service_type_hex.upper()
	
	message['msg_data_len'] = msg_data_len
	message['service_type'] = service_type_hex
	
	print("touch message header parsed: data len:" + str(msg_data_len) + ", service type:" + service_type_hex)
	
	direction = (service_type >> 15) & 0x00000001
	if direction == 1:
		message['sender'] = const.ACCESSORY_HU
		message['receiver'] = const.ACCESSORY_MD
	else:
		message['sender'] = const.ACCESSORY_MD
		message['receiver'] = const.ACCESSORY_HU


# '0x00068001' : 'MSG_TOUCH_ACTION'
def parse_msg_touch_action(data, message):
	print("parse_msg_touch_action:")
	print(data)
	message['name'] = const.MSG_TOUCH_ACTION_SERVICE_NAME
	
	touch_action = protobuf.carlife_touch_action_pb2.CarlifeTouchAction()
	touch_action.ParseFromString(data)
	
	parameters = {}
	parameters['action'] = _get_action_name_from_id(touch_action.action)
	parameters['x'] = str(touch_action.x)
	parameters['y'] = str(touch_action.y)
	
	message['parameters'] = parameters
	_print_message_parameters(parameters)
	

# '0x00068008' : 'MSG_TOUCH_CAR_HARD_KEY_CODE'
def parse_msg_touch_car_hard_key_code(data, message):
	print("parse_msg_touch_car_hard_key_code:")
	print(data)
	message['name'] = const.MSG_TOUCH_CAR_HARD_KEY_CODE_SERVICE_NAME
	
	hard_keycode = protobuf.carlife_car_hard_key_code_pb2.CarLifeCarHardKeyCode()
	hard_keycode.ParseFromString(data)
	
	if hard_keycode_table.__contain__(hard_keycode.keycode):
		keycode_name = hard_keycode_table[hard_keycode.keycode]
	else:
		keycode_name =  hex(hard_keycode.keycode)[2:].rjust(8, '0')
		keycode_name = '0x' + service_type_hex.upper()
	
	
	parameters = {}
	parameters['keycode'] = keycode_name
	
	message['parameters'] = parameters
	_print_message_parameters(parameters)



def _print_message_parameters(parameters):
	print("touch message data parsed, parameters:")
	print(parameters)


def _get_action_name_from_id(action_id):
	action_name = 'unknown'
	
	if action_id == const.ACTION_DOWN_ID:
		action_name = const.ACTION_DOWN_NAME
	elif action_id == const.ACTION_UP_ID:
		action_name = const.ACTION_UP_NAME
	elif action_id == const.ACTION_MOVE_ID:
		action_name = const.ACTION_MOVE_NAME
	
	return action_name
	
