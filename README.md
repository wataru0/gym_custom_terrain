# gym_custom_terrain
This package will help you customize the terrain in MuJoCo.

## How to install

```sh
pip install git+https://github.com/wataru0/gym_custom_terrain.git
```


## How to use

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

## Demo

### Input Image

<img src=https://user-images.githubusercontent.com/44032125/105473966-1256af80-5ce1-11eb-82a8-3a9346925543.png>

### Simulation Environment

<img src=https://user-images.githubusercontent.com/44032125/105473915-036ffd00-5ce1-11eb-9568-cdedf96419d8.png>

