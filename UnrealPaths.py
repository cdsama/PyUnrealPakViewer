import json
import os
import winreg as winreg


def is_valid_root_dir(dir_name, version_info):
    result = False
    if not os.path.isdir(dir_name):
        return result
    if not os.path.isdir(os.path.join(dir_name, "Engine", "Binaries")):
        return result
    build_version_file = os.path.join(dir_name, "Engine", "Build", "Build.version")
    if not os.path.isfile(build_version_file):
        return result
    source_distribution_file = os.path.join(dir_name, "Engine", "Build", "SourceDistribution.txt")
    build_type = "SourceBuild" if os.path.isfile(source_distribution_file) else "BinaryBuild"
    version_info.update({"BuildType": build_type})
    try:
        with open(build_version_file, "r") as f:
            version_info.update(json.load(f))
            result = True
    finally:
        return result


def get_valid_ue4_paths():
    ue4_paths = []
    build_key_name = r"Software\Epic Games\Unreal Engine\Builds"
    build_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, build_key_name)
    i = 0
    try:
        while True:
            _, value, _ = winreg.EnumValue(build_key, i)
            version_info = {"RootPath": value, "OfficialBuild": False}
            if is_valid_root_dir(value, version_info):
                ue4_paths.append(version_info)
            i += 1
    except WindowsError:
        pass
    winreg.CloseKey(build_key)

    installed_key_name = r"SOFTWARE\EpicGames\Unreal Engine"
    installed_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, installed_key_name)
    i = 0
    try:
        while True:
            version_name = winreg.EnumKey(installed_key, i)
            version_key_name = r"%s\%s" % (installed_key_name, version_name)
            version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, version_key_name)
            _, value, _ = winreg.EnumValue(version_key, 0)
            version_info = {"RootPath": value.replace("\\", "/"), "OfficialBuild": True}
            if is_valid_root_dir(value, version_info):
                ue4_paths.append(version_info)
            i += 1
    except WindowsError:
        pass
    winreg.CloseKey(installed_key)
    return ue4_paths


if __name__ == '__main__':
    for path in get_valid_ue4_paths():
        print(path)
