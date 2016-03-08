from window import Window
from door import Door
import openclosefuncs

def main():
    lst = [Door("opened"), Door(), Door(), Window("opened"),
           Window(), Door(), Window("opened"), Window("opened")]

    openclosefuncs.closeAll(lst)
    openclosefuncs.openAll(lst)
