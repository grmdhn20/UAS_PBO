# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class frameLogin
###########################################################################

class frameLogin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 108,232 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button3, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.eventButtonOwner )
		self.m_button2.Bind( wx.EVT_BUTTON, self.eventButtonAdmin )
		self.m_button3.Bind( wx.EVT_BUTTON, self.eventButtonUser )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventButtonOwner( self, event ):
		event.Skip()

	def eventButtonAdmin( self, event ):
		event.Skip()

	def eventButtonUser( self, event ):
		event.Skip()


###########################################################################
## Class frameLoginOwner
###########################################################################

class frameLoginOwner ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login Owner", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self, wx.ID_ANY, u"owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self, wx.ID_ANY, u"owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtPassword, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button17, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_menubar7 = wx.MenuBar( 0 )
		self.m_menu7 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"kembali", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem7 )

		self.m_menubar7.Append( self.m_menu7, u"Menu" )

		self.SetMenuBar( self.m_menubar7 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button17.Bind( wx.EVT_BUTTON, self.eventLoginOwner )
		self.Bind( wx.EVT_MENU, self.eventBack, id = self.m_menuItem7.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventLoginOwner( self, event ):
		event.Skip()

	def eventBack( self, event ):
		event.Skip()


###########################################################################
## Class frameLoginAdmin
###########################################################################

class frameLoginAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login Admin", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self, wx.ID_ANY, u"admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self, wx.ID_ANY, u"admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtPassword, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button17, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_menubar7 = wx.MenuBar( 0 )
		self.m_menu7 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"kembali", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem7 )

		self.m_menubar7.Append( self.m_menu7, u"Menu" )

		self.SetMenuBar( self.m_menubar7 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button17.Bind( wx.EVT_BUTTON, self.eventLoginAdmin )
		self.Bind( wx.EVT_MENU, self.eventBack, id = self.m_menuItem7.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventLoginAdmin( self, event ):
		event.Skip()

	def eventBack( self, event ):
		event.Skip()


###########################################################################
## Class frameLoginUser
###########################################################################

class frameLoginUser ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login Admin", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self, wx.ID_ANY, u"user", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self, wx.ID_ANY, u"user", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtPassword, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button17, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_menubar7 = wx.MenuBar( 0 )
		self.m_menu7 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"kembali", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.Append( self.m_menuItem7 )

		self.m_menubar7.Append( self.m_menu7, u"Menu" )

		self.SetMenuBar( self.m_menubar7 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button17.Bind( wx.EVT_BUTTON, self.eventLoginUser )
		self.Bind( wx.EVT_MENU, self.eventBack, id = self.m_menuItem7.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventLoginUser( self, event ):
		event.Skip()

	def eventBack( self, event ):
		event.Skip()


###########################################################################
## Class frameHomeOwner
###########################################################################

class frameHomeOwner ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Owner Panel", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang Owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Lihat Semua Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Lihat Semua Akun", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.buttonLogoutOwner = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.buttonLogoutOwner )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.eventShowMenuOwner )
		self.m_button5.Bind( wx.EVT_BUTTON, self.eventShowAccountOwner )
		self.Bind( wx.EVT_MENU, self.eventLogout, id = self.buttonLogoutOwner.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventShowMenuOwner( self, event ):
		event.Skip()

	def eventShowAccountOwner( self, event ):
		event.Skip()

	def eventLogout( self, event ):
		event.Skip()


###########################################################################
## Class frameMenuOwner
###########################################################################

class frameMenuOwner ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Owner Panel : Semua Menu", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.dsfs = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang Owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dsfs.Wrap( -1 )

		bSizer6.Add( self.dsfs, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Edit Menu yang dipilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer6.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.tableMenu = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tableMenu.CreateGrid( 5, 4 )
		self.tableMenu.EnableEditing( False )
		self.tableMenu.EnableGridLines( True )
		self.tableMenu.EnableDragGridSize( False )
		self.tableMenu.SetMargins( 0, 0 )

		# Columns
		self.tableMenu.SetColSize( 0, 30 )
		self.tableMenu.SetColSize( 1, 100 )
		self.tableMenu.SetColSize( 2, 50 )
		self.tableMenu.SetColSize( 3, 60 )
		self.tableMenu.EnableDragColMove( False )
		self.tableMenu.EnableDragColSize( True )
		self.tableMenu.SetColLabelSize( 30 )
		self.tableMenu.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tableMenu.EnableDragRowSize( True )
		self.tableMenu.SetRowLabelSize( 20 )
		self.tableMenu.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tableMenu.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.tableMenu, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.buttonLogoutOwner = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Kembali", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.buttonLogoutOwner )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.eventEditMenu )
		self.tableMenu.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.eventSelectCell )
		self.Bind( wx.EVT_MENU, self.eventHomeOwner, id = self.buttonLogoutOwner.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventEditMenu( self, event ):
		event.Skip()

	def eventSelectCell( self, event ):
		event.Skip()

	def eventHomeOwner( self, event ):
		event.Skip()


###########################################################################
## Class dialogEditMenu
###########################################################################

class dialogEditMenu ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Menu", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer5.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.txtStock = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.txtStock, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.txtPrice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.txtPrice, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button8, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()
		fgSizer5.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.eventSave )
		self.m_button8.Bind( wx.EVT_BUTTON, self.eventCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventSave( self, event ):
		event.Skip()

	def eventCancel( self, event ):
		event.Skip()


###########################################################################
## Class frameAccountOwner
###########################################################################

class frameAccountOwner ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Owner Panel : Semua Menu", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.asfaw = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang Owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asfaw.Wrap( -1 )

		bSizer6.Add( self.asfaw, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Edit Akun yang dipilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer6.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.tableMenu = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tableMenu.CreateGrid( 5, 3 )
		self.tableMenu.EnableEditing( False )
		self.tableMenu.EnableGridLines( True )
		self.tableMenu.EnableDragGridSize( False )
		self.tableMenu.SetMargins( 0, 0 )

		# Columns
		self.tableMenu.SetColSize( 0, 30 )
		self.tableMenu.SetColSize( 1, 100 )
		self.tableMenu.SetColSize( 2, 100 )
		self.tableMenu.EnableDragColMove( False )
		self.tableMenu.EnableDragColSize( True )
		self.tableMenu.SetColLabelSize( 30 )
		self.tableMenu.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tableMenu.EnableDragRowSize( True )
		self.tableMenu.SetRowLabelSize( 20 )
		self.tableMenu.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tableMenu.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.tableMenu, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.buttonLogoutOwner = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Kembali", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.buttonLogoutOwner )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.eventEditAccount )
		self.tableMenu.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.eventSelectCell )
		self.Bind( wx.EVT_MENU, self.eventHomeOwner, id = self.buttonLogoutOwner.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventEditAccount( self, event ):
		event.Skip()

	def eventSelectCell( self, event ):
		event.Skip()

	def eventHomeOwner( self, event ):
		event.Skip()


###########################################################################
## Class dialogEditAccount
###########################################################################

class dialogEditAccount ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Menu", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer5.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.txtPassword, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button8, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()
		fgSizer5.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.eventSave )
		self.m_button8.Bind( wx.EVT_BUTTON, self.eventCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventSave( self, event ):
		event.Skip()

	def eventCancel( self, event ):
		event.Skip()


###########################################################################
## Class frameHomeAdmin
###########################################################################

class frameHomeAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Admin Panel", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Lihat Semua Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.buttonLogoutOwner = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.buttonLogoutOwner )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.eventShowMenuOwner )
		self.Bind( wx.EVT_MENU, self.eventLogout, id = self.buttonLogoutOwner.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventShowMenuOwner( self, event ):
		event.Skip()

	def eventLogout( self, event ):
		event.Skip()


###########################################################################
## Class frameMenuUser
###########################################################################

class frameMenuUser ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Owner Panel : Semua Menu", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.dsfs = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dsfs.Wrap( -1 )

		bSizer6.Add( self.dsfs, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		bSizer6.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.tableMenu = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tableMenu.CreateGrid( 5, 4 )
		self.tableMenu.EnableEditing( False )
		self.tableMenu.EnableGridLines( True )
		self.tableMenu.EnableDragGridSize( False )
		self.tableMenu.SetMargins( 0, 0 )

		# Columns
		self.tableMenu.SetColSize( 0, 30 )
		self.tableMenu.SetColSize( 1, 100 )
		self.tableMenu.SetColSize( 2, 50 )
		self.tableMenu.SetColSize( 3, 60 )
		self.tableMenu.EnableDragColMove( False )
		self.tableMenu.EnableDragColSize( True )
		self.tableMenu.SetColLabelSize( 30 )
		self.tableMenu.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tableMenu.EnableDragRowSize( True )
		self.tableMenu.SetRowLabelSize( 20 )
		self.tableMenu.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tableMenu.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.tableMenu, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.buttonLogoutUser = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.buttonLogoutUser )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.tableMenu.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.eventSelectCell )
		self.Bind( wx.EVT_MENU, self.eventLogout, id = self.buttonLogoutUser.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventSelectCell( self, event ):
		event.Skip()

	def eventLogout( self, event ):
		event.Skip()


