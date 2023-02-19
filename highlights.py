"""
Production Script: Will youse final for deploying on pypi. 
"""

class TextHighlights:
    # INFO: Class Attributes 
    RED = '\033[38;5;235;48;5;9m'
    GREEN = '\033[38;5;255;48;5;70m'
    BLUE = '\033[48;5;39m'
    YELLOW = '\033[38;5;235;48;5;220m'
    ORANGE = '\033[38;5;235;48;5;214m'
    FOREGROUND = '\033[0m'
    BACKGROUND = '\033[0m'
    def __init__(self):
        # INFO: Instance Attributes
        self.bg_orange = '\033[38;5;235;48;5;214m'
        self.bg_red = '\033[38;5;235;48;5;9m'
        self.bg_green = '\033[38;5;255;48;5;70m'
        self.bg_yellow = '\033[38;5;235;48;5;220m'
        self.bg_blue = '\033[48;5;39m'
        self.bg_purple = '\033[38;5;235;48;5;134m'
        self.wrong_type = False

        self.bg_checking_green = '\033[38;5;235;48;5;109m'

        self.fg_green = '\033[38;5;28m'
        self.fg_purple = '\033[38;5;91m'
        self.fg_orange = '\033[38;5;214m'


        self.reset_color = '\033[38;5;255;48;5;0m'

        # FIXME : Remove - if not needed at the end. 
        # self.error = f"{self.bg_red}ERROR {self.reset_color}:"
        # self.success = f"{self.bg_green}SUCCESS {self.reset_color}:"
        # self.warning = f"{self.bg_yellow}WARNING {self.reset_color}:"
        # self.info = f"{self.bg_blue}INFO {self.reset_color}:"
        self.loading = f"{self.bg_purple}Loading...{self.reset_color}"
        self.checking= f"{self.bg_checking_green}Checking...↻{self.reset_color}"
        self.searching= f"{self.bg_checking_green}Searching...↻{self.reset_color}"

        self.color_dictionary = {}
        self.foreground_colors = []
        self.background_colors = []


    # TODO Work on learning about static and class methods. 
    # TODO Work on optimizing the whole code. 

    def custom_color_from_rgb(self, fg=None, bg=None):
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

    def custom_log(self, text:str=None, color_type:str=None, fg=None, bg=None ):
        """
        Description:
        Args: 
            fg: Can add value int, str, tuple
        """
        if color_type == 'rgb':
            xterm_color = self.custom_color_from_rgb(fg=fg, bg=bg)
            if self.wrong_type:
                return self.log_error("Give correct RGB Tuple.", prefix=True, bg=None, fg=9)
            else: 
                return f"{xterm_color}{text} \033[0m"
        elif color_type == 'hexa':
            xterm_color = self.custom_color_from_hexa(fg=fg, bg=bg)  
            if self.wrong_type:
                return self.log_error("Give correct HEXA color code.", prefix=True, bg=None, fg=9)
                
            else:
                return f"{xterm_color}{text} \033[0m"
        elif color_type == 'xterm':
            xterm_color = self.custom_color_from_xterm(fg=fg, bg=bg)
            if self.wrong_type:
                return self.log_error("Give Xterm 256 Standard Integer between 0 and 255", prefix=True, bg=None, fg=9)
                
            else:
                return f"{xterm_color}{text} \033[0m"
        else: 
            if color_type is not None:
                return self.message("You have Entered wrong color type.\nAvailable color_type: 'rgb', 'hexa', 'xterm' ")
            else: 
                return text

    # TODO Find a way to check for entered color type as well. 
    # IDEA use simple conversion method given below. for example rgb_to_xterm

    def message(self, text:str=None, color_type:str='xterm', fg=None, bg=None):
        """
        Description: For displaying messages
        """
        if text is None: 
            print(self.custom_log(text=text, color_type=color_type, fg=fg, bg=bg))
        else: 
            print(self.custom_log(text=text, color_type=color_type, fg=fg, bg=bg))
    """
    TODO Think about function name for example:
        1. terminal.log_error()
        2. terminal.print_error()
        3. terminal.error()

        FIXME Then change name of log_error_test method.
    """ 
    # def log_error(self, color=RED, text:str = "ERROR", color_type:str='xterm'):
    #     """
    #     Description:
    #     """
    #     if color_type == 'rgb':
    #         xterm_color = self.rgb_to_xterm(rgb=color)
    #         return f"{xterm_color}{text} \033[0m:"
    #     elif color_type == 'hexa':
    #         xt_color = self.hexa_to_xterm(color)
    #         return f"{xt_color}{text} \033[0m:"
    #     elif color_type == 'xterm':
    #         return f"{color}{text} \033[0m"
    #     else: 
    #         return f"Entered Wrong color type."
    
    def log_error(self, text:str=None, color_type:str='xterm', fg=9, bg=None, prefix:bool=False):
        if text is None:
            print(self.custom_log(text=text, color_type=color_type, fg=fg, bg=9 ))
        else: 
            if prefix:
                print(self.custom_log(text=f"ERROR: {text}", color_type=color_type, fg=fg, bg=bg))
            else: 
                print(self.custom_log(text=text, color_type=color_type, fg=fg, bg=bg))
        
        

    def log_warning(self, color:str=YELLOW, text:str="WARNING"):
        """
        Description:
        """
        return f"{color}{text} \033[0m:"
    
    def log_success(self, color:str=GREEN, text:str="SUCCESS"):
        """
        Description:
        """
        return f"{color}{text} \033[0m:"
    
    def log_info(self, color:str=BLUE, text:str="INFO"):
        """
        Description:
        """
        return f"{color}{text} \033[0m:" 
    
    # ============== # INFO - CONVERSIONS ================= # 
    def rgb_to_hex(self, rgb:tuple = (0, 0, 0)):
        try: 
            hexa = "#%02x%02x%02x" % rgb
            if len(hexa) == 7:
               return hexa
            else:
                return f"{self.log_error()} Entered wrong tuple value."      
        except TypeError:
            return f"{self.log_error()} Tuple needs only three arguments."

    # INFO I think this is a static method !
    def hex_to_rgb(self, hexa:str = "#000000"):
        try: 
            if hexa[0] == '#':
                hexa = hexa.split("#")[1]
                if len(hexa) == 6:
                    return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))
                else:
                    self.log_error("HEXA code length should be equal to 6 without # symbol.", fg=9, bg=None)
            else: 
                print(f"Hexa code should start with # string: #000000")
        except TypeError: 
            return self.log_error("Wrong HEXA code.")
        
    def rgb_to_xterm(self, rgb:tuple=(0, 0, 0), val=False):
        try: 
            if val: 
                return f"{rgb[0]};{rgb[1]};{rgb[2]}"
            else:
                return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
        except TypeError: 
            self.wrong_type = True

    def hexa_to_xterm(self, hexa:str="#000000", val_=False):
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



    # TODO Think about more suitable name for this. Either it should be a default colors or not? 
    # QUESTION How many color should I enter here. 
    def highlight(self, text:str, color:str):
        if color == 'g':
            return f"{self.fg_green}{text}{self.reset_color}"
        elif color == 'p':
            return f"{self.fg_purple}{text}{self.reset_color}"
        elif color == 'o':
            return f"{self.fg_orange}{text}{self.reset_color}"
        elif color == 'bg-g':
            return f"{self.bg_green}{text}{self.reset_color}"
        elif color == 'bg-r':
            return f"{self.bg_red}{text}{self.reset_color}"


    def custom_highlight(self, color, text):
            """
            Highlight text with custom ANSI Color. 
            """
            return f"{color}{text}{self.reset_color}"
    
    def create_color_dictionary(self, trigger_key, color):
        """
        Create color dictionary using custom keys, and color values.
        """
        if type(trigger_key) == list:
            for index, val in enumerate(trigger_key): 
                self.color_dictionary[val] = color[index]
        else: 
            self.color_dictionary[trigger_key] = color
        return self.color_dictionary
    
    def highlight_using_custom_dict(self, color, text):
        """
        Highlight text using custom dictionary created by you. 
        """

        if color in self.color_dictionary.keys():
            return f"{self.color_dictionary[color]}{text}{self.reset_color}"
        else: 
            return f"{color} doesn't exit in custom dictionary."
    
    def create_foreground_colors(self, number):
        if type(number) == list:
            for i in range(0, len(number)-1):
                color = f"\033[38;5;{number[i]}m"
                self.foreground_colors.append(color)
        else: 
            color = f"\033[38;5;{number}m"
            self.foreground_colors.append(color)
        return self.foreground_colors

    def create_background_colors(self, number):
        if type(number) == list:
            for i in range(0, len(number)-1):
                color = f"\033[48;5;{number[i]}m"
                self.background_colors.append(color)
        else: 
            color = f"\033[48;5;{number}m"
            self.background_colors.append(color)
        return self.background_colors




        

        
