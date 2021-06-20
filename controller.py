import wx
import sqlite3
import gui
import owner

class App(wx.App):
	appFrame=None

	def OnInit(self):
		self.appFrame = start(None)
		self.appFrame.Show()
		return True

class start(gui.frameLogin):
	def __init__(self,parent):
		gui.frameLogin.__init__(self,parent)

	def eventButtonOwner(self,event):
		self.ownerLoginPage = subLoginOwner(None)
		self.Destroy()
		self.ownerLoginPage.Show()
	
	def eventButtonAdmin(self,event):
		self.adminLoginPage = subLoginAdmin(None)
		self.Destroy()
		self.adminLoginPage.Show()

	def eventButtonUser(self,event):
		self.userLoginPage = subLoginUser(None)
		self.Destroy()
		self.userLoginPage.Show()

class subLoginUser(gui.frameLoginUser):
	def __init__(self,parent):
		gui.frameLoginUser.__init__(self,parent)

	def eventBack(self,event):
		self.back = start(None)
		self.Destroy()
		self.back.Show()

	def eventLoginUser(self,event):
		inputtedUsername = self.txtUsername.GetValue()
		inputtedPassword = self.txtPassword.GetValue()
		conn = sqlite3.connect("myDb.sqlite3")
		cur = conn.cursor()
		cur.execute("SELECT username FROM users WHERE username='%s' AND password = '%s';" % (inputtedUsername, inputtedPassword))
		if not cur.fetchone():
			wx.MessageBox('Data login salah', 'Terjadi kesalahan')
		else:
			self.loginUser = subMenuUser(None)
			self.Destroy()
			self.loginUser.Show()

class subLoginOwner(gui.frameLoginOwner):
	def __init__(self,parent):
		gui.frameLoginOwner.__init__(self,parent)

	def eventBack(self,event):
		self.back = start(None)
		self.Destroy()
		self.back.Show()

	def eventLoginOwner(self,event):
		inputtedUsername = self.txtUsername.GetValue()
		inputtedPassword = self.txtPassword.GetValue()
		conn = sqlite3.connect("myDb.sqlite3")
		cur = conn.cursor()
		cur.execute("SELECT username FROM owner WHERE username='%s' AND password = '%s';" % (inputtedUsername, inputtedPassword))
		if not cur.fetchone():
			wx.MessageBox('Data login salah', 'Terjadi kesalahan')
		else:
			self.loginOwner = subHomeOwner(None)
			self.Destroy()
			self.loginOwner.Show()

class subLoginAdmin(gui.frameLoginAdmin):
	def __init__(self,parent):
		gui.frameLoginAdmin.__init__(self,parent)

	def eventBack(self,event):
		self.back = start(None)
		self.Destroy()
		self.back.Show()

	def eventLoginAdmin(self,event):
		inputtedUsername = self.txtUsername.GetValue()
		inputtedPassword = self.txtPassword.GetValue()
		conn = sqlite3.connect("myDb.sqlite3")
		cur = conn.cursor()
		cur.execute("SELECT username FROM admins WHERE username='%s' AND password = '%s';" % (inputtedUsername, inputtedPassword))
		if not cur.fetchone():
			wx.MessageBox('Data login salah', 'Terjadi kesalahan')
		else:
			self.loginAdmin = subHomeAdmin(None)
			self.Destroy()
			self.loginAdmin.Show()

class subHomeOwner(gui.frameHomeOwner):
	def eventShowMenuOwner(self, event):
		self.showMenuOwner = subMenuOwner(None)
		self.Destroy()
		self.showMenuOwner.Show()

	def eventShowAccountOwner(self, event):
		self.showAccountOwner = subAccountOwner(None)
		self.Destroy()
		self.showAccountOwner.Show()

	def eventLogout(self,event):
		dlg = wx.MessageBox("Anda yakin ingin logout?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
		if dlg == 2:
			self.back = start(None)
			self.Destroy()
			self.back.Show()

class subHomeAdmin(gui.frameHomeAdmin):
	def eventShowMenuOwner(self, event):
		self.showMenuOwner = subMenuAdmin(None)
		self.Destroy()
		self.showMenuOwner.Show()

	def eventLogout(self,event):
		dlg = wx.MessageBox("Anda yakin ingin logout?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
		if dlg == 2:
			self.back = start(None)
			self.Destroy()
			self.back.Show()			

class subMenuUser(gui.frameMenuUser):
	def __init__(self,parent):
		gui.frameMenuUser.__init__(self,parent)
		self.id=id
		self.InitData()		

	def InitData(self,orderby="cake.id"):
		listCake = owner.modelCakeData()
		dataListCake = listCake.show(orderby)
		self.tableMenu.DeleteRows(0, self.tableMenu.GetNumberRows())
		self.tableMenu.AppendRows(len(dataListCake))

		for row in range(len(dataListCake)):
			for col in range(self.tableMenu.GetNumberCols()):
				val = dataListCake[row][col]
				self.tableMenu.SetCellValue(row,col,str(val))	

	def eventLogout(self, event):
		self.back = start(None)
		self.Destroy()
		self.back.Show()

class subMenuAdmin(gui.frameMenuOwner):
	def __init__(self,parent):
		gui.frameMenuOwner.__init__(self,parent)
		self.id=id
		self.InitData()		

	def InitData(self,orderby="cake.id"):
		listCake = owner.modelCakeData()
		dataListCake = listCake.show(orderby)
		self.tableMenu.DeleteRows(0, self.tableMenu.GetNumberRows())
		self.tableMenu.AppendRows(len(dataListCake))

		for row in range(len(dataListCake)):
			for col in range(self.tableMenu.GetNumberCols()):
				val = dataListCake[row][col]
				self.tableMenu.SetCellValue(row,col,str(val))	

	def eventSelectCell(self, event):
		col = event.GetCol()
		self.row = event.GetRow()
		print(event.GetRow())

	def eventEditMenu(self,event):
		self.dialog = subEditMenu(None,self.tableMenu.GetCellValue(self.row,0))
		self.dialog.ShowModal()

	def eventHomeOwner(self, event):
		self.back = subHomeAdmin(None)
		self.Destroy()
		self.back.Show()

class subMenuOwner(gui.frameMenuOwner):
	def __init__(self,parent):
		gui.frameMenuOwner.__init__(self,parent)
		self.id=id
		self.InitData()		

	def InitData(self,orderby="cake.id"):
		listCake = owner.modelCakeData()
		dataListCake = listCake.show(orderby)
		self.tableMenu.DeleteRows(0, self.tableMenu.GetNumberRows())
		self.tableMenu.AppendRows(len(dataListCake))

		for row in range(len(dataListCake)):
			for col in range(self.tableMenu.GetNumberCols()):
				val = dataListCake[row][col]
				self.tableMenu.SetCellValue(row,col,str(val))	

	def eventSelectCell(self, event):
		col = event.GetCol()
		self.row = event.GetRow()
		print(event.GetRow())

	def eventEditMenu(self,event):
		self.dialog = subEditMenu(None,self.tableMenu.GetCellValue(self.row,0))
		self.dialog.ShowModal()

	def eventHomeOwner(self, event):
		self.back = subHomeOwner(None)
		self.Destroy()
		self.back.Show()

class subEditMenu(gui.dialogEditMenu):
	def __init__(self,parent,id):
		gui.dialogEditMenu.__init__(self,parent)
		listmenu = owner.modelCakeData()
		self.oldid = id
		cakeid = listmenu.getByid(self.oldid)
		self.txtStock.SetValue(str(cakeid[2]))
		self.txtPrice.SetValue(str(cakeid[3]))

	def eventSave(self,event):
		updateMenu = owner.modelCakeData()
		inputtedStock = self.txtStock.GetValue()
		inputtedPrice = self.txtPrice.GetValue()
		if inputtedStock=="" or inputtedPrice=="":
			wx.MessageBox("Terdapat kolom kosong", "ERROR", wx.OK | wx.ICON_ERROR)
		else:
			updateMenu.update(int(inputtedStock),int(inputtedPrice),str(self.oldid))
			wx.MessageBox("Data berhasil diubah", "Update", wx.OK | wx.ICON_INFORMATION)
			self.Destroy()

	def eventCancel(self,event):
		self.Destroy()

class subAccountOwner(gui.frameAccountOwner):

	def __init__(self,parent):
		gui.frameAccountOwner.__init__(self,parent)
		self.id=id
		self.InitData()		

	def InitData(self,orderby="admins.id"):
		listAdmin = owner.modelAccountData()
		dataListAdmin = listAdmin.show(orderby)
		self.tableMenu.DeleteRows(0, self.tableMenu.GetNumberRows())
		self.tableMenu.AppendRows(len(dataListAdmin))

		for row in range(len(dataListAdmin)):
			for col in range(self.tableMenu.GetNumberCols()):
				val = dataListAdmin[row][col]
				self.tableMenu.SetCellValue(row,col,str(val))	

	def eventSelectCell(self, event):
		col = event.GetCol()
		self.row = event.GetRow()	

	def eventEditAccount(self,event):
		self.dialog = subEditAccount(None,self.tableMenu.GetCellValue(self.row,0))
		self.dialog.ShowModal()

	def eventHomeOwner(self, event):
		self.back = subHomeOwner(None)
		self.Destroy()
		self.back.Show()

class subEditAccount(gui.dialogEditAccount):
	def __init__(self,parent,id):
		gui.dialogEditAccount.__init__(self,parent)
		listacc = owner.modelAccountData()
		self.oldid = id
		accid = listacc.getByid(self.oldid)
		self.txtUsername.SetValue(str(accid[1]))
		self.txtPassword.SetValue(str(accid[2]))

	def eventSave(self,event):
		updateAcc = owner.modelAccountData()
		inputtedUsername = self.txtUsername.GetValue()
		inputtedPassword = self.txtPassword.GetValue()
		if inputtedUsername=="" or inputtedPassword=="":
			wx.MessageBox("Terdapat kolom kosong", "ERROR", wx.OK | wx.ICON_ERROR)
		else:
			updateAcc.update(str(inputtedUsername),str(inputtedPassword),str(self.oldid))
			wx.MessageBox("Data berhasil diubah", "Update", wx.OK | wx.ICON_INFORMATION)
			self.Destroy()

	def eventCancel(self,event):
		self.Destroy()