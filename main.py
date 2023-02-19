from highlights import TextHighlights


terminal = TextHighlights()

terminal.log_error()
terminal.log_error("ERROR Message with default prefix ERROR", prefix=True)
terminal.log_error("ERROR Message without prefix", prefix=False)
terminal.log_error("ERROR with custom colors", color_type='hexa', fg="#22223b", bg="#9c89b8")

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
