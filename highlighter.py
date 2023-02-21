"""
Author: Abdullah Amjad 
Data of Creation: 21.02.2023
Contributor: ''
"""

class TextHighlights:
    # INFO: Class Attributes 
    RESET_COLOR = '\033[0m'
    MY_COLOR = 9
    
    def __init__(self, wrong_type: bool =False):

        # INFO: Instance Attributes
        self.wrong_type = wrong_type

    def custom_color_from_rgb(self, fg=None, bg=None):
        """
        Description: return xterm color with custom foreground and background from rgb color tuple. default values are None.
        Arguments:-
            fg: tuple - rgb color tuple for foreground. Example (r, g, b)
            bg: tuple - rgb color tuple for background. Example (r, g, b)
        """
        if type(fg) == tuple or type(bg) == tuple:
            self.wrong_type = False
            if fg is None: 
                bg_color = self.rgb_to_xterm(rgb=bg, val= True)
                final_color = f"\033[48;2;{bg_color}m"
            elif bg is None:
                fg_color = self.rgb_to_xterm(rgb=fg, val= True)
                final_color = f"\033[38;2;{fg_color}m"
            else:
                fg_color = self.rgb_to_xterm(rgb=fg, val=True)
                bg_color = self.rgb_to_xterm(rgb=bg, val=True)
                final_color = f"\033[38;2;{fg_color};48;2;{bg_color}m"
            return final_color
        else: 
            if fg is None and bg is None:
                return f"\033[0m"
            else: 
                self.wrong_type = True   
    

    def custom_color_from_hexa(self, fg=None, bg=None):
        """
        Description: return xterm color with custom foreground and background from hexa color code. default values are None.
        Arguments:-
            fg: str - hexa color code for foreground. Example #000000
            bg: str - hexa color code for background. Example #000000
        """
        if type(fg) == str or type(bg) == str: 
            self.wrong_type = False
            if fg is None: 
                bg_color = self.hexa_to_xterm(hexa=bg, val_= True)
                final_color = f"\033[48;2;{bg_color}m"
            elif bg is None:
                fg_color = self.hexa_to_xterm(hexa=fg, val_= True)
                final_color = f"\033[38;2;{fg_color}m"
            else:
                fg_color = self.hexa_to_xterm(hexa=fg, val_=True)
                bg_color = self.hexa_to_xterm(hexa=bg, val_=True)
                final_color = f"\033[38;2;{fg_color};48;2;{bg_color}m"
            
            return final_color
        else: 
            if fg is None and bg is None:
                return f"\033[0m"
            else: 
                self.wrong_type = True    


    def custom_color_from_xterm(self, fg=None, bg=None):
        """
        Description: return xterm color with custom foreground and background from 256 standard bits. default values are None.
        Arguments:-
            fg: int -  bits value between 0 and 255 for foreground. Example 25
            bg: int -  bits value between 0 and 255 for background. Example 25
        """
        if type(fg) == int or type(bg) == int: 
            self.wrong_type = False
            if fg is None: 
                final_color = f"\033[48;5;{bg}m"
            elif bg is None:
                final_color = f"\033[38;5;{fg}m"
            else:
                final_color = f"\033[38;5;{str(fg)};48;5;{str(bg)}m"
            return final_color
        else: 
            if fg is None and bg is None:
                return f"\033[0m"
            else: 
                self.wrong_type = True


    # TODO Think about best description for this method.
    def create_custom_color(self, color_type:str=None, fg=None, bg=None):
        if color_type == 'rgb':
            return self.custom_color_from_rgb(fg=fg, bg=bg)
        elif color_type == 'hexa':
            return self.custom_color_from_hexa(fg=fg, bg=bg)  
        elif color_type == 'xterm':
            return self.custom_color_from_xterm(fg=fg, bg=bg)
        else: 
            if color_type is not None:
                return self.message("You have Entered wrong color type.\nAvailable color_type: 'rgb', 'hexa', 'xterm' ")


    def message(self, text:str=None, color_type:str='xterm', fg=None, bg=None):
        """
        Description: show your message on terminal with custom foreground and background colors.
        Arguments:-
            text: Message to display on the terminal. default-None
            color_type: color type for creating foreground and background color. default - 'xterm', Available - 'rgb', 'hexa'. 
            fg: Foreground color, default - None
            bg: Background color, default - None

        """  
        custom_color = self.create_custom_color(color_type=color_type, fg=fg, bg=bg)
        if text is None: 
            if self.wrong_type:
                print(self.error("Give Xterm 256 Standard Integer between 0 and 255", prefix=True, bg=None, fg=9))
            else:
                print(f"{custom_color}{text} \033[0m")
        else: 
            if self.wrong_type:
                print(self.error("Give Xterm 256 Standard Integer between 0 and 255", prefix=True, bg=None, fg=9))
            else:
                custom_color = self.create_custom_color(color_type=color_type, fg=146, bg=bg)
                print(f"{custom_color}{text} \033[0m")


    def prefix(self, tag:str=None, color:int=207):
        try: 
            if tag is None: 
                return f"\033[1m[\033[0m\033[38;5;{color}m {tag} \033[0m\033[1m]\033[0m "
            elif tag is not None: 
                return f"\033[1m[\033[0m\033[38;5;{color}m {tag} \033[0m\033[1m]\033[0m "
        except TypeError:
            print("Please provide an integer to color argument.")


    def colorCustomization(self, text=None, color_type='xterm', fg=None, bg=None, default=None, is_return=False, prefix=False, tag=None):
        if text is None:
            color = self.create_custom_color(color_type=color_type, fg=fg, bg=bg)
        
            if self.wrong_type:
                print(self.error("Give Xterm 256 Standard Integer between 0 and 255", prefix=True, bg=None, fg=TextHighlights.MY_COLOR))
            else: 
                if is_return:
                    return f"{color}{text} \033[m"
                else: 
                    print(f"{color}{text} \033[m")
        else: 
            if prefix: 
                color = self.create_custom_color(color_type=color_type, fg=fg, bg=bg)
                if self.wrong_type:
                    print(self.error("Give Xterm 256 Standard Integer between 0 and 255", prefix=True, bg=None, fg=TextHighlights.MY_COLOR))
                else: 
                    print(f"{self.prefix(tag=tag, color=default)}{color}{text} \033[0m")
            else: 
                if fg is None and bg is None:
                    color = self.create_custom_color(color_type=color_type, fg=default, bg=bg)
                else: 
                    color = self.create_custom_color(color_type=color_type, fg=fg, bg=bg)
                
                if self.wrong_type:
                    print(self.error("Give Xterm 256 Standard Integer between 0 and 255", prefix=True, bg=None, fg=147))
                else: 
                    if is_return:
                        return f"{color}{text} \033[0m"
                    else: 
                        print(f"{color}{text} \033[m")

    
    def error(self, text:str=None, color_type:str='xterm', fg=None, bg=None, prefix:bool=False):
        self.colorCustomization(text=text, color_type=color_type, fg=fg, bg=bg, default=9, prefix=prefix, tag='ERROR' )

        
    def warning(self, text:str=None, color_type:str='xterm', fg=None, bg=None, prefix:bool=False):

        self.colorCustomization(text=text, color_type=color_type, fg=fg, bg=bg, default=214, prefix=prefix, tag='WARNING' )


    def success(self, text:str=None, color_type:str='xterm', fg=None, bg=None, prefix:bool=False):
        self.colorCustomization(text=text, color_type=color_type, fg=fg, bg=bg, default=112, prefix=prefix, tag='SUCCESS' )


    def info(self, text:str=None, color_type:str='xterm', fg=None, bg=None, prefix:bool=False):
        self.colorCustomization(text=text, color_type=color_type, fg=fg, bg=bg, default=105, prefix=prefix, tag='INFO' )


    def highlight(self, text:str= None, color_type:str='xterm', fg=None, bg=None ):
        return self.colorCustomization(text=text, color_type=color_type, fg=fg, bg=bg, default=165, is_return=True)

    # ============== # INFO - CONVERSIONS ================= #

    def rgb_to_hex(self, rgb:tuple = (0, 0, 0)):
        """
        Description: return hexa color code from rgb color tuple. 
        Arguments:-
            rgb: Take rgb color tuple as an input argument. default - (0, 0, 0)
        """
        try: 
            hexa = "#%02x%02x%02x" % rgb
            if len(hexa) == 7:
               return hexa
            else:
                self.error(f"Entered wrong tuple value.", fg=TextHighlights.MY_COLOR, bg=None, prefix=True)
        except TypeError:
            self.wrong_type = True
            self.error(f"Tuple needs only three arguments.", fg=TextHighlights.MY_COLOR, bg=None, prefix=True)

    def hex_to_rgb(self, hexa:str = "#000000"):
        """
        Description: return rgb color tuple from hexa color code. 
        Arguments:-
            hexa: Take hexa color code as an input argument. default - #000000
        """
        try: 
            if hexa[0] == '#':
                hexa = hexa.split("#")[1]
                if len(hexa) == 6:
                    return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))
                else:
                    self.error(f"HEXA code length should be equal to 6 without # symbol.", fg=TextHighlights.MY_COLOR, bg=None, prefix=True)
            else: 
                self.error(f"Hexa code should start with # string: #000000", fg=TextHighlights.MY_COLOR, bg=None, prefix=True)
        except TypeError: 
            self.wrong_type = True
            self.error(f"Wrong HEXA code.", fg=TextHighlights.MY_COLOR, bg=None, prefix=True)

    def rgb_to_xterm(self, rgb:tuple=(0, 0, 0), val=False):
        """
        Description: return either xterm string or xterm color from rgb color tuple.
        Arguments:-
            rgb: Take rgb color tuple as an input. Default - (0, 0, 0) 
            val: Return xterm string color if True, Return xterm color if False.
        """
        try: 
            if val: 
                return f"{rgb[0]};{rgb[1]};{rgb[2]}"
            else:
                return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
        except TypeError: 
            self.wrong_type = True

    def hexa_to_xterm(self, hexa:str="#000000", val_:bool=False):
        """
        Description: return either xterm string or xterm color from hexa color code.
        Arguments:-
            hexa: Hexa color code. Default #000000
            val_: Return xterm string color if True, Return xterm color if False.
        """
        rgb = self.hex_to_rgb(hexa=hexa)
        try: 
            if val_: 
                xterm_color = self.rgb_to_xterm(rgb=rgb, val=val_)
                return xterm_color
            else: 
                xterm_color = self.rgb_to_xterm(rgb=rgb)
                return xterm_color
        except TypeError:
            self.wrong_type = True




     

# Calling class here!!

log = TextHighlights()


