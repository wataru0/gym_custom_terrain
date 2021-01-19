import gym
from gym.envs.registration import register
import xml.etree.ElementTree as Et

register(
    id="CustomTerrainAnt-v0",
    entry_point="gym_custom_terrain.envs.custom_terrain_ant_env:CustomTerrainAntEnv",
)


def custom_make(env_id: str, xml_path: str, terrain_image: str):
    xml_file = Et.parse(xml_path)
    root = xml_file.getroot()

    for child in root:
        if child.tag == "asset":
            hfield = child.find("hfield")
            # element.set('属性'，'変更後のデータ')
            hfield.set("file", terrain_image)

    # 編集内容のファイルへの書き込み
    xml_file.write(xml_path, encoding="UTF-8")

    # envの再構成
    env = gym.make(env_id)
    return env
