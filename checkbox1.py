# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\checkbox.ui'
#
# Created: Tue Mar 17 14:49:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from methods import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 577)

        #selects log file.txt (takes user selection) then request user create new report
        def select_method():
            try:
                if self.cbx_all.isChecked():
                    timestamps()
                    port_security()
                    mac_flood_detection()
                    QMessageBox.information(None, 'Done', 'Analysis is complete!\n\nYour report has been generated and is available to view')
                    return
                if self.cbx_mac_flood.isChecked():
                    mac_flood_detection()
                if self.cbx_port_sec.isChecked():
                    port_security()
                if self.cbx_all_timestamps.isChecked():
                    timestamps()

                QMessageBox.information(None, 'Done', 'Analysis is complete!\n\nYour report has been generated and is available to view')
            except:
                QMessageBox.information(None, 'Error', 'Invalid Entry!\nPlease Try Again')



        self.btn_select_file = QtGui.QPushButton(Dialog)
        self.btn_select_file.setGeometry(QtCore.QRect(30, 90, 81, 31))
        self.btn_select_file.setObjectName("btn_select_file")
        QtCore.QObject.connect(self.btn_select_file, QtCore.SIGNAL('clicked()'), get_log_file)

        self.btn_start = QtGui.QPushButton(Dialog)
        self.btn_start.setGeometry(QtCore.QRect(30, 430, 101, 31))
        self.btn_start.setObjectName("btn_start")
        QtCore.QObject.connect(self.btn_start, QtCore.SIGNAL('clicked()'), select_method)

        self.btn_view = QtGui.QPushButton(Dialog)
        self.btn_view.setGeometry(QtCore.QRect(190, 430, 101, 31))
        self.btn_view.setObjectName("btn_view")
        QtCore.QObject.connect(self.btn_view, QtCore.SIGNAL('clicked()'), view_it)

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 350, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 280, 21))
        self.label_2.setObjectName("label_2")

        self.btn_exit = QtGui.QPushButton(Dialog)
        self.btn_exit.setGeometry(QtCore.QRect(360, 530, 75, 25))
        self.btn_exit.setObjectName("btn_exit")
        QtCore.QObject.connect(self.btn_exit, QtCore.SIGNAL('clicked()'), close_it)

        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 230, 311, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.cbx_all = QtGui.QCheckBox(self.layoutWidget)
        self.cbx_all.setObjectName("cbx_all")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.cbx_all)
        self.cbx_vlan_hop = QtGui.QCheckBox(self.layoutWidget)
        self.cbx_vlan_hop.setObjectName("cbx_vlan_hop")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbx_vlan_hop)
        self.cbx_all_timestamps = QtGui.QCheckBox(self.layoutWidget)
        self.cbx_all_timestamps.setObjectName("cbx_all_timestamps")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.cbx_all_timestamps)
        self.cbx_port_sec = QtGui.QCheckBox(self.layoutWidget)
        self.cbx_port_sec.setObjectName("cbx_port_sec")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.cbx_port_sec)
        self.cbx_span_tree = QtGui.QCheckBox(self.layoutWidget)
        self.cbx_span_tree.setObjectName("cbx_span_tree")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbx_span_tree)
        self.cbx_mac_flood = QtGui.QCheckBox(self.layoutWidget)
        self.cbx_mac_flood.setObjectName("cbx_mac_flood")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.cbx_mac_flood)
        self.cbx_dhcp_spoof = QtGui.QCheckBox(self.layoutWidget)
        self.cbx_dhcp_spoof.setObjectName("cbx_dhcp_spoof")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cbx_dhcp_spoof)
        self.cbx_arp_pois = QtGui.QCheckBox(self.layoutWidget)
        self.cbx_arp_pois.setObjectName("cbx_arp_pois")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cbx_arp_pois)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btn_select_file, self.cbx_all)
        Dialog.setTabOrder(self.cbx_all, self.cbx_all_timestamps)
        Dialog.setTabOrder(self.cbx_all_timestamps, self.cbx_port_sec)
        Dialog.setTabOrder(self.cbx_port_sec, self.cbx_mac_flood)
        Dialog.setTabOrder(self.cbx_mac_flood, self.cbx_vlan_hop)
        Dialog.setTabOrder(self.cbx_vlan_hop, self.cbx_arp_pois)
        Dialog.setTabOrder(self.cbx_arp_pois, self.cbx_span_tree)
        Dialog.setTabOrder(self.cbx_span_tree, self.cbx_dhcp_spoof)
        Dialog.setTabOrder(self.cbx_dhcp_spoof, self.btn_start)
        Dialog.setTabOrder(self.btn_start, self.btn_view)
        Dialog.setTabOrder(self.btn_view, self.btn_exit)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_select_file.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_start.setText(QtGui.QApplication.translate("Dialog", "Run Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_view.setText(QtGui.QApplication.translate("Dialog", "View Report", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Please select log file for analysis and follow prompt to create case file:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Select one or more categories for Security Analysis:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_exit.setText(QtGui.QApplication.translate("Dialog", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_all.setText(QtGui.QApplication.translate("Dialog", "ALL: Full Report", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_vlan_hop.setText(QtGui.QApplication.translate("Dialog", "VLAN Hopping", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_all_timestamps.setText(QtGui.QApplication.translate("Dialog", "Extract All Timestamps", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_port_sec.setText(QtGui.QApplication.translate("Dialog", "Port Security Violations", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_span_tree.setText(QtGui.QApplication.translate("Dialog", "Spanning Tree Protocol", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_mac_flood.setText(QtGui.QApplication.translate("Dialog", "Mac Flooding", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_dhcp_spoof.setText(QtGui.QApplication.translate("Dialog", "DHCP Server Spoofing", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_arp_pois.setText(QtGui.QApplication.translate("Dialog", "ARP Poisoning", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

