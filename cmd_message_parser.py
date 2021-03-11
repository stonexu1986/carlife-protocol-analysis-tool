import struct
import binascii

from common_constant import const
import protobuf.carlife_protocol_version_pb2
import protobuf.carlife_protocol_version_match_status_pb2
import protobuf.carlife_device_info_pb2
import protobuf.carlife_video_encoder_info_pb2
import protobuf.carlife_statistics_info_pb2
import protobuf.carlife_authen_result_pb2
import protobuf.carlife_feature_config_list_pb2
import protobuf.carlife_vehicle_info_pb2
import protobuf.carlife_vehicle_info_list_pb2
import protobuf.carlife_module_status_pb2
import protobuf.carlife_module_status_list_pb2
import protobuf.carlife_video_frame_rate_pb2
import protobuf.carlife_car_speed_pb2
import protobuf.carlife_car_gps_pb2
import protobuf.carlife_car_gyroscope_pb2
import protobuf.carlife_car_acceleration_pb2
import protobuf.carlife_car_oil_pb2
import protobuf.carlife_car_gear_info_pb2
import protobuf.carlife_navi_next_turn_info_pb2
import protobuf.carlife_media_info_pb2
import protobuf.carlife_media_progress_bar_pb2
import protobuf.carlife_connect_exception_pb2
import protobuf.carlife_navi_assitant_guide_info_pb2
import protobuf.carlife_authen_request_pb2
import protobuf.carlife_authen_response_pb2
import protobuf.carlife_error_code_pb2
import protobuf.carlife_con_statistic_pb2



def parse_header(header, message):
	print("parsing cmd message header:")
	print(header)
	
	msg_data_len, reserved, service_type = struct.unpack('>HHI', header)
	
	service_type_hex = hex(service_type)[2:].rjust(8, '0')
	service_type_hex = '0x' + service_type_hex.upper()
	
	message['msg_data_len'] = msg_data_len
	message['service_type'] = service_type_hex
	
	print("cmd message header parsed: data len:" + str(msg_data_len) + ", service type:" + service_type_hex)
	
	direction = (service_type >> 15) & 0x00000001
	if direction == 1:
		message['sender'] = const.ACCESSORY_HU
		message['receiver'] = const.ACCESSORY_MD
	else:
		message['sender'] = const.ACCESSORY_MD
		message['receiver'] = const.ACCESSORY_HU
	

# '0x00018001' : 'MSG_CMD_HU_PROTOCOL_VERSION'
def parse_msg_cmd_hu_protocol_version(data, message):
	print("parse_data_msg_cmd_hu_protocol_version:")
	print(data)

	message['name'] = const.MSG_CMD_HU_PROTOCOL_VERSION_SERVICE_NAME
	
	protocol_version = protobuf.carlife_protocol_version_pb2.CarlifeProtocolVersion()
	protocol_version.ParseFromString(data)
	
	parameters = {'majorVersion': str(protocol_version.majorVersion), 
				  'minorVersion': str(protocol_version.minorVersion)}
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	
	
# '0x00010002' : 'MSG_CMD_PROTOCOL_VERSION_MATCH_STATUS'
def parse_msg_cmd_protocol_version_match_status(data, message):
	print("parse_data_msg_cmd_hu_protocol_version:")
	print(data)
	
	message['name'] = const.MSG_CMD_PROTOCOL_VERSION_MATCH_STATUS_SERVICE_NAME
	
	procotol_match_status = protobuf.carlife_protocol_version_match_status_pb2.CarlifeProtocolVersionMatchStatus()
	procotol_match_status.ParseFromString(data)
	
	parameters = {'matchStatus': str(procotol_match_status.matchStatus)}
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x00018003' : 'MSG_CMD_HU_INFO'
def parse_msg_cmd_hu_info(data, message):
	print("parse_msg_cmd_hu_info:")
	print(data)
	
	message['name'] = const.MSG_CMD_HU_INFO_SERVICE_NAME
	
	device_info = protobuf.carlife_device_info_pb2.CarlifeDeviceInfo()
	device_info.ParseFromString(data)

	parameters = {}
	
	if len(device_info.os) > 0:
		parameters['os'] = device_info.os
	
	if len(device_info.manufacturer) > 0:
		parameters['manufacturer'] = device_info.manufacturer
		
	if len(device_info.model) > 0:
		parameters['model'] = device_info.model
		
	if len(device_info.release) > 0:
		parameters['release'] = device_info.release
		
	if len(device_info.btaddress) > 0:
		parameters['btaddress'] = device_info.btaddress
	
	if len(device_info.btname) > 0:
		parameters['btname'] = device_info.btname
	
	message['parameters'] = parameters
	print_message_parameters(parameters)

	
# '0x00010004' : 'MSG_CMD_MD_INFO'
def parse_msg_cmd_md_info(data, message):
	print("parse_msg_cmd_md_info:")
	print(data)
	
	message['name'] = const.MSG_CMD_MD_INFO_SERVICE_NAME
	
	device_info = protobuf.carlife_device_info_pb2.CarlifeDeviceInfo()
	device_info.ParseFromString(data)
	
	print(device_info)

	parameters = {}
	
	if len(device_info.os) > 0:
		parameters['os'] = device_info.os
	
	if len(device_info.board) > 0:
		parameters['board'] = device_info.board
		
	if len(device_info.bootloader) > 0:
		parameters['bootloader'] = device_info.bootloader
	
	if len(device_info.brand) > 0:
		parameters['brand'] = device_info.brand
		
	if len(device_info.cpu_abi) > 0:
		parameters['cpu_abi'] = device_info.cpu_abi
	
	if len(device_info.cpu_abi2) > 0:
		parameters['cpu_abi2'] = device_info.cpu_abi2
	
	if len(device_info.device) > 0:
		parameters['device'] = device_info.device
		
	if len(device_info.display) > 0:
		parameters['display'] = device_info.display
		
	if len(device_info.fingerprint) > 0:
		parameters['fingerprint'] = device_info.fingerprint	
	
	if len(device_info.hardware) > 0:
		parameters['hardware'] = device_info.hardware	
		
	if len(device_info.host) > 0:
		parameters['host'] = device_info.host	
		
	if len(device_info.cid) > 0:
		parameters['cid'] = device_info.cid	
		
	if len(device_info.manufacturer) > 0:
		parameters['manufacturer'] = device_info.manufacturer
		
	if len(device_info.model) > 0:
		parameters['model'] = device_info.model	
		
	if len(device_info.product) > 0:
		parameters['product'] = device_info.product	
		
	if len(device_info.serial) > 0:
		parameters['serial'] = device_info.serial	
		
	if len(device_info.codename) > 0:
		parameters['codename'] = device_info.codename	
		
	if len(device_info.incremental) > 0:
		parameters['incremental'] = device_info.incremental
	
	if len(device_info.release) > 0:
		parameters['release'] = device_info.release	
	
	if len(device_info.sdk) > 0:
		parameters['sdk'] = device_info.sdk	
		
	if device_info.sdk_int > 0:
		parameters['sdk_int'] = str(device_info.sdk_int)	
		
	if len(device_info.token) > 0:
		parameters['token'] = device_info.token
	
	if len(device_info.btaddress) > 0:
		parameters['btaddress'] = device_info.btaddress
	
	if len(device_info.btname) > 0:
		parameters['btname'] = device_info.btname

	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x00018007' : 'MSG_CMD_VIDEO_ENCODER_INIT'
def parse_msg_cmd_video_encoder_init(data, message):
	print("parse_msg_cmd_video_encoder_init:")
	print(data)
	message['name'] = const.MSG_CMD_VIDEO_ENCODER_INIT_SERVICE_NAME
	
	encoder_info = protobuf.carlife_video_encoder_info_pb2.CarlifeVideoEncoderInfo()
	encoder_info.ParseFromString(data)
	
	parameters = {}
	parameters['width'] = str(encoder_info.width)
	parameters['height'] = str(encoder_info.height)
	parameters['frameRate'] = str(encoder_info.frameRate)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x00010008' : 'MSG_CMD_VIDEO_ENCODER_INIT_DONE'
def parse_msg_cmd_video_encoder_init_done(data, message):
	print("parse_msg_cmd_video_encoder_init_done:")
	print(data)
	message['name'] = const.MSG_CMD_VIDEO_ENCODER_INIT_DONE_SERVICE_NAME
	
	encoder_info = protobuf.carlife_video_encoder_info_pb2.CarlifeVideoEncoderInfo()
	encoder_info.ParseFromString(data)
	
	parameters = {}
	parameters['width'] = str(encoder_info.width)
	parameters['height'] = str(encoder_info.height)
	parameters['frameRate'] = str(encoder_info.frameRate)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x00018009' : 'MSG_CMD_VIDEO_ENCODER_START'
def parse_msg_cmd_video_encoder_start(data, message):
	print("parse_msg_cmd_video_encoder_start:")
	print(data)
	message['name'] = const.MSG_CMD_VIDEO_ENCODER_START_SERVICE_NAME


# '0x0001800A' : 'MSG_CMD_VIDEO_ENCODER_PAUSE'
def parse_msg_cmd_video_encoder_pause(data, message):
	print("parse_msg_cmd_video_encoder_pause:")
	print(data)
	message['name'] = const.MSG_CMD_VIDEO_ENCODER_PAUSE_SERVICE_NAME	


# '0x0001800B' : 'MSG_CMD_VIDEO_ENCODER_RESET'
def parse_msg_cmd_video_encoder_reset(data, message):
	print("parse_msg_cmd_video_encoder_reset:")
	print(data)
	message['name'] = const.MSG_CMD_VIDEO_ENCODER_RESET_SERVICE_NAME
	
	
# '0x0001800C' : 'MSG_CMD_VIDEO_ENCODER_FRAME_RATE_CHANGE'
def parse_msg_cmd_video_encoder_frame_rate_change(data, message):
	print("parse_msg_cmd_video_encoder_frame_rate_change:")
	print(data)
	message['name'] = const.MSG_CMD_VIDEO_ENCODER_FRAME_RATE_CHANGE_SERVICE_NAME
	
	frame_rate = protobuf.carlife_video_frame_rate_pb2.CarlifeVideoFrameRate()
	frame_rate.ParseFromString(data)
	
	parameters = {}
	parameters['frameRate'] = str(frame_rate.frameRate)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x0001000D' : 'MSG_CMD_VIDEO_ENCODER_FRAME_RATE_CHANGE_DONE'
def parse_msg_cmd_video_encoder_frame_rate_change_done(data, message):
	print("parse_msg_cmd_video_encoder_frame_rate_change_done:")
	print(data)
	message['name'] = const.MSG_CMD_VIDEO_ENCODER_FRAME_RATE_CHANGE_DONE_SERVICE_NAME
	
	frame_rate = protobuf.carlife_video_frame_rate_pb2.CarlifeVideoFrameRate()
	frame_rate.ParseFromString(data)
	
	parameters = {}
	parameters['frameRate'] = str(frame_rate.frameRate)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x0001800F' : 'MSG_CMD_CAR_VELOCITY'
def parse_msg_cmd_car_velocity(data, message):
	print("parse_msg_cmd_car_velocity:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_VELOCITY_SERVICE_NAME
	
	car_speed = protobuf.carlife_car_speed_pb2.CarlifeCarSpeed()
	car_speed.ParseFromString(data)
	
	parameters = {}
	parameters['speed'] = str(car_speed.car_speed)
	if car_speed.timeStamp > 0:
		parameters['timeStamp'] = str(car_speed.timeStamp)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	
	
# '0x00018010' : 'MSG_CMD_CAR_GPS_SERVICE_NAME'
def parse_msg_cmd_car_gps(data, message):
	print("parse_msg_cmd_car_gps:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_GPS_SERVICE_NAME
	
	car_gps = protobuf.carlife_car_gps_pb2.CarLifeCarGps()
	car_gps.ParseFromString(data)
	
	parameters = {}
	parameters['antennaState'] = str(car_gps.antennaState)
	parameters['latitude'] = str(car_gps.latitude)
	parameters['longitude'] = str(car_gps.longitude)
	parameters['height'] = str(car_gps.height)
	parameters['speed'] = str(car_gps.speed)
	parameters['heading'] = str(car_gps.heading)
	parameters['satsUsed'] = str(car_gps.satsUsed)
	parameters['satsVisible'] = str(car_gps.satsVisible)
	if car_gps.timeStamp > 0:
		parameters['timeStamp'] = str(car_gps.timeStamp)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00018011' : 'MSG_CMD_CAR_GYROSCOPE'
def parse_msg_cmd_car_gytoscope(data, message):
	print("parse_msg_cmd_car_gytoscope:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_GYROSCOPE_SERVICE_NAME
	
	car_gyroscope = protobuf.carlife_car_gyroscope_pb2.CarlifeGyroscope()
	car_gyroscope.ParseFromString(data)
	
	parameters = {}
	if car_gyroscope.gyroType == protobuf.carlife_car_gyroscope_pb2.GyroType.SINGLE_AXIS_GYRO:	
		parameters['gyroType'] = "SINGLE_AXIS_GYRO"
	elif car_gyroscope.gyroType == protobuf.carlife_car_gyroscope_pb2.GyroType.THREE_AXIS_GYRO:	
		parameters['gyroType'] = "THREE_AXIS_GYRO"
	else:
		parameters['gyroType'] = "unknown(" + str(car_gyroscope.gyroType) + ')'
				
	parameters['gyroX'] = str(car_gyroscope.gyroX)
	parameters['gyroY'] = str(car_gyroscope.gyroY)
	parameters['gyroZ'] = str(car_gyroscope.gyroZ)
	
	if car_gyroscope.timeStamp > 0:
		parameters['timeStamp'] = str(car_gyroscope.timeStamp)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00018012' : 'MSG_CMD_CAR_ACCELERATION'
def parse_msg_cmd_car_acceleration(data, message):
	print("parse_msg_cmd_car_acceleration:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_ACCELERATION_SERVICE_NAME
	
	car_acceleration = protobuf.carlife_car_acceleration_pb2.CarlifeAcceleration()
	car_acceleration.ParseFromString(data)
	
	parameters = {}
	parameters['accX'] = str(car_acceleration.accX)
	parameters['accY'] = str(car_acceleration.accY)
	parameters['accZ'] = str(car_acceleration.accZ)
	if car_acceleration.timeStamp > 0:
		parameters['timeStamp'] = str(car_acceleration.timeStamp)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x00018013' : 'MSG_CMD_CAR_OIL'
def parse_msg_cmd_car_oil(data, message):
	print("parse_msg_cmd_car_oil:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_OIL_SERVICE_NAME
	
	car_oil = protobuf.carlife_car_oil_pb2.CarlifeOil()
	car_oil.ParseFromString(data)

	parameters = {}
	parameters['level'] = str(car_oil.level)
	parameters['range'] = str(car_oil.range)
	parameters['lowFuleWarning'] = str(car_oil.lowFuleWarning)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00010018' : 'MSG_CMD_SCREEN_ON'
def parse_msg_cmd_screen_on(data, message):
	print("parse_msg_cmd_screen_on:")
	print(data)
	message['name'] = const.MSG_CMD_SCREEN_ON_SERVICE_NAME
	
	
# '0x00010019' : 'MSG_CMD_SCREEN_OFF'
def parse_msg_cmd_screen_off(data, message):
	print("parse_msg_cmd_screen_off:")
	print(data)
	message['name'] = const.MSG_CMD_SCREEN_OFF_SERVICE_NAME


# '0x0001001A' : 'MSG_CMD_SCREEN_USERPRESENT'
def parse_msg_cmd_screen_userpresent(data, message):
	print("parse_msg_cmd_screen_userpresent:")
	print(data)
	message['name'] = const.MSG_CMD_SCREEN_USERPRESENT_SERVICE_NAME
	
	
# '0x0001001B' : 'MSG_CMD_FOREGROUND'
def parse_msg_cmd_foreground(data, message):
	print("parse_msg_cmd_foreground:")
	print(data)
	message['name'] = const.MSG_CMD_FOREGROUND_SERVICE_NAME


# '0x0001001C' : 'MSG_CMD_BACKGROUND'
def parse_msg_cmd_background(data, message):
	print("parse_msg_cmd_background:")
	print(data)
	message['name'] = const.MSG_CMD_BACKGROUND_SERVICE_NAME
	
	
# '0x0001801D' : 'MSG_CMD_LAUNCH_MODE_NORMAL'
def parse_msg_cmd_launch_mode_normal(data, message):
	print("parse_msg_cmd_launch_mode_normal:")
	print(data)
	message['name'] = const.MSG_CMD_LAUNCH_MODE_NORMAL_SERVICE_NAME


# '0x0001801E' : 'MSG_CMD_LAUNCH_MODE_PHONE'
def parse_msg_cmd_launch_mode_phone(data, message):
	print("parse_msg_cmd_launch_mode_phone:")
	print(data)
	message['name'] = const.MSG_CMD_LAUNCH_MODE_PHONE_SERVICE_NAME

	
# '0x0001801F' : 'MSG_CMD_LAUNCH_MODE_MAP'
def parse_msg_cmd_launch_mode_map(data, message):
	print("parse_msg_cmd_launch_mode_map:")
	print(data)
	message['name'] = const.MSG_CMD_LAUNCH_MODE_MAP_SERVICE_NAME	
	

# '0x00018020' : 'MSG_CMD_LAUNCH_MODE_MUSIC'
def parse_msg_cmd_launch_mode_music(data, message):
	print("parse_msg_cmd_launch_mode_music:")
	print(data)
	message['name'] = const.MSG_CMD_LAUNCH_MODE_MUSIC_SERVICE_NAME	
	

# '0x00010021' : 'MSG_CMD_GO_TO_DESKTOP'
def parse_msg_cmd_go_to_desktop(data, message):
	print("parse_msg_cmd_go_to_desktop:")
	print(data)
	message['name'] = const.MSG_CMD_GO_TO_DESKTOP_SERVICE_NAME		
	

# '0x00010022' : 'MSG_CMD_MIC_RECORD_WAKEUP_START'
def parse_msg_cmd_mic_record_wakeup_start(data, message):
	print("parse_msg_cmd_mic_record_wakeup_start:")
	print(data)
	message['name'] = const.MSG_CMD_MIC_RECORD_WAKEUP_START_SERVICE_NAME
	

# '0x00010023' : 'MSG_CMD_MIC_RECORD_END'
def parse_msg_cmd_mic_record_end(data, message):
	print("parse_msg_cmd_mic_record_end:")
	print(data)
	message['name'] = const.MSG_CMD_MIC_RECORD_END_SERVICE_NAME


# '0x00010024' : 'MSG_CMD_MIC_RECORD_RECOG_START'
def parse_msg_cmd_mic_record_recog_start(data, message):
	print("parse_msg_cmd_mic_record_recog_start:")
	print(data)
	message['name'] = const.MSG_CMD_MIC_RECORD_RECOG_START_SERVICE_NAME


# '0x00018025' : 'MSG_CMD_GO_TO_FOREGROUND'
def parse_msg_cmd_mic_go_to_foreground(data, message):
	print("parse_msg_cmd_mic_go_to_foreground:")
	print(data)
	message['name'] = const.MSG_CMD_GO_TO_FOREGROUND_SERVICE_NAME
	

# '0x00010026' : 'MSG_CMD_MODULE_STATUS'
def parse_msg_cmd_module_status(data, message):
	print("parse_msg_cmd_module_status:")
	print(data)
	message['name'] = const.MSG_CMD_MODULE_STATUS_SERVICE_NAME
	
	module_status_list = protobuf.carlife_module_status_list_pb2.CarlifeModuleStatusList()
	module_status_list.ParseFromString(data)
	print(module_status_list)
	
	parameters = {}
	
	for module_status in module_status_list.moduleStatus:
		module_name = get_module_name_from_module_id(module_status.moduleID)
		status_name = get_module_status_from_module_info(module_status)
		parameters[module_name] = status_name	
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00018027' : 'MSG_CMD_STATISTIC_INFO'
def parse_msg_cmd_statistic_info(data, message):
	print("parse_msg_cmd_statistic_info:")
	print(data)
	message['name'] = const.MSG_CMD_STATISTIC_INFO_SERVICE_NAME
	
	statistics_info = protobuf.carlife_statistics_info_pb2.CarlifeStatisticsInfo()
	statistics_info.ParseFromString(data)

	parameters = {}
	parameters['cuid'] = statistics_info.cuid
	parameters['versionName'] = statistics_info.versionName
	parameters['versionCode'] = str(statistics_info.versionCode)
	parameters['channel'] = statistics_info.channel
	parameters['connectCount'] = str(statistics_info.connectCount)
	parameters['connectSuccessCount'] = str(statistics_info.connectSuccessCount)
	parameters['connectTime'] = str(statistics_info.connectTime)
	
	if len(statistics_info.crashLog) > 0:
		parameters['crashLog'] = statistics_info.crashLog
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00018028' : 'MSG_CMD_MODULE_CONTROL'
def parse_msg_cmd_module_control(data, message):
	print("parse_msg_cmd_module_control:")
	print(data)
	message['name'] = const.MSG_CMD_MODULE_CONTROL_SERVICE_NAME
	
	module_status = protobuf.carlife_module_status_pb2.CarlifeModuleStatus()
	module_status.ParseFromString(data)
	
	module_name = get_module_name_from_module_id(module_status.moduleID)
	status_name = get_module_status_from_module_info(module_status)
	
	parameters = {module_name: status_name}
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00018029' : 'MSG_CMD_CAR_DATA_GEAR'
def parse_msg_cmd_car_data_gear(data, message):
	print("parse_msg_cmd_car_data_gear:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_DATA_GEAR_SERVICE_NAME
	
	gear_info = protobuf.carlife_car_gear_info_pb2.CarLifeGearInfo()
	gear_info.ParseFromString(data)
	
	parameters = {'gear': str(gear_info.gear_info)}
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	
	
# '0x00010030' : 'MSG_CMD_NAVI_NEXT_TURN_INFO'
def parse_msg_cmd_navi_next_turn_info(data, message):
	print("parse_msg_cmd_navi_next_turn_info:")
	print(data)
	message['name'] = const.MSG_CMD_NAVI_NEXT_TURN_INFO_SERVICE_NAME
	
	navi_info = protobuf.carlife_navi_next_turn_info_pb2.CarlifeNaviNextTurnInfo()
	navi_info.ParseFromString(data)

	parameters = {}
	parameters['action'] = str(navi_info.action)
	parameters['nextTurn'] = str(navi_info.nextTurn)
	parameters['roadName'] = navi_info.roadName
	parameters['totalDistance'] = str(navi_info.totalDistance)
	parameters['remaindistance'] = str(navi_info.remaindistance)
	parameters['turnIconData'] = str(turnIconData)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00010031' : 'MSG_CMD_CAR_DATA_SUBSCRIBE'
def parse_msg_cmd_car_data_subscribe(data, message):
	print("parse_msg_cmd_car_data_subscribe:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_DATA_SUBSCRIBE_SERVICE_NAME
	

# '0x00018032' : 'MSG_CMD_CAR_DATA_SUBSCRIBE_DONE'
def parse_msg_cmd_car_data_subscribe_done(data, message):
	print("parse_msg_cmd_car_data_subscribe_done:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_DATA_SUBSCRIBE_DONE_SERVICE_NAME
	
	vehicle_info_list = protobuf.carlife_vehicle_info_list_pb2.CarlifeVehicleInfoList()
	vehicle_info_list.ParseFromString(data)
	print(vehicle_info_list)
	
	parameters = {}
	for vehicle_info in vehicle_info_list:
		module_name = get_name_from_vehicle_info_module_id(vehicle_info.moduleID)
		parameters['module name'] = module_name
		parameters[module_name + ' supportFlag'] = get_capability_from_vehicle_info_module_support_flag(vehicle_info.moduleID, vehicle_info.supportFlag)
		parameters[module_name + ' frequency'] = str(vehicle_info.frequency)
		
	message['parameters'] = parameters
	print_message_parameters(parameters)

	
# '0x00010033' : 'MSG_CMD_CAR_DATA_SUBSCRIBE_START'
def parse_msg_cmd_car_data_subscribe_start(data, message):
	print("parse_msg_cmd_car_data_subscribe_start:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_DATA_SUBSCRIBE_START_SERVICE_NAME
	
	vehicle_info = protobuf.carlife_vehicle_info_pb2.CarlifeVehicleInfo()
	vehicle_info.ParseFromString(data)
	
	parameters = {}
	parameters['module name'] = get_name_from_vehicle_info_module_id(vehicle_info.moduleID)
	parameters['supportFlag'] = get_capability_from_vehicle_info_module_support_flag(vehicle_info.moduleID, vehicle_info.supportFlag)
	parameters['frequency'] = str(vehicle_info.frequency)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00010034' : 'MSG_CMD_CAR_DATA_SUBSCRIBE_STOP'
def parse_msg_cmd_car_data_subscribe_stop(data, message):
	print("parse_msg_cmd_car_data_subscribe_stop:")
	print(data)
	message['name'] = const.MSG_CMD_CAR_DATA_SUBSCRIBE_STOP_SERVICE_NAME
	
	vehicle_info = protobuf.carlife_vehicle_info_pb2.CarlifeVehicleInfo()
	vehicle_info.ParseFromString(data)
	
	parameters = {}
	parameters['module name'] = get_name_from_vehicle_info_module_id(vehicle_info.moduleID)
	parameters['supportFlag'] = get_capability_from_vehicle_info_module_support_flag(vehicle_info.moduleID, vehicle_info.supportFlag)
	parameters['frequency'] = str(vehicle_info.frequency)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00010035' : 'MSG_CMD_MEDIA_INFO'
def parse_msg_cmd_media_info(data, message):
	print("parse_msg_cmd_media_info:")
	print(data)
	message['name'] = const.MSG_CMD_MEDIA_INFO_SERVICE_NAME
	
	media_info = protobuf.carlife_media_info_pb2.CarlifeMediaInfo()
	media_info.ParseFromString(data)
	
	parameters = {}
	parameters['source'] = media_info.source
	parameters['song'] = media_info.song
	parameters['artist'] = media_info.artist
	parameters['album'] = media_info.album
	parameters['albumArt'] = str(len(media_info.albumArt)) + ' bytes'
	parameters['duration'] = str(media_info.duration)
	parameters['playlistNum'] = str(media_info.playlistNum)
	parameters['songId'] = media_info.songId
	parameters['mode'] = get_playmode_name_from_playmode_id(media_info.mode)
	
	message['albumArt_raw'] = media_info.albumArt
	message['parameters'] = parameters
	print_message_parameters(parameters)
	
	

# '0x00010036' : 'MSG_CMD_MEDIA_PROGRESS_BAR'
def parse_msg_cmd_media_progress_bar(data, message):
	print("parse_msg_cmd_media_progress_bar:")
	print(data)
	message['name'] = const.MSG_CMD_MEDIA_PROGRESS_BAR_SERVICE_NAME
	
	progress_bar = protobuf.carlife_media_progress_bar_pb2.CarlifeMediaProgressBar()
	progress_bar.ParseFromString(data)
	
	parameters = {}
	parameters['progressBar'] = str(progress_bar.progressBar)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00010037' : 'MSG_CMD_CONNECT_EXCEPTION'
def parse_msg_cmd_connect_exception(data, message):
	print("parse_msg_cmd_connect_exception:")
	print(data)
	message['name'] = const.MSG_CMD_CONNECT_EXCEPTION_SERVICE_NAME

	connect_exception = protobuf.carlife_connect_exception_pb2.CarlifeConnectException()
	connect_exception.ParseFromString(data)
	
	exception_name = 'unknown'
	if connect_exception.exceptionType == const.TYPE_ENCORDER_ERROR_ID:
		exception_name = const.TYPE_ENCORDER_ERROR_NAME
	elif connect_exception.exceptionType == const.TYPE_PERMISSION_DENIED_ID:
		exception_name = const.TYPE_PERMISSION_DENIED_NAME
	elif connect_exception.exceptionType == const.TYPE_SCREENSHARE_REQUEST_ID:
		exception_name = const.TYPE_SCREENSHARE_REQUEST_NAME
	
	parameters = {}
	parameters['exceptionType'] = exception_name + '(' + str(connect_exception.exceptionType) + ')'
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x00010038' : 'MSG_CMD_REQUEST_GO_TO_FOREGROUND'
def parse_msg_cmd_request_go_to_foreground(data, message):
	print("parse_msg_cmd_request_go_to_foreground:")
	print(data)
	message['name'] = const.MSG_CMD_REQUEST_GO_TO_FOREGROUND_SERVICE_NAME


# '0x00010039' : 'MSG_CMD_UI_ACTION_SOUND'
def parse_msg_cmd_ui_action_sound(data, message):
	print("parse_msg_cmd_ui_action_sound:")
	print(data)
	message['name'] = const.MSG_CMD_UI_ACTION_SOUND_SERVICE_NAME

	
# '0x00010047' : 'MSG_CMD_NAVI_ASSITANTGUIDE_INFO'
def parse_msg_cmd_navi_assitant_guide_info(data, message):
	print("parse_msg_cmd_navi_assitant_guide_info:")
	print(data)
	message['name'] = const.MSG_CMD_NAVI_ASSITANTGUIDE_INFO_SERVICE_NAME
	
	guide_info = protobuf.carlife_navi_assitant_guide_info_pb2.CarLifeNaviAssitantGuideInfo()
	guide_info.ParseFromString(data)
	
	parameters = {}
	parameters['action'] = str(guide_info.action)
	parameters['assistantType'] = str(guide_info.assistantType)
	parameters['trafficSignType'] = str(guide_info.trafficSignType)
	parameters['totalDistance'] = str(guide_info.totalDistance)
	parameters['remainDistance'] = str(guide_info.remainDistance)
	parameters['cameraSpeed'] = str(guide_info.cameraSpeed)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x00018048' : 'MSG_CMD_HU_AUTHEN_REQUEST'
def parse_msg_cmd_hu_authen_request(data, message):
	print("parse_msg_cmd_hu_authen_request:")
	print(data)
	message['name'] = const.MSG_CMD_HU_AUTHEN_REQUEST_SERVICE_NAME
	
	authen_request = protobuf.carlife_authen_request_pb2.CarlifeAuthenRequest()
	authen_request.ParseFromString(data)
	
	parameters = {}
	parameters['randomValue'] = str(authen_request.randomValue)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	
	
# '0x00010049' : 'MSG_CMD_MD_AUTHEN_RESPONSE'
def parse_msg_cmd_md_authen_response(data, message):
	print("parse_msg_cmd_md_authen_response:")
	print(data)
	message['name'] = const.MSG_CMD_MD_AUTHEN_RESPONSE_SERVICE_NAME
	
	authen_response = protobuf.carlife_authen_response_pb2.CarlifeAuthenResponse()
	authen_response.ParseFromString(data)
	
	parameters = {}
	parameters['encryptValue'] = str(authen_response.encryptValue)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x0001804A' : 'MSG_CMD_HU_AUTHEN_RESULT'
def parse_msg_cmd_hu_authen_result(data, message):
	print("parse_msg_cmd_hu_authen_result:")
	print(data)
	message['name'] = const.MSG_CMD_HU_AUTHEN_RESULT_SERVICE_NAME
	
	authen_result = protobuf.carlife_authen_result_pb2.CarlifeAuthenResult()
	authen_result.ParseFromString(data)
	
	parameters = {}
	parameters['result'] = str(authen_result.result)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x0001004B' : 'MSG_CMD_MD_AUTHEN_RESULT'
def parse_msg_cmd_md_authen_result(data, message):
	print("parse_msg_cmd_md_authen_result:")
	print(data)
	message['name'] = const.MSG_CMD_MD_AUTHEN_RESULT_SERVICE_NAME
	
	authen_result = protobuf.carlife_authen_result_pb2.CarlifeAuthenResult()
	authen_result.ParseFromString(data)
	
	parameters = {}
	parameters['result'] = str(authen_result.result)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)


# '0x0001004C' : 'MSG_CMD_GO_TO_FOREGROUND_RESPONSE'
def parse_msg_cmd_go_to_foreground_response(data, message):
	print("parse_msg_cmd_go_to_foreground_response:")
	print(data)
	message['name'] = const.MSG_CMD_GO_TO_FOREGROUND_RESPONSE_SERVICE_NAME

	
# '0x00010051' : 'MSG_CMD_MD_FEATURE_CONFIG_REQUEST'
def parse_msg_cmd_md_feature_config_request(data, message):
	print("parse_msg_cmd_md_feature_config_request:")
	print(data)
	message['name'] = const.MSG_CMD_MD_FEATURE_CONFIG_REQUEST_SERVICE_NAME
	
	
# '0x00018052' : 'MSG_CMD_HU_FEATURE_CONFIG_RESPONSE'
def parse_msg_cmd_hu_feature_config_response(data, message):
	print("parse_msg_cmd_hu_feature_config_response:")
	print(data)
	message['name'] = const.MSG_CMD_HU_FEATURE_CONFIG_RESPONSE_SERVICE_NAME
	
	feature_config_list = protobuf.carlife_feature_config_list_pb2.CarlifeFeatureConfigList()
	feature_config_list.ParseFromString(data)
	
	parameters = {}
	
	for feature_config in feature_config_list.featureConfig:
		#print(feature_config)
		parameters[feature_config.key] = str(feature_config.value)
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x00018055' : 'MSG_CMD_ERROR_CODE'
def parse_msg_cmd_error_code(data, message):
	print("parse_msg_cmd_error_code:")
	print(data)
	message['name'] = const.MSG_CMD_ERROR_CODE_SERVICE_NAME
	
	error_code = protobuf.carlife_error_code_pb2.CarlifeErrorCode()
	error_code.ParseFromString(data)
	
	parameters = {}
	parameters['errorCode'] = error_code.errorCode
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	

# '0x00018056' : 'MSG_CMD_VIDEO_ENCODER_JPEG'	
def parse_msg_cmd_video_encoder_jpeg(data, message):
	print("parse_msg_cmd_video_encoder_jpeg:")
	print(data)
	message['name'] = const.MSG_CMD_VIDEO_ENCODER_JPEG_SERVICE_NAME
	
	

# '0x00010057' : 'MSG_CMD_VIDEO_ENCODER_JPEG_ACK'	
def parse_msg_cmd_video_encoder_jpeg_ack(data, message):
	print("parse_msg_cmd_video_encoder_jpeg_ack:")
	print(data)
	message['name'] = const.MSG_CMD_VIDEO_ENCODER_JPEG_ACK_SERVICE_NAME
	

# '0x00010059' : 'MSG_CMD_MD_EXIT'
def parse_msg_cmd_md_exit(data, message):
	print("parse_msg_cmd_md_exit:")
	print(data)
	message['name'] = const.MSG_CMD_MD_EXIT_SERVICE_NAME


# '0x00018070' : 'MSG_CMD_HU_CONNECT_STATISTIC'
def parse_msg_cmd_hu_connect_statistic(data, message):
	print("parse_msg_cmd_hu_connect_statistic:")
	print(data)
	message['name'] = const.MSG_CMD_HU_CONNECT_STATISTIC_SERVICE_NAME
	
	connect_statistic = protobuf.carlife_con_statistic_pb2.CarlifeConStatisticProto()
	connect_statistic.ParseFromString(data)

	parameters = {}
	parameters['nConnectTotal'] = str(connect_statistic.nConnectTotal)
	parameters['nSuccessCount'] = str(connect_statistic.nSuccessCount)
	parameters['nFailedCount'] = str(connect_statistic.nFailedCount)
	parameters['nConnectTime'] = str(connect_statistic.nConnectTime)
	parameters['nErrorCount'] = str(connect_statistic.nErrorCount)
	parameters['ErrorType'] = connect_statistic.ErrorType
	
	message['parameters'] = parameters
	print_message_parameters(parameters)
	
	

def print_message_parameters(parameters):
	print("cmd message data parsed, parameters:")
	print(parameters)
	
	
def get_module_name_from_module_id(module_id):
	module_name = 'unknown'
	
	if module_id == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_PHONE_MODULE_ID:
		module_name = const.MODULE_PHONE_NAME
	elif module_id == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_NAVI_MODULE_ID:
		module_name = const.MODULE_NAVI_NAME
	elif module_id == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_MUSIC_MODULE_ID:
		module_name = const.MODULE_MUSIC_NAME
	elif module_id == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_VR_MODULE_ID:
		module_name = const.MODULE_VR_NAME
	elif module_id == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_CONNECT_MODULE_ID:
		module_name = const.MODULE_CONNECT_NAME
	elif module_id == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_MIC_MODULE_ID:
		module_name = const.MODULE_MIC_NAME
	elif module_id == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_MEDIAPCM_MODULE_ID:
		module_name = const.MODULE_MEDIAPCM_NAME
	elif module_id == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_EDOG_MODULE_ID:
		module_name = const.MODULE_EDOG_NAME
	elif module_id == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_CRUISE_ID:
		module_name = const.MODULE_CRUISE_NAME
	
	return module_name
	
	
def get_module_status_from_module_info(module_info):
	module_status = 'unknown'
	if module_info.moduleID == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_PHONE_MODULE_ID:
		if module_info.statusID == protobuf.carlife_module_status_pb2.PhoneState.PHONE_STATUS_IDLE:
			module_status = const.MODULE_PHONE_STATUS_IDLE
		elif module_info.statusID == protobuf.carlife_module_status_pb2.PhoneState.PHONE_STATUS_INCOMING:
			module_status = const.MODULE_PHONE_STATUS_INCOMING
		elif module_info.statusID == protobuf.carlife_module_status_pb2.PhoneState.PHONE_STATUS_OUTING:
			module_status = const.MODULE_PHONE_STATUS_OUTING
		elif module_info.statusID == protobuf.carlife_module_status_pb2.PhoneState.PHONE_STATUS_CONNECTED:
			module_status = const.MODULE_PHONE_STATUS_CONNECTED
		else:
			module_status = const.MODULE_STATUS_UNKNOWN
	elif module_info.moduleID == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_NAVI_MODULE_ID:
		if module_info.statusID == protobuf.carlife_module_status_pb2.NaviState.NAVI_STATUS_IDLE:
			module_status = const.MODULE_NAVI_STATUS_IDLE
		elif module_info.statusID == protobuf.carlife_module_status_pb2.NaviState.NAVI_STATUS_START:
			module_status = const.MODULE_NAVI_STATUS_START
		else:
			module_status = const.MODULE_STATUS_UNKNOWN
	elif module_info.moduleID == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_MUSIC_MODULE_ID:
		if module_info.statusID == protobuf.carlife_module_status_pb2.MusicState.MUSIC_STATUS_IDLE:
			module_status = const.MODULE_MUSIC_STATUS_IDLE
		elif module_info.statusID == protobuf.carlife_module_status_pb2.MusicState.MUSIC_STATUS_RUNNING:
			module_status = const.MODULE_MUSIC_STATUS_RUNNING
		else:
			module_status = const.MODULE_STATUS_UNKNOWN
	elif module_info.moduleID == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_VR_MODULE_ID:
		if module_info.statusID == protobuf.carlife_module_status_pb2.VRState.VR_STATUS_RECORD_IDLE:
			module_status = const.MODULE_VR_STATUS_RECORD_IDLE
		elif module_info.statusID == protobuf.carlife_module_status_pb2.VRState.VR_STATUS_RECORD_RUNNING:
			module_status = const.MODULE_VR_STATUS_RECORD_RUNNING
		else:
			module_status = const.MODULE_STATUS_UNKNOWN
	elif module_info.moduleID == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_CONNECT_MODULE_ID:
		if module_info.statusID == protobuf.carlife_module_status_pb2.ConnectState.CONNECT_STATUS_ADB:
			module_status = const.MODULE_CONNECT_STATUS_ADB
		elif module_info.statusID == protobuf.carlife_module_status_pb2.ConnectState.CONNECT_STATUS_AOA:
			module_status = const.MODULE_CONNECT_STATUS_AOA
		elif module_info.statusID == protobuf.carlife_module_status_pb2.ConnectState.CONNECT_STATUS_NCM_ANDROID:
			module_status = const.MODULE_CONNECT_STATUS_NCM_ANDROID
		elif module_info.statusID == protobuf.carlife_module_status_pb2.ConnectState.CONNECT_STATUS_NCM_IOS:
			module_status = const.MODULE_CONNECT_STATUS_IOS
		elif module_info.statusID == protobuf.carlife_module_status_pb2.ConnectState.CONNECT_STATUS_WIFI:
			module_status = const.MODULE_CONNECT_STATUS_WIFI
		else:
			module_status = const.MODULE_STATUS_UNKNOWN
	elif module_info.moduleID == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_MIC_MODULE_ID:
		if module_info.statusID == protobuf.carlife_module_status_pb2.MicState.MIC_STATUS_USE_VEHICLE_MIC:
			module_status = const.MODULE_MIC_STATUS_USE_VEHICLE_MIC
		elif module_info.statusID == protobuf.carlife_module_status_pb2.MicState.MIC_STATUS_USE_MOBILE_MIC:
			module_status = const.MODULE_MIC_STATUS_USE_MOBILE_MIC
		else:
			module_status = const.MODULE_STATUS_UNKNOWN
	elif module_info.moduleID == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_MEDIAPCM_MODULE_ID:
		if module_info.statusID == protobuf.carlife_module_status_pb2.MediaPCMState.MEDIAPCM_STATUS_IDLE:
			module_status = const.MODULE_MEDIAPCM_STATUS_IDLE
		elif module_info.statusID == protobuf.carlife_module_status_pb2.MediaPCMState.MEDIAPCM_STATUS_RUNNING:
			module_status = const.MODULE_MEDIAPCM_STATUS_RUNNING
		else:
			module_status = const.MODULE_STATUS_UNKNOWN
	elif module_info.moduleID == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_EDOG_MODULE_ID:
		if module_info.statusID == protobuf.carlife_module_status_pb2.EDogState.EDOG_STATUS_IDLE:
			module_status = const.MODULE_EDOG_STATUS_IDLE
		elif module_info.statusID == protobuf.carlife_module_status_pb2.EDogState.EDOG_STATUS_RUNNING:
			module_status = const.MODULE_EDOG_STATUS_RUNNING
		else:
			module_status = const.MODULE_STATUS_UNKNOWN
	elif module_info.moduleID == protobuf.carlife_module_status_pb2.ModuleId.CARLIFE_CRUISE_ID:
		if module_info.statusID == protobuf.carlife_module_status_pb2.CruiseState.CRUISE_STATUS_IDLE:
			module_status = const.MODULE_CRUISE_STATUS_IDLE
		elif module_info.statusID == protobuf.carlife_module_status_pb2.CruiseState.CRUISE_STATUS_RUNNING:
			module_status = const.MODULE_CRUISE_STATUS_RUNNING
		else:
			module_status = const.MODULE_STATUS_UNKNOWN
	
	return module_status
	

def get_name_from_vehicle_info_module_id(module_id):
	module_name = 'unknown'
	
	if module_id == protobuf.carlife_vehicle_info_pb2.ModuleID.CAR_DATA_GPS:
		module_name = const.CAR_DATA_GPS_NAME
	elif module_id == protobuf.carlife_vehicle_info_pb2.ModuleID.CAR_DATA_VELOCITY:
		module_name = const.CAR_DATA_VELOCITY_NAME
	elif module_id == protobuf.carlife_vehicle_info_pb2.ModuleID.CAR_DATA_GYROSCOPE:
		module_name = const.CAR_DATA_GYROSCOPE_NAME
	elif module_id == protobuf.carlife_vehicle_info_pb2.ModuleID.CAR_DATA_ACCELERATION:
		module_name = const.CAR_DATA_ACCELERATION_NAME
	elif module_id == protobuf.carlife_vehicle_info_pb2.ModuleID.CAR_DATA_GEAR:
		module_name = const.CAR_DATA_GEAR_NAME
	elif module_id == protobuf.carlife_vehicle_info_pb2.ModuleID.CAR_DATA_OIL:
		module_name = const.CAR_DATA_OIL_NAME
	
	return module_name

def get_capability_from_vehicle_info_module_support_flag(module_id, support_flag):
	capability = 'unknown'
	
	if module_id == protobuf.carlife_vehicle_info_pb2.ModuleID.CAR_DATA_GPS:
		if support_flag == const.COORDINATE_SYSTEM_WGS84_ID:
			capability = const.COORDINATE_SYSTEM_WGS84_NAME
		elif support_flag == const.COORDINATE_SYSTEM_GCJ02_ID:
			capability = const.COORDINATE_SYSTEM_GCJ02_NAME
	else:
		if support_flag == 1:
			capability = 'yes'
		elif support_flag == 0:
			capability = 'no'
			
	return capability
	
def get_playmode_name_from_playmode_id(playmode_id):
	playmode_name = 'unknown'
	
	if playmode_id == protobuf.carlife_media_info_pb2.CarlifeMediaPlayMode.PLAYMODE_REPEATE_ONE:
		playmode_name = const.PLAYMODE_REPEAT_ONE_NAME
	elif playmode_id == protobuf.carlife_media_info_pb2.CarlifeMediaPlayMode.PLAYMODE_SHUFFLE:
		playmode_name = const.PLAYMODE_SHUFFLE_NAME
	elif playmode_id == protobuf.carlife_media_info_pb2.CarlifeMediaPlayMode.PLAYMODE_REPEATE_ALL:
		playmode_name = const.PLAYMODE_REPEAT_ALL_NAME
	
	return playmode_name
