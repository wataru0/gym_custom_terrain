import os
import shutil
import xml.etree.ElementTree as Et

import gym

from .registration import env_xml_dict

_image_dir_abs_path = ""


def get_image_abs_path(image_path: str) -> str:
    if image_path.startswith("/"):
        return image_path
    cwd = os.getcwd()
    return os.path.join(cwd, image_path)


def get_assets_dir_abs_path() -> str:
    return os.path.join(os.path.dirname(__file__), "envs", "assets")


def get_assets_xml_abs_path(filename: str) -> str:
    assets_dir_path = get_assets_dir_abs_path()
    return os.path.join(assets_dir_path, filename)


def get_tmp_xml_abs_path(filename: str) -> str:
    return os.path.join("/tmp", filename)


def custom_make(env_id: str, terrain_image_name: str):
    xml_name = env_xml_dict[env_id]
    assets_xml_path = get_assets_xml_abs_path(xml_name)

    # 編集するのは/tmp以下のXMLファイル
    tmp_xml_path = os.path.join("/tmp", xml_name)
    shutil.copyfile(assets_xml_path, tmp_xml_path)

    tmp_xml_file = Et.parse(tmp_xml_path)
    root = tmp_xml_file.getroot()

    image_abs_path = get_image_abs_path(terrain_image_name)

    for child in root:
        if child.tag == "asset":
            hfield = child.find("hfield")
            # element.set('属性'，'変更後のデータ')
            hfield.set("file", image_abs_path)

    # 編集内容のファイルへの書き込み
    tmp_xml_file.write(tmp_xml_path, encoding="UTF-8")

    # envの再構成
    env = gym.make(env_id)
    return env
