# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class BaseMainWindow
###########################################################################

class BaseMainWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CarLife Protocol Analysis Tool", pos = wx.DefaultPosition, size = wx.Size( 1280,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.menubar = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.menuItem_import = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Import", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.AppendItem( self.menuItem_import )
		
		self.menubar.Append( self.menu_file, u"File" ) 
		
		self.menu_view = wx.Menu()
		self.menuItem_filter = wx.MenuItem( self.menu_view, wx.ID_ANY, u"Stream Filter Setting", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_view.AppendItem( self.menuItem_filter )
		
		self.menubar.Append( self.menu_view, u"View" ) 
		
		self.menu_help = wx.Menu()
		self.menuItem_about = wx.MenuItem( self.menu_help, wx.ID_ANY, u"About...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_help.AppendItem( self.menuItem_about )
		
		self.menubar.Append( self.menu_help, u"Help" ) 
		
		self.SetMenuBar( self.menubar )
		
		self.toolbar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.tool_import = self.toolbar.AddLabelTool( wx.ID_ANY, u"Import", wx.Bitmap( u"res/import.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.AddSeparator()
		
		self.tool_filter = self.toolbar.AddLabelTool( wx.ID_ANY, u"Filter Stream", wx.Bitmap( u"res/filter.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.Realize() 
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( 1280,800 ) ) 
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.listctrl_protocols = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		self.listctrl_protocols.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer2.Add( self.listctrl_protocols, 3, wx.BOTTOM|wx.EXPAND, 1 )
		
		self.treectrl_details = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_NO_LINES )
		self.treectrl_details.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.treectrl_details, 1, wx.ALL|wx.EXPAND, 1 )
		
		
		bSizer1.Add( bSizer2, 4, wx.EXPAND, 5 )
		
		self.text_rawdata = wx.TextCtrl( self, wx.ID_ANY, u"00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		self.text_rawdata.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 75, 90, 90, False, "Courier New" ) )
		
		bSizer1.Add( self.text_rawdata, 1, wx.ALL|wx.EXPAND, 1 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.statusbar = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.menuItem_importOnMenuSelection, id = self.menuItem_import.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_filterOnMenuSelection, id = self.menuItem_filter.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_aboutOnMenuSelection, id = self.menuItem_about.GetId() )
		self.Bind( wx.EVT_TOOL, self.tool_importOnToolClicked, id = self.tool_import.GetId() )
		self.Bind( wx.EVT_TOOL, self.tool_filterOnToolClicked, id = self.tool_filter.GetId() )
		self.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.listctrl_protocolsOnDataViewListCtrlSelectionChanged, id = wx.ID_ANY )
		self.treectrl_details.Bind( wx.EVT_TREE_SEL_CHANGED, self.treectrl_detailsOnTreeSelChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def menuItem_importOnMenuSelection( self, event ):
		event.Skip()
	
	def menuItem_filterOnMenuSelection( self, event ):
		event.Skip()
	
	def menuItem_aboutOnMenuSelection( self, event ):
		event.Skip()
	
	def tool_importOnToolClicked( self, event ):
		event.Skip()
	
	def tool_filterOnToolClicked( self, event ):
		event.Skip()
	
	def listctrl_protocolsOnDataViewListCtrlSelectionChanged( self, event ):
		event.Skip()
	
	def treectrl_detailsOnTreeSelChanged( self, event ):
		event.Skip()
	

