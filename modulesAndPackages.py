# import urllib
# dir(urllib)
# ['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__',
# '__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies',
# '_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost',
# '_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters',
# '_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook',
# 'addinfo', 'addinfourl', 'always_safe', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies',
# 'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'main', 'noheaders', 'os',
# 'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote',
# 'quote_plus', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport',
# 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test', 'test1',
# 'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode',
# 'urlopen', 'urlretrieve']

# help(urllib.urlopen)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     help(urllib.urlopen)
# NameError: name 'urllib' is not defined

# Each package in Python is a directory which MUST contain a special file called __init__.py.
    # This file can be empty, and it indicates that the directory it contains is a Python package,
    # so it can be imported the same way a module can be imported.
# If we create a directory called foo, which marks the package name,
    # we can then create a module inside that package called bar.
    # We also must not forget to add the __init__.py file inside the foo directory.
# To use the module bar, we can import it in two ways:
    # import foo.bar or from foo import bar

# The __init__.py file can also decide which modules the package exports as the API,
    # while keeping other modules internal, by overriding the __all__ variable, like so:
    # __init__.py:
    #
    # __all__ = ["bar"]

# Exercise
# In this exercise, you will need to print an alphabetically sorted list of all functions in the re module,
    # which contain the word find.
import re

find_members = []
for function in re:
    if 'find' in function:
        find_members.append(function)

print(sorted(find_members))
