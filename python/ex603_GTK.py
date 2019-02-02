###################################################
#
# File name  : ex603_GTK.py
# Executeoin : python3 ex603_GTK.py
# Description : 
#
###################################################


from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="")


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
