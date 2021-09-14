from Controller import *
from Repository import *
from UI import *

repos = MovieRepository()
ctrl = MovieController(repos)
ui = UI(ctrl)
ui.show_menu()
