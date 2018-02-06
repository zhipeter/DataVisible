'''Create a world map'''
import pygal

wm = pygal.maps.world.World()
wm.title = 'World Map'

# wm.add('Asia', {'cn':1, 'tw':2, 'jp':3})
wm.add('America', ['us', 'ca'])

wm.render_to_file('worldmap.svg')
