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
## Class BaseStreamFilterDialog
###########################################################################

class BaseStreamFilterDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Stream Filter Setting", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3.SetMinSize( wx.Size( 400,250 ) ) 
		self.checkbox_video = wx.CheckBox( self, wx.ID_ANY, u"Video Stream", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer3.Add( self.checkbox_video, 1, wx.EXPAND|wx.LEFT, 100 )
		
		self.checkbox_music = wx.CheckBox( self, wx.ID_ANY, u"Music Stream", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.checkbox_music, 1, wx.EXPAND|wx.LEFT, 100 )
		
		self.checkbox_tts = wx.CheckBox( self, wx.ID_ANY, u"TTS Stream", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer3.Add( self.checkbox_tts, 1, wx.EXPAND|wx.LEFT, 100 )
		
		self.checkbox_vr = wx.CheckBox( self, wx.ID_ANY, u"VR Stream", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.checkbox_vr, 1, wx.EXPAND|wx.LEFT, 100 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_ok = wx.Button( self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.Size( 120,40 ), 0 )
		bSizer4.Add( self.button_ok, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 50 )
		
		self.button_cancel = wx.Button( self, wx.ID_CANCEL, u"CANCEL", wx.DefaultPosition, wx.Size( 120,40 ), 0 )
		bSizer4.Add( self.button_cancel, 0, wx.ALIGN_CENTER_VERTICAL, 50 )
		
		
		bSizer3.Add( bSizer4, 2, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		bSizer3.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_ok.Bind( wx.EVT_BUTTON, self.button_okOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def button_okOnButtonClick( self, event ):
		event.Skip()
	

