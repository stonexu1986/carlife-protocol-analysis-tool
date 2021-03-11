
import layout_stream_filter_dialog
import settings

from common_constant import const

class StreamFilterDialog (layout_stream_filter_dialog.BaseStreamFilterDialog):
	def __init__(self, parent):
		super().__init__(parent)
		
		self.stream_filter = {}
		self._init_views();
		
	def _init_views(self):
		if settings.stream_filter_setting.__contains__('video'):
			self.checkbox_video.SetValue(settings.stream_filter_setting['video'])
			
		if settings.stream_filter_setting.__contains__('music'):
			self.checkbox_music.SetValue(settings.stream_filter_setting['music'])
			
		if settings.stream_filter_setting.__contains__('tts'):
			self.checkbox_tts.SetValue(settings.stream_filter_setting['tts'])
		
		if settings.stream_filter_setting.__contains__('vr'):
			self.checkbox_vr.SetValue(settings.stream_filter_setting['vr'])
		
	
	def button_okOnButtonClick( self, event ):
		event.Skip()
		
		self.stream_filter.clear()
		settings.packets_ignore_setting.clear()
		
		settings.stream_filter_setting.clear()
		settings.stream_filter_setting['video'] = self.checkbox_video.IsChecked()
		settings.stream_filter_setting['music'] = self.checkbox_music.IsChecked()
		settings.stream_filter_setting['tts'] = self.checkbox_tts.IsChecked()
		settings.stream_filter_setting['vr'] = self.checkbox_vr.IsChecked()
		
		print("stream_filter_setting: ", settings.stream_filter_setting)
		
		if not self.checkbox_video.IsChecked():
			settings.packets_ignore_setting.append(const.MSG_VIDEO_DATA_SERVICE_TYPE)
		
		if not self.checkbox_music.IsChecked():
			settings.packets_ignore_setting.append(const.MSG_MEDIA_DATA_SERVICE_TYPE)
		
		if not self.checkbox_tts.IsChecked():
			settings.packets_ignore_setting.append(const.MSG_NAVI_TTS_DATA_SERVICE_TYPE)
		
		if not self.checkbox_vr.IsChecked():
			settings.packets_ignore_setting.append(const.MSG_VR_AUDIO_DATA_SERVICE_TYPE)
			settings.packets_ignore_setting.append(const.MSG_VR_DATA_SERVICE_TYPE)
		
		print("packets_ignore_setting: ", settings.packets_ignore_setting)
		
