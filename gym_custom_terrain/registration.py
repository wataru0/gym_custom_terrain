import gym

env_xml_dict = {}


def register(
    id: str,
    entry_point: str,
    max_episode_steps: int,
    reward_threshold: float,
    xml: str,
) -> None:
    gym.register(
        id=id,
        entry_point=entry_point,
        max_episode_steps=max_episode_steps,
        reward_threshold=reward_threshold,
    )
    env_xml_dict[id] = xml
