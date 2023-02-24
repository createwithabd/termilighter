# Termilighter  

Support by giving stars :star:  on `github`  - Follow for more.

A small module that allows you to customize print statements or output text with different colors. You can use any color type from the following `xterm`, `rgb`, and `hexa` to select a color for your output text. 

## Requirements: 
1. Python version >= `3` 

## Dependencies
This project has no dependencies till now and can be used with `windows`, and `Linux` operating system. 

## Installation
You can install it by running following command on your terminal.
~~~bash
pip install termilighter
~~~


## Usage

To use this package, import `log` method from `termilighter` inside your required python script .

~~~python
from termilighter import log
~~~

Now, you can use `log` to output colored text on terminal. 

##### Example - 01: Default Message

###### Input

~~~python
from termilighter import log
log.message(text="Message with custom foreground color.")
~~~

###### Output

<img src="https://raw.githubusercontent.com/createwithabd/termilighter/master/images/default_msg.png" alt="default" align="left" />

<br>

##### Example - 02: Message with Custom `Foreground` Color

###### Input

~~~python 
log.message(
    text="Message with custom foreground color.", color_type="hex", fg="#2a9d8f"
)
~~~

###### Output

<img src="https://raw.githubusercontent.com/createwithabd/termilighter/master/images/custom_fg.png" alt="custom-fg" align="left" />

<br>

##### Example - 03: Message with Custom `Background` Color

###### Input

~~~python
log.message(
    text="\nMessage with custom background color.", color_type="hex", bg="#d9ed92"
)
~~~

###### Output

<img src="https://raw.githubusercontent.com/createwithabd/termilighter/master/images/custom_bg.png" alt="custom-bg" align="left" />

<br>

##### Example - 05: Message with Custom `Foreground` & `Background` Color 

###### Input

~~~python
log.message(
    text="\nMessage with custom foreground and background color.",
    color_type="hex",
    fg="#dd6e42",
    bg="#eff7f6",
)
~~~

###### Output

<img src="https://raw.githubusercontent.com/createwithabd/termilighter/master/images/custom_fg_bg.png" alt="custom-bg-fg" align="left" />

<br>

##### Example - 06: Message with `Prefix` and Custom `Tag`

###### Input

~~~python 
log.message(text="Message with Prefix and custom-tag.", prefix=True, tag="custom-tag")
~~~

###### Output

<img src="https://raw.githubusercontent.com/createwithabd/termilighter/master/images/msg_with_tag.png" align="left" alt="custom-tag" />

<br>

##### Example - 07: Message with `Prefix`, Custom `Tag` and Custom `tag-color`

###### Input

~~~python 
log.message(
    text="Message with Prefix, custom-tag and custom tag color.",
    prefix=True,
    tag="custom-tag",
    dc=49,
)
~~~

###### Output: 

<img src="https://raw.githubusercontent.com/createwithabd/termilighter/master/images/custom_tag_color.png" align="left" />

<br>



## Available Features 

I build this module with flexibility to select any color type between `xterm` bit integer, `rgb` color tuple and `hexa` color code. You can use any color type to customize the output text on your terminal. There are some default methods as well which you can directly use to output respective text. Those methods are as follow; 

1. `log.message()` - You can put any string inside the curly brackets to display your text on the terminal. Default color is `put color`. 
2. `log.error()` - You can use this method to output `ERROR` on your terminal. 
3. `log.warning()` - You can use this method to output `WARNING` on your terminal. 
4. `log.success()` - You can use this method to output `SUCCESS` status on your terminal. 
5. `log.info()` - You can use this method to output any kind of important `INFO` on your terminal. 
6. `log.highlight()` - If you want to highlight any specific part in your print statement then, you can use this method inside the `f-string` or `.format` option of print statement.  

#### Common Options: 
1. `text` - Can provide any string value. **Default:** `None`. 
2. `color_type` - Can provide any color type from `xterm` , `rgb` and `hexa` . **Default:** `xterm`
3. `fg` - Can provide any foreground color with respect to its color type. For Example: 
   - For `xterm` - you can provide any integer between `1 and 255`
   - For `rgb` - You can provide `rgb` tuple `(r, g, b)`. 
   - For `hexa` - You can provide HEX color code `#000000`

4. `bg` - Same as foreground color you can provide any value with respective to `color_type` argument. 
5. `prefix` - Can be used in special method like `log.error()` - Prefix = `True` will display `[ ERROR ]` prefix at start of your output text. **Default:** `False`. 
6. `tag` - Can customize prefix tag as well. **Default:** `None`. 
7. `dc` - Default color to pass an argument to a method or it can be used to set the color for your prefix tag. 



------
## Other features 

1. `rgb_to_hex(rgb:tuple=(0, 0, 0))` 
2. `hex_to_rgb(hex:str = "#000000")` 
3. `rgb_to_xterm(rgb:tuple=(0, 0, 0), val = False)`
4. `hexa_to_xterm(hex:str = "#000000" val_ = False)`
5. `custom_color_from_rgb(fg=None, bg=None)`
6. `custom_color_from_hex(fg=None, bg=None)`
7. `custom_color_from_xterm(fg=None, bg=None)`

## Contributing

If you any suggestion to improve this package, feel free to create `issues` on `github`. Just create `PR` 

Support by giving stars :star:  on `github`  - Follow for more.

## Credits

Build with Love :heart:. 

##### Contributors

<div class='set' > 
    <a href="https://github.com/createwithabd/termilighter/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=createwithabd/termilighter" />
    </a>
</div>

------



