# gym_custom_terrain

## インストール

```sh
pip install git+https://github.com/wataru0/gym_custom_terrain.git
```


## 使い方

```python
from gym_custom_terrain import custom_make


env = custom_make("CustomTerrainAnt-v0", "images/terrain.png")

env.reset()
done = False

while True:
    env.render()
    if done:
        break
    action = env.action_space.sample()
    _, _, done, _ = env.step(action)
```
