# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BaseAlbumArtworkDialog
###########################################################################

class BaseAlbumArtworkDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5.SetMinSize( wx.Size( 500,300 ) ) 
		self.bitmap_artwork = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.bitmap_artwork, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizerImageDetails = wx.BoxSizer( wx.VERTICAL )
		
		self.st_format = wx.StaticText( self, wx.ID_ANY, u"Format:  JPEG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_format.Wrap( -1 )
		bSizerImageDetails.Add( self.st_format, 0, wx.ALL, 5 )
		
		self.st_width = wx.StaticText( self, wx.ID_ANY, u"Width:  255 pixels", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_width.Wrap( -1 )
		bSizerImageDetails.Add( self.st_width, 0, wx.ALL, 5 )
		
		self.st_height = wx.StaticText( self, wx.ID_ANY, u"Height:  255 pixels", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_height.Wrap( -1 )
		bSizerImageDetails.Add( self.st_height, 0, wx.ALL, 5 )
		
		self.st_size = wx.StaticText( self, wx.ID_ANY, u"Size:  1024 bytes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_size.Wrap( -1 )
		bSizerImageDetails.Add( self.st_size, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizerImageDetails, 1, wx.ALL|wx.EXPAND, 10 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		bSizer5.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

