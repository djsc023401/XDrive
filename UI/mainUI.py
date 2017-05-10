from popup import *


# TitleBar class (custom)
# Tooltip(minimize, maximize, close)
# Set css to widget, dialog, button
class TitleBar(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # set css for TitleBar
        css = """
        QWidget{
            Background: #F6F6F6;
            color:Black;
            font:12px bold;
            font-weight:bold;
            border-radius: 1px;
            height: 11px;
        }
        QDialog{
            font-size:12px;
            color: black;
        }
        QToolButton{
            Background:#F6F6F6;
            font-size:11px;
        }
        QToolButton:hover{
            font-size:11px;
        }
        QLabel{
            font-size:14px;
        }
        """
        # set css and background
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css)

        # XDrive icon
        XD = QtWidgets.QToolButton(self)
        XD.setIcon(QtGui.QIcon('images/1.png'))

        # tooltip button setting
        self.minimize = QtWidgets.QToolButton(self)
        self.minimize.setIcon(QtGui.QIcon('images/minimize.png'))

        self.maximize = QtWidgets.QToolButton(self)
        self.maximize.setIcon(QtGui.QIcon('images/maximize.png'))

        self.close = QtWidgets.QToolButton(self)
        self.close.setIcon(QtGui.QIcon('images/close.png'))

        # title bar default setting
        self.minimize.setMinimumHeight(15)
        self.close.setMinimumHeight(10)
        self.maximize.setMinimumHeight(10)

        # set title
        label = QtWidgets.QLabel(self)
        label.setText("XDrive")
        self.setWindowTitle("XDrive")

        # set horizontal box for titlebar
        # add label, tooltip buttons
        title_bar_left_layout = QtWidgets.QHBoxLayout()
        title_bar_left_layout.addWidget(XD)
        title_bar_left_layout.addWidget(label)

        title_bar_right_layout = QtWidgets.QHBoxLayout()
        title_bar_right_layout.addWidget(self.minimize)
        title_bar_right_layout.addWidget(self.maximize)
        title_bar_right_layout.addWidget(self.close)

        title_bar_layout = QtWidgets.QHBoxLayout(self)
        title_bar_layout.addLayout(title_bar_left_layout)
        title_bar_layout.addLayout(title_bar_right_layout)

        # set title bar size
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.maxNormal = False

        self.close.clicked.connect(self.close_window)
        self.minimize.clicked.connect(self.show_minimize)
        self.maximize.clicked.connect(self.show_max_restore)

    def close_window(self):
        mainUI.close()

    def show_minimize(self):
        mainUI.showMinimized()

    def show_max_restore(self):
        if(self.maxNormal):
            mainUI.showNormal()
            self.maxNormal = False
            self.maximize.setIcon(QtGui.QIcon('images/maximize.png'))
        else:
            mainUI.showMaximized()
            self.maxNormal = True
            self.maximize.setIcon(QtGui.QIcon('images/maximize.png'))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            mainUI.moving = True
            mainUI.offset = event.pos()

    def mouseMoveEvent(self, event):
        if mainUI.moving:
            mainUI.move(event.globalPos() - mainUI.offset)


class MenuBar(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # set css for TitleBar
        css = """
        QWidget{
            Background: #4374D9;
            border-radius: 0px;
        }
        """
        # set css and background
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css)

        # set cloud add button
        self.addCloudBtn = QtWidgets.QToolButton(self)
        self.addCloudBtn.setIcon(QtGui.QIcon('images/add_cloud.png'))
        self.addCloudBtn.setMouseTracking(True)

        # set cloud remove button
        self.removeCloudBtn = QtWidgets.QToolButton(self)
        self.removeCloudBtn.setIcon(QtGui.QIcon('images/remove_cloud.png'))
        self.removeCloudBtn.setMouseTracking(True)

        # set setting button
        self.settingBtn = QtWidgets.QToolButton(self)
        self.settingBtn.setIcon(QtGui.QIcon('images/setting.png'))
        self.settingBtn.setMouseTracking(True)

        # set array button
        self.arrangeBtn = QtWidgets.QToolButton(self)
        self.arrangeBtn.setIcon(QtGui.QIcon('images/arrange.png'))

        # set layout
        menu_left_layout = QtWidgets.QHBoxLayout()
        used_label = QtWidgets.QLabel()
        not_used_label = QtWidgets.QLabel()
        menu_left_layout.addWidget(used_label)
        menu_left_layout.addWidget(not_used_label)

        # add/remove cloud, setting, arrange button
        menu_right_layout = QtWidgets.QHBoxLayout()
        menu_right_layout.addWidget(self.arrangeBtn)
        menu_right_layout.addWidget(self.addCloudBtn)
        menu_right_layout.addWidget(self.removeCloudBtn)
        menu_right_layout.addWidget(self.settingBtn)
        menu_right_layout.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        menu_layout = QtWidgets.QHBoxLayout(self)
        menu_layout.addLayout(menu_left_layout)
        menu_layout.addLayout(menu_right_layout)

        # set title bar size
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.maxNormal = False

        # add action
        self.addCloudBtn.clicked.connect(self.add_cloud_action)
        self.removeCloudBtn.clicked.connect(self.remove_cloud_action)
        self.settingBtn.clicked.connect(self.setting_action)
        self.arrangeBtn.clicked.connect(self.directory_arrange_action)

        # set popup
        self.add_popup = PopupMainDialog()
        self.add_popup.m_titleBar.close.clicked.connect(self.close_add_cloud)
        self.add_popup.m_popupMenuBar.checkBtn.clicked.connect(self.check_add_cloud)

    def directory_arrange_action(self):
        print("arrange")

    def add_cloud_action(self):
        self.add_popup.exec_()

    def close_add_cloud(self):
        self.add_popup.close()

    def check_add_cloud(self):
        ret = self.add_popup.get_add_cloud_data()
        if ret[1] == "":
            print("none")
        else:
            print(ret[0])
        mainUI.m_statusBar.statusLabel.setText(ret[0]+" (" + ret[1] + ") is conntected")

    def remove_cloud_action(self):
        print("remove")

    def setting_action(self):
        print("setting")


class StatusBar(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # set css for TitleBar
        css = """
        QWidget{
            Background: #F6F6F6;
            border-radius: 1px;
            color: black;
        }
        """
        # set css and background
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css)

        self.statusLabel = QtWidgets.QLabel("running")

        # set horizontal box
        # add/remove cloud, setting button
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.statusLabel)
        # set title bar size
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.maxNormal = False


class DirectoryViewer(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        css = """
        QFrame{
            Background : #FFFFFF;
            Color:black;
        }
        """
        self.setStyleSheet(css)
        self.setMinimumSize(800, 400)
        self.setAcceptDrops(True)

        box = QtWidgets.QHBoxLayout(self)
        self.label1 = QtWidgets.QLabel("virtual directory")
        box.addWidget(self.label1)

    def dropEvent(self, event):
            print(event)
            print(event.mimeData().text())


class MainFrame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        css = """
        QFrame{
            Background:  #CFCFCF;
            color:white;
            font:13px ;
            font-weight:bold;
            }
        """
        self.setStyleSheet(css)
        self.m_mouse_down = False
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.setAcceptDrops(True)

        self.m_titleBar = TitleBar(self)
        self.m_content = QtWidgets.QWidget(self)
        self.m_menuBar = MenuBar(self)
        self.m_directoryViewer = DirectoryViewer(self)
        self.m_statusBar = StatusBar(self)
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.m_titleBar)
        vbox.addWidget(self.m_menuBar)
        vbox.addWidget(self.m_directoryViewer)
        vbox.addWidget(self.m_statusBar)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)

    def contentWidget(self):
        return self.m_content

    def titleBar(self):
        return self.m_titleBar

    def mousePressEvent(self, event):
        self.m_old_pos = event.pos()
        self.m_mouse_down = (event.button() == Qt.LeftButton)

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()

    def mouseReleaseEvent(self, event):
        m_mouse_down = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainUI = MainFrame()
    mainUI.move(60, 60)
    mainUI.show()
    app.exec_()
