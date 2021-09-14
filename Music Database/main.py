from  Controller import *
from Repository import *
from UI import *

r = MusicRepository()
ctrl = MusicController(r)
ui = UI(ctrl)
ui.show_menu()