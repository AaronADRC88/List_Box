__author__ = 'aferreiradominguez'
# !/usr/bin/python
from gi.repository import Gtk


class Lista_en_caja(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ventana")
        self.set_border_width(10)
        self.set_default_size(200, 300)

        caixaV = Gtk.Box(spacing=6)
        self.add(caixaV)

        # crea obxeto ListBox
        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        caixaV.pack_start(listBox, True, True, 0)

        fila = Gtk.ListBoxRow()
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(caixaH)
        caixaV_int = Gtk.Box(Gtk.Orientation.VERTICAL)
        caixaH.pack_start(caixaV_int, True, True, 0)

        etiqueta = Gtk.Label("Hora e data automatics", xalign=0)
        etiqueta2 = Gtk.Label("Require acceso a internet", xalign=0)
        caixaV_int.pack_start(etiqueta, True, True, 0)
        caixaV_int.pack_start(etiqueta2, True, True, 0)

        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        caixaH.pack_start(switch, False, True, 0)

        listBox.add(fila)

        # Segunda fila
        fila2 = Gtk.ListBoxRow()
        caixaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila2.add(caixaH2)

        etiqueta3 = Gtk.Label("Permitir auto-actualizar", xalign=0)
        check = Gtk.CheckButton()
        caixaH2.pack_start(etiqueta3, True, True, 0)
        caixaH2.pack_start(check, True, True, 0)
        listBox.add(fila2)

        fila3 = Gtk.ListBoxRow()
        caixaH3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila3.add(caixaH3)

        etiqueta4 = Gtk.Label("formato data", xalign=0)
        combo = Gtk.ComboBoxText()
        combo.insert(0, "0", "24-h")
        combo.insert(1, "1", "AM/PM")
        caixaH3.pack_start(etiqueta4, True, True, 0)
        caixaH3.pack_start(combo, False, True, 0)
        listBox.add(fila3)


lista = Lista_en_caja()
lista.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
lista.set_resizable(False)
lista.connect("delete-event", Gtk.main_quit)
lista.show_all()
lista.set_decorated(True)
Gtk.main()
