# Highlighter  

Highlighter is build to color print terminal in Python. You can use this to print different kind message on the terminal.

## Requirements: 
1. Python version >= `3.8.10`

## Dependencies
This project has no dependencies and can be used with `windows`, and `Linux` operating system. 

## Installation
You can install it by running following command on your terminal.
~~~bash
pip install highlighter
~~~
OR 
~~~bash
pip3 install highlighter
~~~


## Usage 

To use this package, import `log` method from `highlighter` inside your required python script .
~~~python
from highlighter import log
~~~ 
Now, you can use `log` to output colored text on terminal. 

**For Example:**
~~~python
from highlighter import log
log.message("My first message using this package.")
~~~

### Output
![log.message](./images/log_message.png)

#### Arguments: 
1. `text` - 
2. `color_type` - 
3. `fg` - 
4. `bg` - 
5. `prefix` - 
6. `tag` - 
7. `default` -

You can change either foreground or background color.

### `log.error()`
### `log.warning()`
### `log.success()`
### `log.info()`

## Contributors
----
<div class='set' > 
    <a href="https://github.com/createwithabd/highlighter/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=createwithabd/highlighter" />
    </a>
</div>

------

<style>
.set {
    padding-top: 20px;
    padding-bottom: 10px
}
</style>
