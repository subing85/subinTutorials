# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/dumps/publish_01.ui'
#
# Created: Sat Nov  2 21:27:27 2019
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(744, 598)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupbox_label = QtGui.QGroupBox(Form)
        self.groupbox_label.setObjectName(_fromUtf8("groupbox_label"))
        self.horizontallayout_data = QtGui.QHBoxLayout(self.groupbox_label)
        self.horizontallayout_data.setSpacing(10)
        self.horizontallayout_data.setContentsMargins(10, 12, 10, 10)
        self.horizontallayout_data.setObjectName(_fromUtf8("horizontallayout_data"))
        self.button_label = QtGui.QPushButton(self.groupbox_label)
        self.button_label.setMinimumSize(QtCore.QSize(100, 100))
        self.button_label.setMaximumSize(QtCore.QSize(100, 100))
        self.button_label.setObjectName(_fromUtf8("button_label"))
        self.horizontallayout_data.addWidget(self.button_label)
        self.label_2 = QtGui.QLabel(self.groupbox_label)
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(188, 188, 188);\n"
"font: 14pt \"Sans Serif\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontallayout_data.addWidget(self.label_2)
        self.button_open = QtGui.QPushButton(self.groupbox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_open.sizePolicy().hasHeightForWidth())
        self.button_open.setSizePolicy(sizePolicy)
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.horizontallayout_data.addWidget(self.button_open)
        self.verticalLayout.addWidget(self.groupbox_label)
        self.groupbox_input = QtGui.QGroupBox(Form)
        self.groupbox_input.setObjectName(_fromUtf8("groupbox_input"))
        self.verticallayout_input = QtGui.QVBoxLayout(self.groupbox_input)
        self.verticallayout_input.setSpacing(10)
        self.verticallayout_input.setMargin(10)
        self.verticallayout_input.setObjectName(_fromUtf8("verticallayout_input"))
        self.gridlayout_input = QtGui.QGridLayout()
        self.gridlayout_input.setObjectName(_fromUtf8("gridlayout_input"))
        self.button_thumbnail = QtGui.QPushButton(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_thumbnail.sizePolicy().hasHeightForWidth())
        self.button_thumbnail.setSizePolicy(sizePolicy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setObjectName(_fromUtf8("button_thumbnail"))
        self.gridlayout_input.addWidget(self.button_thumbnail, 1, 0, 1, 1)
        self.label_thumbnail = QtGui.QLabel(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_thumbnail.sizePolicy().hasHeightForWidth())
        self.label_thumbnail.setSizePolicy(sizePolicy)
        self.label_thumbnail.setObjectName(_fromUtf8("label_thumbnail"))
        self.gridlayout_input.addWidget(self.label_thumbnail, 0, 0, 1, 1)
        self.label_description = QtGui.QLabel(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setObjectName(_fromUtf8("label_description"))
        self.gridlayout_input.addWidget(self.label_description, 0, 1, 1, 1)
        self.textedit_description = QtGui.QTextEdit(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_description.sizePolicy().hasHeightForWidth())
        self.textedit_description.setSizePolicy(sizePolicy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 180))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 180))
        self.textedit_description.setObjectName(_fromUtf8("textedit_description"))
        self.gridlayout_input.addWidget(self.textedit_description, 1, 1, 1, 1)
        self.verticallayout_input.addLayout(self.gridlayout_input)
        self.gridlayout_inputs = QtGui.QGridLayout()
        self.gridlayout_inputs.setContentsMargins(4, 4, 3, 10)
        self.gridlayout_inputs.setHorizontalSpacing(5)
        self.gridlayout_inputs.setVerticalSpacing(10)
        self.gridlayout_inputs.setObjectName(_fromUtf8("gridlayout_inputs"))
        self.label_category = QtGui.QLabel(self.groupbox_input)
        self.label_category.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_category.setObjectName(_fromUtf8("label_category"))
        self.gridlayout_inputs.addWidget(self.label_category, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout_inputs.addItem(spacerItem, 0, 2, 1, 1)
        self.combobox_category = QtGui.QComboBox(self.groupbox_input)
        self.combobox_category.setMinimumSize(QtCore.QSize(150, 0))
        self.combobox_category.setEditable(False)
        self.combobox_category.setInsertPolicy(QtGui.QComboBox.InsertAfterCurrent)
        self.combobox_category.setObjectName(_fromUtf8("combobox_category"))
        self.combobox_category.addItem(_fromUtf8(""))
        self.gridlayout_inputs.addWidget(self.combobox_category, 0, 1, 1, 1)
        self.label_tag = QtGui.QLabel(self.groupbox_input)
        self.label_tag.setObjectName(_fromUtf8("label_tag"))
        self.gridlayout_inputs.addWidget(self.label_tag, 1, 0, 1, 1)
        self.combobox_tag = QtGui.QComboBox(self.groupbox_input)
        self.combobox_tag.setObjectName(_fromUtf8("combobox_tag"))
        self.gridlayout_inputs.addWidget(self.combobox_tag, 1, 1, 1, 1)
        self.verticallayout_input.addLayout(self.gridlayout_inputs)
        self.horizontallayout_input = QtGui.QHBoxLayout()
        self.horizontallayout_input.setObjectName(_fromUtf8("horizontallayout_input"))
        self.verticallayout_input.addLayout(self.horizontallayout_input)
        self.verticalLayout.addWidget(self.groupbox_input)
        self.groupbox_publish = QtGui.QGroupBox(Form)
        self.groupbox_publish.setObjectName(_fromUtf8("groupbox_publish"))
        self.horizontallayout_publish = QtGui.QHBoxLayout(self.groupbox_publish)
        self.horizontallayout_publish.setSpacing(10)
        self.horizontallayout_publish.setMargin(10)
        self.horizontallayout_publish.setObjectName(_fromUtf8("horizontallayout_publish"))
        self.label_publish = QtGui.QLabel(self.groupbox_publish)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_publish.sizePolicy().hasHeightForWidth())
        self.label_publish.setSizePolicy(sizePolicy)
        self.label_publish.setObjectName(_fromUtf8("label_publish"))
        self.horizontallayout_publish.addWidget(self.label_publish)
        self.combobox_publish = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_publish.setObjectName(_fromUtf8("combobox_publish"))
        self.combobox_publish.addItem(_fromUtf8(""))
        self.combobox_publish.addItem(_fromUtf8(""))
        self.combobox_publish.addItem(_fromUtf8(""))
        self.horizontallayout_publish.addWidget(self.combobox_publish)
        self.label_version = QtGui.QLabel(self.groupbox_publish)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_version.sizePolicy().hasHeightForWidth())
        self.label_version.setSizePolicy(sizePolicy)
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName(_fromUtf8("label_version"))
        self.horizontallayout_publish.addWidget(self.label_version)
        self.button_publish = QtGui.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName(_fromUtf8("button_publish"))
        self.horizontallayout_publish.addWidget(self.button_publish)
        self.verticalLayout.addWidget(self.groupbox_publish)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupbox_label.setTitle(_translate("Form", "Input File", None))
        self.button_label.setText(_translate("Form", "PushButton", None))
        self.label_2.setText(_translate("Form", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", None))
        self.button_open.setText(_translate("Form", "...", None))
        self.groupbox_input.setTitle(_translate("Form", "Inputs", None))
        self.button_thumbnail.setText(_translate("Form", "Image", None))
        self.label_thumbnail.setText(_translate("Form", "Thumbnail", None))
        self.label_description.setText(_translate("Form", "Description", None))
        self.label_category.setText(_translate("Form", "Cat", None))
        self.combobox_category.setItemText(0, _translate("Form", "Model", None))
        self.label_tag.setText(_translate("Form", "TextLabel", None))
        self.groupbox_publish.setTitle(_translate("Form", "Publish", None))
        self.label_publish.setText(_translate("Form", "Next Avilable Publish versions", None))
        self.combobox_publish.setItemText(0, _translate("Form", "Major", None))
        self.combobox_publish.setItemText(1, _translate("Form", "Minor", None))
        self.combobox_publish.setItemText(2, _translate("Form", "Patch", None))
        self.label_version.setText(_translate("Form", "0.0.0", None))
        self.button_publish.setText(_translate("Form", "Publish", None))
