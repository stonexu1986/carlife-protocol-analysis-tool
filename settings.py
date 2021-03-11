
import datetime
from common_constant import const

# filter the packet which do not display in HMI
packets_ignore_setting = [
	const.MSG_VIDEO_DATA_SERVICE_TYPE,
	const.MSG_MEDIA_DATA_SERVICE_TYPE,
	const.MSG_NAVI_TTS_DATA_SERVICE_TYPE,
	const.MSG_VR_DATA_SERVICE_TYPE,
	const.MSG_VR_AUDIO_DATA_SERVICE_TYPE,
]

stream_filter_setting = {}


application_info = {
	'name' : 'CarLife Protocol Analysis Tool',
	'version': 'v1.0.0',
	'description': 'This application is developed for analyzing carlife\n' + 'protocol between headunit and mobile phone',
	'copyright': '(C) 2018 - ' + str(datetime.date.today().year),
	'website': 'https://www.aptiv.com/',
	'developer': 'APTIV Media Team',
}

