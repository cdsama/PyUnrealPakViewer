import os
import re
import subprocess
import threading

from PySide2.QtCore import Slot, QMimeData
from PySide2.QtGui import QDropEvent, QDragEnterEvent
from PySide2.QtWidgets import QMainWindow, QListWidgetItem, QTreeWidgetItem, QHeaderView

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
        self.ui.pak_content_tree_view.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.pak_content_tree_view.setHeaderLabels(["File Name", "Offset", "Size (bytes)", "Hash (sha1)"])

        self.file_content = dict()
        self.items = dict()

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

            self.ui.pak_content_tree_view.clear()
            self.file_content.clear()
            self.items.clear()
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
                sep_file = PakFileSepFile(res.group(1), res.group(2), res.group(3), res.group(4))
                sep_file_list.append(sep_file)

                path_sections = sep_file.path.split("/")
                path_connect = ""
                parent_item: QTreeWidgetItem = None
                for path_section in path_sections[:-1]:
                    path_connect += path_section + "/"
                    if path_connect in self.items:
                        parent_item = self.items[path_connect]
                    else:
                        tmp_item = QTreeWidgetItem(None, [path_section])
                        self.items[path_connect] = tmp_item
                        if parent_item is None:
                            print(path_section, sep_file.path)
                            self.ui.pak_content_tree_view.addTopLevelItem(
                                tmp_item)
                        else:
                            parent_item.addChild(tmp_item)
                        parent_item = tmp_item

                item = QTreeWidgetItem(
                    None, [path_sections[-1], sep_file.offset, sep_file.size, sep_file.sha1])
                if parent_item is None:
                    self.ui.pak_content_tree_view.addTopLevelItem(item)
                else:
                    parent_item.addChild(item)
                self.items[sep_file.path] = item

    @Slot()
    def on_btn_test_clicked(self):
        item = QTreeWidgetItem(None, ["Test", "a"])
        child = QTreeWidgetItem(None, ["Test", "a"])
        g_c = QTreeWidgetItem(None, ["Test", "a"])
        child.addChild(g_c)
        item.addChild(child)
        self.ui.pak_content_tree_view.addTopLevelItem(item)
