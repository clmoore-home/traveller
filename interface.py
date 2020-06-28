import collections
import tkinter as tk
import tkinter.scrolledtext as tkst

from planet import Planet

"""
Previous editions of Traveller and various websites may
describe planets using a single line of hexadecimal
code, such as:
Cogri 0101 CA6A643-9 N Ri Wa A
Once you get used to this method of laying out the
Characteristics of a planet, it becomes easy to decipher
during play.
The first component is the name.
The second component (the four digit number) is the
hex location (denoting column and row).
The next string of digits following the hex location
denote, in order:
• Starport quality
• Size
• Atmosphere Type
• Hydrographic percentage
• Population
• Government Type
• Law Level
• Tech Level - note that this is a range. e.g. in the above example, it's 3-9
The next component marks any bases present on the
world – examples include N for Naval Base, S for
Scout Base.
This is followed by any Trade Codes for the planet.
The travel zone for the system is next; A = Amber Zone,
R = Red Zone. If no code is given then the world is
either unclassified or a Green Zone.

"""

class Application(tk.Tk):
    """The main entry point"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Planet Decoder")
        self.minsize(300, 500)
        self.make_widgets()

    def make_widgets(self):
        # self.code_entry_frame, self.entry = self.default_entry_box(label='Enter Planet Code:')
        self.code_entry_frame, self.entry = self.default_frame(label='Enter Planet Code:', WidgetName='Entry')
        self.code_entry_frame.grid(row=1, column=1, columnspan=5)
        self.entry.bind('<Key-Return>', self.handle_decode_request)
        decode_frame = self.button_frame()
        decode_frame.grid(row=2, column=1, columnspan=5)
        # self.geoframe, self.geography_text = self.default_text_box('Geography')
        self.geoframe, self.geography_text = self.default_frame(label='Geography', WidgetName='ScrolledText')
        self.geoframe.grid(row=3, column=1, columnspan=2)
        # self.socframe, self.society_text = self.default_text_box('Society')
        self.socframe, self.society_text = self.default_frame(label='Society', WidgetName='ScrolledText')
        self.socframe.grid(row=3, column=3, columnspan=2)
        self.planet_name_frame, self.planet_name_entry = self.default_frame(label='Planet Name', WidgetName='Entry')
        self.planet_name_frame.grid(row=1, column=1, columnspan=2)

    def default_frame(self, label=None, WidgetName=None):
        frame = tk.Frame()
        if label:
            tk.Label(text=label, master=frame).pack()
        if WidgetName:
            try:
                pack_object = getattr(tk, WidgetName)(master=frame)
            except AttributeError:
                pack_object = getattr(tkst, WidgetName)(master=frame)
            pack_object.pack()
        return frame, pack_object

    def button_frame(self):
        frame = tk.Frame()
        self.decode_btn(frame)
        self.clear_btn(frame)
        return frame
    
    def make_default_btn(self, text, frame, style=None):
        button = tk.Button(text=text, master=frame)
        button.pack(padx=5, pady=5)
        return button

    def decode_btn(self, frame):
        btn_decode = self.make_default_btn('Decode', frame)
        btn_decode.pack(side=tk.LEFT)
        btn_decode.bind('<Button-1>', self.handle_decode_request)
        
    def clear_btn(self, frame):
        btn_clear = self.make_default_btn('Clear', frame)
        btn_clear.bind('<Button-1>', self.handle_clear_request)

    def insert_information_block(self, text_box, *info_block):
        """Inserts a block of information into the text_display based on info tuple"""
        text_box.insert(tk.END, '\n'.join(info_block))
        text_box.insert(tk.END, '\n\n')

    def set_textbox_states(self, *text_boxes, state='normal', fg='black', clear=False):
        """Sets the input textboxes to input states"""
        for tb in text_boxes:
            tb.config(state=state, fg=fg)
            if clear:
                try:
                    tb.delete(1.0, tk.END)
                except tk.TclError:
                    pass

    def handle_decode_request(self, event):
        self.set_textbox_states(self.geography_text, self.society_text, clear=True)
        p = Planet(self.entry.get())
        self.insert_information_block(self.geography_text, f'Starport Rating {p.starport_rating}', p.starport_info)
        self.insert_information_block(self.geography_text, f'Size Rating {p.size}', p.planet_size_info)
        self.insert_information_block(self.geography_text, f'Atmospheric Rating {p.atmosphere}', p.atmosphere_info)
        self.insert_information_block(self.geography_text, f'Hydrographics Rating {p.waterpercent}', p.hydrographic_info)
        self.insert_information_block(self.geography_text, f'Population: {p.population_info}')
        self.insert_information_block(self.society_text, f'Goverment Rating {p.govtype}', p.government_info)
        self.insert_information_block(self.society_text, f'Law Level: {p.lawlevel}', 
            'Restricted Weapons:', p.lawlevel_info_weapons.restricted, 
            'Permitted Weapons:', p.lawlevel_info_weapons.allowed)
        self.insert_information_block(self.society_text, f'Restricted Armour:', p.lawlevel_info_armour.restricted, f'Permitted Armour:', p.lawlevel_info_armour.allowed)
        self.insert_information_block(self.society_text, f'Technology Level: {p.techlevel}')
        self.set_textbox_states(self.geography_text, self.society_text, state='disabled')
        
    def validate_decode_input(self):
        if len(self.entry.get()) != 10:
            self.text_display['fg'] = 'red'
            self.text_display.insert(tk.END, f'Warning: Code entered should be 10 \ncharacters long. Check for entry error.')
            self.text_display.config(state='disabled')

    def handle_clear_request(self, event):
        self.entry.delete(0, tk.END)


if __name__ == '__main__':
    app = Application()
    app.mainloop()