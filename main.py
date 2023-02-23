# from highlights import log
from highlighter import log

log.message("Message with default color!")
log.message("\n======== HEXA ========\n")  # use all default values
log.message(
    text="Message with custom foreground! - HEXA", color_type="hex", fg="#ff8fab"
)
log.message(
    text="Message with custom background - HEXA", color_type="hex", bg="#adc178"
)
log.message(
    text="Message with custom foreground and background color - HEXA",
    color_type="hex",
    fg="#f0e6ef",
    bg="#3d405b",
)

log.message("\n======== Xterm ========\n")  # use all default values
log.message(text="Message with custom foreground! - xterm", color_type="xterm", fg=166)
log.message(text="Message with custom background - xterm", color_type="xterm", bg=239)
log.message(
    text="Message with custom foreground and background color - xterm",
    color_type="xterm",
    fg=236,
    bg=112,
)


log.message("\n======== RGB ========\n")  # use all default values
log.message(
    text="Message with custom foreground! - rgb", color_type="rgb", fg=(39, 158, 126)
)
log.message(
    text="Message with custom background - rgb", color_type="rgb", bg=(229, 152, 155)
)
log.message(
    text="Message with custom foreground and background color - rgb",
    color_type="rgb",
    fg=(57, 48, 43),
    bg=(238, 185, 42),
)

print("\n======== With Prefix ========\n")
log.error("Type anything you like!", prefix=True)
log.warning("Type anything you like!", prefix=True)
log.success("Type anything you like!", prefix=True)
log.info("Type anything you like!", prefix=True)

print("\n======== Custom color with Prefix ========\n")
log.error("Custom foreground with prefix", prefix=True, fg=9)
log.error(
    "Custom foreground and background with prefix",
    prefix=True,
    color_type="hex",
    fg="#fae0e4",
    bg="#8c2f39",
)


print("\n======== Without Prefix ===========\n")
log.error("log error without prefix")
log.error("ERROR with custom colors", color_type="hex", fg="#545e56", bg="#edeec9")


print("\n======= Passing Variables =========\n")
dict = {
    "string_var": "string",
    "int_var": 2,
    "tuple_var": (2, 4, 5),
    "list_var": ["element01", "element02", "element"],
}

for key, value in dict.items():
    log.message(text=f"Dict Values: {value}", fg=104)


print(f"\nHighlight {log.highlight(text='Specific Part of')}your output")
