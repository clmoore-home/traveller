import collections
import tkinter as tk

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
        entry_frame = self.main_entry()
        decode_frame = self.button_frame()
        entry_frame.pack()
        decode_frame.pack()
        self.make_text_box()

    def make_text_box(self):
        s = tk.Scrollbar(self)
        self.text_display = tk.Text(self, height=4, width=100)
        self.text_display.pack(side=tk.LEFT, fill=tk.Y)
        s.pack(side=tk.RIGHT, fill=tk.Y)
        s.config(command=self.text_display.yview)
        self.text_display.config(yscrollcommand=s.set)

    def main_entry(self):
        tk.Label(text="Enter Planet Code:").pack(padx=5, pady=5)
        entry_frame = tk.Frame()
        self.entry = tk.Entry(master=entry_frame)
        self.entry.pack()
        self.entry.bind('<Key-Return>', self.handle_decode_request)
        return entry_frame

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

    def insert_information_block(self, *info_block):
        """Inserts a block of information into the text_display based on info tuple"""
        self.text_display.insert(tk.END, '\n'.join(info_block))
        self.text_display.insert(tk.END, '\n\n')

    def handle_decode_request(self, event):
        self.text_display.config(state='normal')
        try:
            self.text_display.delete(1.0, tk.END)
        except tk.TclError:
            pass
        self.validate_decode_input()
        p = Planet(self.entry.get())
        self.insert_information_block(f'Starport Rating {p.starport_rating}', p.starport_info)
        self.insert_information_block(f'Size Rating {p.size}', p.planet_size_info)
        self.insert_information_block(f'Atmospheric Rating {p.atmosphere}', p.atmosphere_info)
        self.insert_information_block(f'Hydrographics Rating {p.waterpercent}', p.hydrographic_info)
        self.insert_information_block(f'Population: {p.population_info}')
        self.insert_information_block(f'Goverment Rating {p.govtype}', p.government_info)
        self.text_display.insert(tk.END, f'Law Level: {p.lawlevel}\n')
        self.insert_information_block(f'Restricted Weapons:', p.lawlevel_info_weapons.restricted, 'Permitted Weapons:', p.lawlevel_info_weapons.allowed)
        self.insert_information_block(f'Restricted Armour:', p.lawlevel_info_armour.restricted, f'Permitted Armour:', p.lawlevel_info_armour.allowed)
        self.insert_information_block(f'Technology Level: {p.techlevel}')
        self.text_display.config(state='disabled')
    
    def validate_decode_input(self):
        if len(self.entry.get()) != 10:
            self.insert_information_block(f'Warning: Code entered should be 10 \ncharacters long. Check for entry error.' )
            self.text_display.config(state='disabled')

        
    
    def handle_clear_request(self, event):
        self.entry.delete(0, tk.END)


if __name__ == '__main__':
    app = Application()
    app.mainloop()