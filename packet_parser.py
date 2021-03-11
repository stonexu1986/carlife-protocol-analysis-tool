import wx
import struct
import binascii
import time

import cmd_message_parser
import video_message_parser
import music_message_parser
import tts_message_parser
import vr_message_parser
import touch_message_parser

from common_constant import const

all_cmd_parser_functions = {
	const.MSG_CMD_HU_PROTOCOL_VERSION_SERVICE_TYPE : 				cmd_message_parser.parse_msg_cmd_hu_protocol_version, 
	const.MSG_CMD_PROTOCOL_VERSION_MATCH_STATUS_SERVICE_TYPE: 		cmd_message_parser.parse_msg_cmd_protocol_version_match_status,
	const.MSG_CMD_HU_INFO_SERVICE_TYPE: 							cmd_message_parser.parse_msg_cmd_hu_info,
	const.MSG_CMD_MD_INFO_SERVICE_TYPE: 							cmd_message_parser.parse_msg_cmd_md_info,
	const.MSG_CMD_VIDEO_ENCODER_INIT_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_video_encoder_init,
	const.MSG_CMD_VIDEO_ENCODER_INIT_DONE_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_video_encoder_init_done,
	const.MSG_CMD_VIDEO_ENCODER_START_SERVICE_TYPE: 				cmd_message_parser.parse_msg_cmd_video_encoder_start,
	const.MSG_CMD_VIDEO_ENCODER_PAUSE_SERVICE_TYPE: 				cmd_message_parser.parse_msg_cmd_video_encoder_pause,
	const.MSG_CMD_VIDEO_ENCODER_RESET_SERVICE_TYPE: 				cmd_message_parser.parse_msg_cmd_video_encoder_reset,
	const.MSG_CMD_VIDEO_ENCODER_FRAME_RATE_CHANGE_SERVICE_TYPE: 	cmd_message_parser.parse_msg_cmd_video_encoder_frame_rate_change,
	const.MSG_CMD_VIDEO_ENCODER_FRAME_RATE_CHANGE_DONE_SERVICE_TYPE:cmd_message_parser.parse_msg_cmd_video_encoder_frame_rate_change_done,
	const.MSG_CMD_CAR_VELOCITY_SERVICE_TYPE:						cmd_message_parser.parse_msg_cmd_car_velocity,
	const.MSG_CMD_CAR_GPS_SERVICE_TYPE:								cmd_message_parser.parse_msg_cmd_car_gps,
	const.MSG_CMD_CAR_GYROSCOPE_SERVICE_TYPE:						cmd_message_parser.parse_msg_cmd_car_gytoscope,
	const.MSG_CMD_CAR_ACCELERATION_SERVICE_TYPE:					cmd_message_parser.parse_msg_cmd_car_acceleration,
	const.MSG_CMD_CAR_OIL_SERVICE_TYPE:								cmd_message_parser.parse_msg_cmd_car_oil,
	const.MSG_CMD_SCREEN_ON_SERVICE_TYPE: 							cmd_message_parser.parse_msg_cmd_screen_on,
	const.MSG_CMD_SCREEN_OFF_SERVICE_TYPE: 							cmd_message_parser.parse_msg_cmd_screen_off,
	const.MSG_CMD_SCREEN_USERPRESENT_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_screen_userpresent,
	const.MSG_CMD_FOREGROUND_SERVICE_TYPE: 							cmd_message_parser.parse_msg_cmd_foreground,
	const.MSG_CMD_BACKGROUND_SERVICE_TYPE: 							cmd_message_parser.parse_msg_cmd_background,
	const.MSG_CMD_LAUNCH_MODE_NORMAL_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_launch_mode_normal,
	const.MSG_CMD_LAUNCH_MODE_PHONE_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_launch_mode_phone,
	const.MSG_CMD_LAUNCH_MODE_MAP_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_launch_mode_map,
	const.MSG_CMD_LAUNCH_MODE_MUSIC_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_launch_mode_music,
	const.MSG_CMD_GO_TO_DESKTOP_SERVICE_TYPE: 						cmd_message_parser.parse_msg_cmd_go_to_desktop,
	const.MSG_CMD_MIC_RECORD_WAKEUP_START_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_mic_record_wakeup_start,
	const.MSG_CMD_MIC_RECORD_END_SERVICE_TYPE: 						cmd_message_parser.parse_msg_cmd_mic_record_end,
	const.MSG_CMD_MIC_RECORD_RECOG_START_SERVICE_TYPE: 				cmd_message_parser.parse_msg_cmd_mic_record_recog_start,
	const.MSG_CMD_GO_TO_FOREGROUND_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_mic_go_to_foreground,
	const.MSG_CMD_MODULE_STATUS_SERVICE_TYPE: 						cmd_message_parser.parse_msg_cmd_module_status,
	const.MSG_CMD_STATISTIC_INFO_SERVICE_TYPE: 						cmd_message_parser.parse_msg_cmd_statistic_info,
	const.MSG_CMD_MODULE_CONTROL_SERVICE_TYPE: 						cmd_message_parser.parse_msg_cmd_module_control,
	const.MSG_CMD_CAR_DATA_GEAR_SERVICE_TYPE: 						cmd_message_parser.parse_msg_cmd_car_data_gear,
	const.MSG_CMD_NAVI_NEXT_TURN_INFO_SERVICE_TYPE: 				cmd_message_parser.parse_msg_cmd_navi_next_turn_info,
	const.MSG_CMD_CAR_DATA_SUBSCRIBE_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_car_data_subscribe,
	const.MSG_CMD_CAR_DATA_SUBSCRIBE_DONE_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_car_data_subscribe_done,
	const.MSG_CMD_CAR_DATA_SUBSCRIBE_START_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_car_data_subscribe_start,
	const.MSG_CMD_CAR_DATA_SUBSCRIBE_STOP_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_car_data_subscribe_stop,
	const.MSG_CMD_MEDIA_INFO_SERVICE_TYPE: 							cmd_message_parser.parse_msg_cmd_media_info,
	const.MSG_CMD_MEDIA_PROGRESS_BAR_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_media_progress_bar,
	const.MSG_CMD_CONNECT_EXCEPTION_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_connect_exception,
	const.MSG_CMD_REQUEST_GO_TO_FOREGROUND_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_request_go_to_foreground,
	const.MSG_CMD_UI_ACTION_SOUND_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_ui_action_sound,
	const.MSG_CMD_NAVI_ASSITANTGUIDE_INFO_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_navi_assitant_guide_info,
	const.MSG_CMD_HU_AUTHEN_REQUEST_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_hu_authen_request,
	const.MSG_CMD_MD_AUTHEN_RESPONSE_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_md_authen_response,
	const.MSG_CMD_HU_AUTHEN_RESULT_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_hu_authen_result,
	const.MSG_CMD_MD_AUTHEN_RESULT_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_md_authen_result,
	const.MSG_CMD_GO_TO_FOREGROUND_RESPONSE_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_go_to_foreground_response,
	const.MSG_CMD_MD_FEATURE_CONFIG_REQUEST_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_md_feature_config_request,
	const.MSG_CMD_HU_FEATURE_CONFIG_RESPONSE_SERVICE_TYPE: 			cmd_message_parser.parse_msg_cmd_hu_feature_config_response,
	const.MSG_CMD_ERROR_CODE_SERVICE_TYPE: 							cmd_message_parser.parse_msg_cmd_error_code,
	const.MSG_CMD_VIDEO_ENCODER_JPEG_SERVICE_TYPE: 					cmd_message_parser.parse_msg_cmd_video_encoder_jpeg,
	const.MSG_CMD_VIDEO_ENCODER_JPEG_ACK_SERVICE_TYPE: 				cmd_message_parser.parse_msg_cmd_video_encoder_jpeg_ack,
	const.MSG_CMD_MD_EXIT_SERVICE_TYPE: 							cmd_message_parser.parse_msg_cmd_md_exit,
	const.MSG_CMD_HU_CONNECT_STATISTIC_SERVICE_TYPE: 				cmd_message_parser.parse_msg_cmd_hu_connect_statistic,
}

all_video_parser_functions = {
	const.MSG_VIDEO_DATA_SERVICE_TYPE: 				video_message_parser.parse_msg_video_data,
	const.MSG_VIDEO_HEARTBEAT_SERVICE_TYPE: 		video_message_parser.parse_msg_video_heartbeat
}

all_music_parser_functions = {
	const.MSG_MEDIA_INIT_SERVICE_TYPE: 				music_message_parser.parse_msg_media_init,
	const.MSG_MEDIA_PAUSE_SERVICE_TYPE: 			music_message_parser.parse_msg_media_pause,
	const.MSG_MEDIA_RESUME_PLAY_SERVICE_TYPE:		music_message_parser.parse_msg_media_resume_play,
	const.MSG_MEDIA_DATA_SERVICE_TYPE:				music_message_parser.parse_msg_media_data
}

all_tts_parser_functions = {
	const.MSG_NAVI_TTS_INIT_SERVICE_TYPE: 			tts_message_parser.parse_msg_navi_tts_init,
	const.MSG_NAVI_TTS_END_SERVICE_TYPE: 			tts_message_parser.parse_msg_navi_tts_end,
	const.MSG_NAVI_TTS_DATA_SERVICE_TYPE: 			tts_message_parser.parse_msg_navi_tts_data
}

all_vr_parser_functions = {
	const.MSG_VR_DATA_SERVICE_TYPE: 				vr_message_parser.parse_msg_vr_data,
	const.MSG_VR_AUDIO_INIT_SERVICE_TYPE: 			vr_message_parser.parse_msg_vr_audio_init,
	const.MSG_VR_AUDIO_DATA_SERVICE_TYPE: 			vr_message_parser.parse_msg_vr_audio_data,
	const.MSG_VR_AUDIO_STOP_SERVICE_TYPE: 			vr_message_parser.parse_msg_vr_audio_stop,
	const.MSG_VR_MODULE_STATUS_SERVICE_TYPE: 		vr_message_parser.parse_msg_vr_module_status,
	const.MSG_VR_AUDIO_INTERRUPT_SERVICE_TYPE: 		vr_message_parser.parse_msg_vr_audio_interrupt,
}

all_touch_parser_functions = {
	const.MSG_TOUCH_ACTION_SERVICE_TYPE: 			touch_message_parser.parse_msg_touch_action,
	const.MSG_TOUCH_CAR_HARD_KEY_CODE_SERVICE_TYPE: touch_message_parser.parse_msg_touch_car_hard_key_code
}

all_parsers = {
	const.CHANNEL_CMD: 	 cmd_message_parser,   const.CHANNEL_CMD+'_parser_functions': all_cmd_parser_functions,
	const.CHANNEL_VIDEO: video_message_parser, const.CHANNEL_VIDEO+'_parser_functions': all_video_parser_functions,
	const.CHANNEL_MUSIC: music_message_parser, const.CHANNEL_MUSIC+'_parser_functions': all_music_parser_functions,
	const.CHANNEL_TTS: 	 tts_message_parser,   const.CHANNEL_TTS+'_parser_functions': all_tts_parser_functions,
	const.CHANNEL_VR: 	 vr_message_parser, const.CHANNEL_VR+'_parser_functions': all_vr_parser_functions,
	const.CHANNEL_TOUCH: touch_message_parser, const.CHANNEL_TOUCH+'_parser_functions': all_touch_parser_functions,
}


def parse_packet(packet):
	packet['status'] = const.PARSE_STATUS_PASS
	
	if not packet.__contains__('message'):
		packet['status'] = const.PARSE_STATUS_FAIL
		return
		
	header = packet['header']
	message = packet['message']
	
	message_raw_data = message['raw_data']['data'].replace(' ', '')
	if len(message_raw_data) <= const.MAX_PRINT_MESSAGE_BYTES:
		print("\nparsing packet message: " + message_raw_data)
	else:
		print("\nparsing packet message: " + message_raw_data[0:const.MAX_PRINT_MESSAGE_BYTES] + '...')
	
	channel_id = header['channel_id']
	message_length = packet['message']['raw_data']['len']
	
	if channel_id == const.CHANNEL_ID_CMD:
		MESSAGE_HEADER_LENGTH = const.PACKET_CMD_MESSAGE_HEADER_LENGTH
	elif channel_id == const.CHANNEL_ID_VIDEO:
		MESSAGE_HEADER_LENGTH = const.PACKET_VIDEO_MESSAGE_HEADER_LENGTH
	elif channel_id == const.CHANNEL_ID_MUSIC:
		MESSAGE_HEADER_LENGTH = const.PACKET_AUDIO_MESSAGE_HEADER_LENGTH
	elif channel_id == const.CHANNEL_ID_TTS:
		MESSAGE_HEADER_LENGTH = const.PACKET_AUDIO_MESSAGE_HEADER_LENGTH
	elif channel_id == const.CHANNEL_ID_VR:
		MESSAGE_HEADER_LENGTH = const.PACKET_VR_MESSAGE_HEADER_LENGTH
	elif channel_id == const.CHANNEL_ID_TOUCH:
		MESSAGE_HEADER_LENGTH = const.PACKET_TOUCH_MESSAGE_HEADER_LENGTH
	else:
		print("invalid channel id: " + str(channel_id) + ', ignoring')
		return
		
	
	if int(message_length) < MESSAGE_HEADER_LENGTH:
		print("packet message length is too short, ignoring")
		packet['status'] = const.PARSE_STATUS_FAIL
		return
	
	message_hex_data = binascii.a2b_hex(message_raw_data)
	message_header = message_hex_data[0:MESSAGE_HEADER_LENGTH]
	message_data = message_hex_data[MESSAGE_HEADER_LENGTH:]
	
	channel_id_name = get_channel_name_from_id(channel_id)
	if all_parsers.__contains__(channel_id_name):
		all_parsers[channel_id_name].parse_header(message_header, message)
	else:
		packet['status'] = const.PARSE_STATUS_FAIL
		print("no parsers found, ignored")
		return
	
	
	if not message.__contains__('service_type'):
		print("no service type found, ignored")
		packet['status'] = const.PARSE_STATUS_FAIL
		return
	
	print("parsing message data:")
	service_type = message['service_type']
	
	if not all_parsers.__contains__(channel_id_name+'_parser_functions'):
		print("no parser functions found, ignored")
		packet['status'] = const.PARSE_STATUS_FAIL
		return
		
	
	parser_functions = all_parsers[channel_id_name+'_parser_functions']
	if parser_functions.__contains__(service_type):
		parser_functions[service_type](message_data, message)
		
	else:
		packet['status'] = const.PARSE_STATUS_FAIL
		print("# parse packet failed, unknown service type: " + service_type)
	


def find_all_packets(raw_datas, dialog):
	packets = []
	index = 0
	total_data_numbers = len(raw_datas)
	
	for raw_data in raw_datas:
		if raw_data.__contains__('prompt'):
			print("this is a prompt packet")
			packet = {'prompt': True, 'raw_data': raw_data}
			packets.append(packet)
		
		elif is_packet_header(raw_data):
			print("this is a packet header")
			
			header = {'raw_data': raw_data}
			parse_packet_header(raw_data, header)
			
			packet = {'header': header}
			packet['data_complete'] = False
			packet['prompt'] = False
			packets.append(packet)
		else :
			print("this is a packet message")
			
			for packet in packets[::-1]:
				if packet['prompt']:
					continue
				
				header = packet['header']
				header_msg_len = header['msg_len']
				header_direction = header['raw_data']['direction']
				
				if not packet['data_complete'] and header_direction == raw_data['direction'] and header['raw_data']['dev'] == raw_data['dev'] and header['raw_data']['ep'] == raw_data['ep']:
					if not packet.__contains__('message'):
						msg_len = raw_data['len']
						
						if int(msg_len) > header_msg_len:
							print("### invalid message, message is too long:")
							continue
						
						massage = {'raw_data': raw_data}
						packet['message'] = massage
						print("header_msg_len:" + str(header_msg_len) + ", msg_len:" + msg_len)
						if header_msg_len == int(msg_len):
							packet['data_complete'] = True
							print("matched with a packet header:")
							#print(packet)
							break
					else:
						message = packet['message']
						message_raw_data = message['raw_data']
						message_raw_data['data'] += ' '
						message_raw_data['data'] += raw_data['data']
						message_raw_data['ascii'] += raw_data['ascii']
						
						message_data_len = str(int(message_raw_data['len']) + int(raw_data['len']))
						message_raw_data['len'] = message_data_len
						
						print("message data length: total:" + str(header_msg_len) + ', now:' + message_data_len)
						
						if int(message_data_len) >= header_msg_len:
							packet['data_complete'] = True
							print("matched with a packet header:")
							#print(packet)	
							break
		
		# update UI
		index += 1
		progress = int((index / total_data_numbers) * 100)
		if progress < 100:	
			dialog.Update(progress, 'Extracting packet: ' + str(progress) + '%')
			#wx.CallAfter(dialog.Update, progress, 'Extracting packet: ' + str(progress) + '%')
			
		#time.sleep(0.0005)
			
	return packets
	
		
def is_packet_header(raw_data):
	contents = raw_data['data'].replace(' ', '')
	if len(contents) <= const.MAX_PRINT_MESSAGE_BYTES:
		print("\nparsing raw data(" + raw_data['len'] + "): " + contents)
	else:
		print("\nparsing raw data(" + raw_data['len'] + "): " + contents[0:const.MAX_PRINT_MESSAGE_BYTES] + '...')

	
	data_length = raw_data['len']
	
	if int(data_length) != const.PACKET_HEADER_LENGTH:
		return False
	
	hex_contents = binascii.a2b_hex(contents)
	header_content = hex_contents[0:8];
	
	channel_id, msg_len = struct.unpack('>ii', header_content)
	print("channel id: " + str(channel_id))
	
	if channel_id >= 1 and channel_id <= 6:
		return True

def parse_packet_header(raw_data, header):
	contents = raw_data['data'].replace(' ', '')
	#print("parsing raw data(" + raw_data['len'] + "): " + contents)
	
	hex_contents = binascii.a2b_hex(contents)
	
	channel_id, msg_len = struct.unpack('>ii', hex_contents)
	
	header['channel_id'] = channel_id
	header['msg_len'] = msg_len
	
def get_channel_name_from_id(channel_id):
	if channel_id == const.CHANNEL_ID_CMD:
		return const.CHANNEL_CMD
	elif channel_id == const.CHANNEL_ID_VIDEO:
		return const.CHANNEL_VIDEO
	elif channel_id == const.CHANNEL_ID_MUSIC:
		return const.CHANNEL_MUSIC
	elif channel_id == const.CHANNEL_ID_VIDEO:
		return const.CHANNEL_ID_TTS
	elif channel_id == const.CHANNEL_TTS:
		return const.CHANNEL_VIDEO
	elif channel_id == const.CHANNEL_ID_VR:
		return const.CHANNEL_VR
	elif channel_id == const.CHANNEL_ID_TOUCH:
		return const.CHANNEL_TOUCH
	else:
		return 'Unknown Channel'
