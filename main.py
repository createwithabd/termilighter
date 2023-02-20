# from highlights import terminal
from highlights import TextHighlights


terminal = TextHighlights()


terminal.message('\n======== HEXA ========\n' ) # use all default values
terminal.message(text="Message with custom foreground! - HEXA" ,color_type='hexa', fg="#ff8fab")
terminal.message(text="Message with custom background - HEXA", color_type='hexa', bg="#adc178")
terminal.message(text="Message with custom foreground and background color - HEXA", color_type='hexa', fg="#f0e6ef", bg="#3d405b")

terminal.message('\n======== Xterm ========\n'  ) # use all default values
terminal.message(text="Message with custom foreground! - xterm" ,color_type='xterm', fg=166)
terminal.message(text="Message with custom background - xterm", color_type='xterm', bg=239)
terminal.message(text="Message with custom foreground and background color - xterm", color_type='xterm', fg=236, bg=112)


terminal.message('\n======== RGB ========\n' ) # use all default values
terminal.message(text="Message with custom foreground! - rgb" ,color_type='rgb', fg=(39, 158, 126))
terminal.message(text="Message with custom background - rgb", color_type='rgb', bg=(229, 152, 155))
terminal.message(text="Message with custom foreground and background color - rgb", color_type='rgb', fg=(57, 48, 43), bg=(238, 185, 42))

print('\n======== With Prefix ========\n')
terminal.error("Type anything you like!", prefix=True)
terminal.warning("Type anything you like!", prefix=True)
terminal.success("Type anything you like!", prefix=True)
terminal.info("Type anything you like!", prefix=True)

print('\n======== Custom color with Prefix ========\n')
terminal.error("Custom foreground with prefix", prefix=True, fg=9)
terminal.error("Custom foreground and background with prefix", prefix=True, color_type='hexa', fg='#fae0e4', bg='#8c2f39')


print("\n======== Without Prefix ===========\n")
terminal.error("log error without prefix")
terminal.error("ERROR with custom colors", color_type='hexa', fg="#545e56", bg="#edeec9")


print("\n======= Passing Variables =========\n")
dict = {
    "string_var": 'string',
    "int_var": 2,
    "tuple_var": (2, 4, 5),
    "list_var": ['element01', 'element02', 'element'] 
}

for key, value in dict.items():
    terminal.message(text=f"Dict Values: {value}", fg=104)


