import wx
import io
import os

from PIL import Image

import layout_album_artwork_dialog
import carlife_ico

class AlbumArtworkDialog (layout_album_artwork_dialog.BaseAlbumArtworkDialog):
	def __init__( self, parent ):
		super().__init__(parent)
		
		self._init_views()
		
	
	def _init_views(self):
		self.st_format.SetLabel('')
		self.st_width.SetLabel('')
		self.st_height.SetLabel('')
		self.st_size.SetLabel('')
		
	
	def set_album_artwork_stream(self, stream):
		saved_image_path = 'album_artwork.png'
		
		byte_stream = io.BytesIO(stream)
		pilImg = Image.open(byte_stream)
		pilImg.save(saved_image_path)
		
		self.st_format.SetLabel('Format:  ' + pilImg.format)
		self.st_width.SetLabel('Width:  ' + str(pilImg.width) + ' pixels')
		self.st_height.SetLabel('Height:  ' + str(pilImg.height) + ' pixels')
		self.st_size.SetLabel('Size:  ' + str(len(stream)) + ' bytes')
		
		bitmap = wx.Bitmap(saved_image_path)
		self.bitmap_artwork.SetBitmap(bitmap)
		
		os.remove(saved_image_path)
