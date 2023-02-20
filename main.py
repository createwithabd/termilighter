# from highlights import terminal
from highlights import TextHighlights


terminal = TextHighlights()

terminal.error()
terminal.error("Message with default prefix ERROR", prefix=True)
terminal.error("Message without prefix", prefix=False)
terminal.error("ERROR with custom colors", color_type='hexa', fg="#22223b", bg="#4cbc84")

print("\n")

terminal.message(text='Message with default values' ) # use all default values
terminal.message(text="Message with custom foreground! - HEXA" ,color_type='hexa', fg="#d5bdaf")
terminal.message(text="Message with custom background - HEXA", color_type='hexa', bg="#e76f51")
terminal.message(text="Message with custom foreground and background color - HEXA", color_type='hexa', fg="#f0e6ef", bg="#3d405b")

print("\n")
terminal.message(text='Message with DEFAULT VALUES' ) # use all default values
terminal.message(text="Message with custom foreground! - xterm" ,color_type='xterm', fg=166)
terminal.message(text="Message with custom background - xterm", color_type='xterm', bg=135)
terminal.message(text="Message with custom foreground and background color - xterm", color_type='xterm', fg=52, bg=51)

print("\n")
terminal.message(text='Message with DEFAULT VALUES' ) # use all default values
terminal.message(text="Message with custom foreground! - rgb" ,color_type='rgb', fg=(206, 127, 252))
terminal.message(text="Message with custom background - rgb", color_type='rgb', bg=(15, 189, 166))
terminal.message(text="Message with custom foreground and background color - rgb", color_type='rgb', fg=(57, 48, 43), bg=(233, 104, 30))


print("\nYou can pass variable as well!!")




dict = {
    "string_var": 'string',
    "int_var": 2,
    "tuple_var": (2, 4, 5),
    "list_var": ['element01', 'element02', 'element'] 
}

for key, value in dict.items():
    terminal.message(text=f"Dict Values: {value}", fg=154)



# terminal.warning('HEALLO',prefix=True)
# print(terminal.custom_log(
#     color_type='rgb', 
#     bg=(255, 153, 51), 
#     fg=(51, 25, 0)
#     ))
# print(terminal.custom_log(
#     color_type='hexa', 
#     bg="#855571", 
#     fg="#e1dad8"
#     ))
# print(terminal.custom_log(color_type='hexa'))



terminal.error("Type anything you like!", prefix=True)
terminal.warning("Type anything you like!", prefix=True)
terminal.success("Type anything you like!", prefix=True)
terminal.info("Type anything you like!", prefix=True)

terminal.error("TEST", prefix=True, color_type='hexa', fg='#edf2f4', bg='#d90429')
terminal.error("TEST 2", prefix=True, fg=204)


