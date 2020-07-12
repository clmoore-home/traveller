import collections
import tkinter as tk
import tkinter.scrolledtext as tkst

from planet import Planet

"""
Previous editions of Traveller and various websites may
describe planets using a single line of hexadecimal
code, such as:

Cogri 0101 CA6A643-9 N Ri Wa A

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
    """The main entry point. When instantiated, a GUI with the
    following attributes is created:
    Planet Name Entry, option button to Save to a file
    Planet Code Entry, option button to Decode string or clear the output text boxes
    Geography text box to display the geographical features of the planet
    Society text box to display information about the society and culture.
    
    Validation on code entry will display a warning message if the code entered is too short or long
    
    Enhancements:
    - Add check boxes for Naval Base, Scout Base etc to include information about those in output
    - Create various images of planets and display one based on geographical input (water, size, etc)
    - Add option to load previously saved planet and edit/add information"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Planet Decoder")
        self.minsize(300, 700)
        self.make_widgets()

    def make_widgets(self):
        self.planet_name_frame, self.planet_name_entry = self.default_frame(label='Planet Name:', WidgetName='Entry')
        self.planet_name_frame.grid(row=1, column=3, columnspan=2, pady=20)
        self.save_btn = self.base_widget(frame=self.planet_name_frame, text='Save', WidgetName='Button')
        self.save_btn.pack(padx=5, pady=5)
        self.code_entry_frame, self.entry = self.default_frame(label='Enter Planet Code:', WidgetName='Entry')
        self.decode_buttons()
        self.code_entry_frame.grid(row=1, column=1, columnspan=2, pady=20)
        self.entry.bind('<Key-Return>', self.handle_decode_request)
        self.geoframe, self.geography_text = self.default_frame(label='Geography', WidgetName='ScrolledText')
        self.geoframe.grid(row=3, column=1, columnspan=2)
        self.socframe, self.society_text = self.default_frame(label='Society', WidgetName='ScrolledText')
        self.socframe.grid(row=3, column=3, columnspan=2)
        
    def default_frame(self, *, frame=None, label=None, text=None, WidgetName=None):
        """Sets up a frame with an optional basic Widget packed in"""
        if not frame:
            frame = tk.Frame()
        if label:
            tk.Label(text=label, master=frame).pack()
        if WidgetName:
            WidgetName = self.base_widget(frame, WidgetName, text=text)
            WidgetName.pack()
        return frame, WidgetName
    
    def base_widget(self, frame, WidgetName, text=None):
        """Create a basic widget from input"""
        try:
            return getattr(tk, WidgetName)(master=frame, text=text)
        except AttributeError:
            return getattr(tkst, WidgetName)(master=frame, text=text)

    def decode_buttons(self):
        """Set up for the decode and clear buttons. Not as clean as the rest of the code..."""
        decode = self.base_widget(self.code_entry_frame, 'Button', 'Decode')
        decode.pack(side=tk.LEFT, padx=5, pady=5)
        clear = self.base_widget(self.code_entry_frame, 'Button', 'Clear')
        clear.pack(padx=5, pady=5)
        decode.bind('<Button-1>', self.handle_decode_request)
        clear.bind('<Button-1>', self.handle_clear_request)

    def insert_information_block(self, text_box, *info_block):
        """Inserts a block of information into the specified text_box based on info_blocks"""
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
        self.validate_decode_input()
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
        self.insert_information_block(self.society_text,
            f'Restricted Armour:', p.lawlevel_info_armour.restricted, 
            f'Permitted Armour:', p.lawlevel_info_armour.allowed)
        self.insert_information_block(self.society_text, f'Technology Level: {p.techlevel}')
        self.set_textbox_states(self.geography_text, self.society_text, state='disabled')
        
    def validate_decode_input(self):
        if not 7 < len(self.entry.get()) < 13:
            self.set_textbox_states(self.geography_text, self.society_text, fg='red', clear=True)
            self.geography_text.insert(tk.END, f'Warning: Code entered should be 10-11 \ncharacters long. Check for entry error.')
            self.set_textbox_states(self.geography_text, self.society_text, state='disabled', fg='red')

    def handle_clear_request(self, event):
        self.entry.delete(0, tk.END)


if __name__ == '__main__':
    app = Application()
    app.mainloop()