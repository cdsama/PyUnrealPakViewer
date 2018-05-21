import os
import re
import subprocess
import threading

from PySide2.QtCore import Slot, QMimeData
from PySide2.QtGui import QDropEvent, QDragEnterEvent
from PySide2.QtWidgets import QMainWindow, QListWidgetItem, QTreeWidgetItem

from PakFile import PakFileSepFile
from UIMainWindow import Ui_MainWindow
from UnrealPaths import get_valid_ue4_paths


class WMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setAcceptDrops(True)

        self.ue4_paths = get_valid_ue4_paths()
        for item in self.ue4_paths:
            version = f"{item['MajorVersion']:d}.{item['MinorVersion']:d}.{item['PatchVersion']:d}"
            if item["OfficialBuild"]:
                self.ui.combo_box.addItem(f"{version} - Epic Games Build")
            else:
                self.ui.combo_box.addItem(f"{version} - {item['BuildType']} - {item['RootPath']}")
        self.ui.combo_box.currentIndexChanged.connect(self.on_ue4_path_selection_changed)
        self.ui.combo_box.setCurrentIndex(0)

        self.ui.file_list_view.itemSelectionChanged.connect(self.on_file_list_view_selection_changed)

        self.file_content = dict()

    @Slot(int)
    def on_ue4_path_selection_changed(self, index):
        print(index)

    def dragEnterEvent(self, event: QDragEnterEvent):
        mime_data: QMimeData = event.mimeData()
        if mime_data.hasUrls() and len(mime_data.urls()[0].toLocalFile()) > 0:
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        mime_data: QMimeData = event.mimeData()
        for url in mime_data.urls():
            file_name = url.toLocalFile()
            if os.path.splitext(file_name)[1][1:] == "pak":
                self.ui.file_list_view.addItem(file_name)

    def on_file_list_view_selection_changed(self):
        selected_files = self.ui.file_list_view.selectedItems()
        if len(selected_files) > 0:
            selected_file: QListWidgetItem = selected_files[0]
            pak_file = selected_file.text()

            ue4_path = self.ue4_paths[self.ui.combo_box.currentIndex()]['RootPath']
            command = f"{ue4_path}/Engine/Binaries/Win64/UnrealPak.exe {pak_file} -List"
            t = threading.Thread(target=self.get_pak_content, args=(command,))
            t.start()

    def get_pak_content(self, command):
        status, output = subprocess.getstatusoutput(command)
        result_list = output.splitlines()
        sep_file_list = []
        for line in result_list:
            pattern = r'LogPakFile: Display: "(.+)" offset: (.+), size: (.+) bytes, sha1: (.+)\.'
            res = re.match(pattern, line)
            if res is not None:
                # print(res.groups())
                sep_file_list.append(PakFileSepFile(res.group(0), res.group(1), res.group(2), res.group(3)))
                self.ui.pak_content_tree_view.addItem(line)

    @Slot()
    def on_btn_test_clicked(self):
        item = QTreeWidgetItem(None, ["Test", "a"])
        child = QTreeWidgetItem(None, ["Test", "a"])
        g_c = QTreeWidgetItem(None, ["Test", "a"])
        child.addChild(g_c)
        item.addChild(child)
        self.ui.pak_content_tree_view.addTopLevelItem(item)
