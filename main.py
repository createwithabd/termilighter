from highlights import TextHighlights


text = TextHighlights()

print(text.custom_log(
    color_type='rgb', 
    bg=(255, 153, 51), 
    fg=(51, 25, 0)
    ))
print(text.custom_log(
    color_type='hexa', 
    bg="#10DBB9", 
    fg="#10DBB9"
    ))
print(text.custom_log(color_type='test', bg="#10DBB9"))


