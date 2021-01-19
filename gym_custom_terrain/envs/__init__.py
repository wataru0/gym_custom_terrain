from ..registration import register


register(
    id="CustomTerrainAnt-v0",
    entry_point="gym_custom_terrain.envs.custom_terrain_ant_env:CustomTerrainAntEnv",
    max_episode_steps=1000,
    reward_threshold=6000.0,
    xml="custom_terrain_ant.xml",
)
