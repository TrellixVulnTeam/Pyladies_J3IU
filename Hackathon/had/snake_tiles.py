from pathlib import Path
import pyglet

TILES_DIRECTORY = Path('snake-tiles')

snake_tiles = {}

for path in TILES_DIRECTORY.glob('*.png'):
    snake_tiles[path.stem] = pyglet.image.load(path)

#print(snake_tiles)