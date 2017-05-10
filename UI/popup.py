import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import *


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
        self.close = QtWidgets.QToolButton(self)
        self.close.setIcon(QtGui.QIcon('images/close.png'))
        self.close.setMouseTracking(True)

        # title bar default setting
        self.close.setMinimumHeight(10)

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
        title_bar_right_layout.addWidget(self.close)

        title_bar_layout = QtWidgets.QHBoxLayout(self)
        title_bar_layout.addLayout(title_bar_left_layout)
        title_bar_layout.addLayout(title_bar_right_layout)

        # set title bar size
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Fixed)


class PopupMenuBar(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
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

        # set check button
        self.checkBtn = QtWidgets.QToolButton(self)
        self.checkBtn.setIcon(QtGui.QIcon('images/check_white.png'))
        self.checkBtn.setMouseTracking(True)

        # set close button
        self.eraseBtn = QtWidgets.QToolButton(self)
        self.eraseBtn.setIcon(QtGui.QIcon('images/erase_white.png'))
        self.eraseBtn.setMouseTracking(True)

        # set close button
        self.closeBtn = QtWidgets.QToolButton(self)
        self.closeBtn.setIcon(QtGui.QIcon('images/close_white.png'))
        self.closeBtn.setMouseTracking(True)

        # set layout
        popup_layout = QtWidgets.QHBoxLayout(self)

        # add widget
        popup_layout.addWidget(self.checkBtn)
        popup_layout.addWidget(self.eraseBtn)
        popup_layout.addWidget(self.closeBtn)
        popup_layout.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # set title bar size
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.maxNormal = False


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


class PopupContents(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        #QtWidgets.QDialog.__init__(self, act_type)
        css ="""
        QWidget{
            Background:  #FFFFFF;
            color: black;
            }
        QWidget.QComboBox {
            Background : #F6F6F6;
        }
        QWidget.QLineEdit {
            Background : #F6F6F6;
        }
        """
        self.setStyleSheet(css)
        self.m_addCloud = AddCloud()
        self.contents = QtWidgets.QVBoxLayout(self)
        self.contents.addWidget(self.m_addCloud)


class AddCloud(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        # set combo box
        self.drive_combo = QtWidgets.QComboBox()
        self.drive_combo.addItem("GoogleDrive")
        self.drive_combo.addItem("Box")
        self.drive_combo.addItem("OneDrive")
        self.drive_combo.addItem("DropBox")

        # set id QLineEdit
        self.id = QtWidgets.QLineEdit()

        # set password LineEdit to secret
        self.pw = QtWidgets.QLineEdit()
        self.pw.setEchoMode(QtWidgets.QLineEdit.Password)

        # set layout
        layout = QtWidgets.QFormLayout(self)
        layout.addRow(QtWidgets.QLabel("Drive"), self.drive_combo)
        layout.addRow(QtWidgets.QLabel("Id"), self.id)
        layout.addRow(QtWidgets.QLabel("Password"), self.pw)


class PopupMainDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        css = """
        QFrame{
            Background:  #CFCFCF;
            color:white;
            font:13px ;
            font-weight:bold;
            }
        """
        self.setStyleSheet(css)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(400, 400)

        self.m_titleBar = TitleBar()
        self.m_popupMenuBar = PopupMenuBar()
        self.m_popupContents = PopupContents()
        self.m_popupStatusBar = StatusBar()
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.m_titleBar)
        vbox.addWidget(self.m_popupMenuBar)
        vbox.addWidget(self.m_popupContents)
        vbox.addWidget(self.m_popupStatusBar)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(event.globalPos() - self.offset)

    def get_add_cloud_data(self):
        m_data_area = self.m_popupContents.m_addCloud
        ret = [m_data_area.drive_combo.currentText(), m_data_area.id.text(), m_data_area.pw.text()]
        return ret


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    popupMainDialog = PopupMainDialog()
    popupMainDialog.move(60, 60)
    popupMainDialog.show()
    app.exec_()
