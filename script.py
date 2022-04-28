from tkinter import *
from tkinter import ttk
import ctypes
import PokeAPI
import sys
import os

def main():

    # sets the path containing the current script to "script_dir"
    script_dir = sys.path[0]
    # if an "images" directory does not exist in script_dir, create one
    if os.path.isdir(os.path.join(script_dir, "images")):
        pass
    else:
        os.mkdir(os.path.join(script_dir, "Images"))
    # changes the taskbar icon of the program
    app_id = "poke.image.viewer"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    # creates window, changes window title, changes window icon, sets minimum window size, and sets window resizing options
    root = Tk()
    root.title("Poke Image Viewer")
    root.iconbitmap(os.path.join(script_dir,"charizard.ico"))
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.minsize(500, 600)
    # creates base frame, sets grid and window resizing options
    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.rowconfigure(0, weight=10)
    frm.columnconfigure(0, weight=1)
    # creates the image object and sets it to a label
    poke_img = PhotoImage(file=os.path.join(script_dir, "shrek.png"))
    img_lbl = ttk.Label(frm, image=poke_img)
    img_lbl.grid(row=0, column=0, padx=(5,10), pady=10)
    # defines function for when a pokemon selection is made from the combo box
    def cbo_select_event(event):
        # gets current selection
        current_sel = cbo_select.get()
        # gets the image URL for the selected pokemon
        poke_URL = PokeAPI.getPokeImgUrl(current_sel)
        # sets image path to script_dir images directory, appends the selected pokemons name and a png extension
        img_path = (script_dir + "\\Images\\" + current_sel + ".png")
        # downloads the pokemon image from the URL to the path defined in the previous line
        PokeAPI.downloadPokeImg(poke_URL, img_path)
        # sets the image contained in the label to the image downloaded in the previous line
        poke_img["file"] = img_path
        # enables a button so the picture can be set as the desktop background
        btn_set_dsktp.state(["!disabled"])
    # retrieves and sorts a list of pokemon names, creates combo box and links it to the combo box selection function
    poke_list = PokeAPI.getPokeList()
    poke_list.sort()
    cbo_select = ttk.Combobox(frm, values=poke_list, state="readonly")
    cbo_select.set("Select a Pokemon")
    cbo_select.grid(row=1, column=0, padx=10, pady=10, sticky=(N,E,S,W))
    cbo_select.bind("<<ComboboxSelected>>", cbo_select_event)
    # defines function for when the "btn_set_dsktp" button is pressed
    def btn_click_event():
        # gets current combo box selection
        current_sel = cbo_select.get()
        img_path = (script_dir + "\\Images\\" + current_sel + ".png")
        # sets the desktop background to the image downloaded earlier
        PokeAPI.setDsktpBckgrndImg(img_path)
    # creates button and links it to the button click event function
    btn_set_dsktp = ttk.Button(frm, text="Set as Desktop Image", command=btn_click_event)
    # sets the button to disabled until a combo box selection is made
    btn_set_dsktp.state(["disabled"])
    btn_set_dsktp.grid(row=2, column=0, padx=10, pady=10, sticky=(N,E,S,W))

    root.mainloop()


main()