Frequently asked questions
--------------------------

__Q__ : _what does "Brython" mean ?_

__A__ : <u>Br</u>owser P<u>ython</u>. It's also the Welsh word for "breton".

__Q__ : _which browsers support Brython ?_

__A__ : all modern browsers, including on smartphones. The generated Javascript purposely avoids using new syntax until it is supported by most browsers.

Note that performance is usually better (sometimes _much_ better) with Firefox than with Chrome.

__Q__ : _what is the performance of Brython compared to Javascript, or to other solutions that allow using Python in the browser ?_

__A__ : compared to Javascript, the ratio is naturally very different from one program to another. A Javascript console is provided in the distribution or on [the Brython site](http://brython.info/tests/js_console.html), it can be used to measure the execution time of a Javascript program compared to its equivalent in Python in the editor (unchecking the "debug" box)

The diffence is due to two factors :

- the time to translate Python into Javascript, on the fly in the browser. To give an idea, the module datetime (2130 lines of Python code) is parsed and converted to Javascript in 0,5 second on an ordinary PC
- JavaScript code generated by Brython must be compliant with the specifications of Python, including the dynamic nature of the search attributes, which leads to unoptimized Javascript code

Compared to other solutions that translate Python to Javascript, a benchmark is available on [Pierre Quentel's](https://brythonista.wordpress.com/2015/03/28/comparing-the-speed-of-cpython-brython-skulpt-and-pypy-js/) blog (he is the creator and main developer of Brython). It compares Brython, [Skulpt](http://skulpt.org) and [pypy.js](http://pypyjs.org/demo/). One must be careful with this kind of benchmark between implementation, but with the features tested, Brython is generally faster than pypy.js, itself faster than Skulpt. In some cases, Brython is faster than Python reference implementation, CPython.

The Brython repository includes a script, at address _localhost:8000/speed_, that
compares the speed of Bython and CPython on the local machine for a variety of
elementary operations.

__Q__ : _I see a lot of 404 errors in the browser console when I run Brython scripts, why is that ?_

__A__ : this is because of the way Brython implements the "import" mechanism. When a script has to import module X, Brython searches for a file or a package in different directories : the standard library (directory libs for Javascript modules, Lib for Python modules), the directory Lib/site-packages, the directory of current page. For that, Ajax calls are sent to the matching urls ; if the file is not found, the 404 error message is written in the browser console, but the error is caught by Brython which goes on searching until it finds the module, or raises `ImportError` if all paths have been tried with no result

__Q__ : _why does this message show in the browser console : "Synchronous XMLHttpRequest on the main thread is deprecated because of its detrimental effects to the end user's experience. For more help http://xhr.spec.whatwg.org/" ?_

__A__ : this is also related to imports, or to file reading. To achieve these operations, Brython uses _blocking_ Ajax calls : an imported module must be loaded before it can be used. Browser vendors should normally not remove blocking calls any time soon.

__Q__ : _is it possible to precompile Brython scripts, in order to reduce execution time ?_

__A__ : Brython is designed to be as simple to run as Javascript : put Python code in a `<script>` section of an HTML page, load the page, edit the code, reload the page, etc. It is not like other projects where the Python code is translated to Javascript by a CPython script, so for each modification you have to run this script before reloading the page.

Another reason why it is a not a good idea to precompile Brython is that the generated code is typically 10 times bigger than the original Python source - this is the price to pay for compliance with the language specification. The page would take longer to load, and we haven't found that this would be faster than compiling on the fly.

However, since version 3.6.0, a precompiled version of the scripts in the standard library is stored in an indexedDB database attached to the browser where the code is executed. The compilation is performed the first time a script is imported, or if the Brytohn version changed since the last compilation. This improves dramatically the imports loading time.

__Q__ : _why use the operator `<=` to build the tree of DOM elements ? This is not pythonic !_

__A__ : Python has no built-in structure to manipulate trees, ie to add "child" or "sibling" nodes to a tree node. For these operations, functions can be used ; the syntax proposed by Brython is to use operators : this is easier to type (no parenthesis) and more readable

To add a sibling node, the operator `+` is used

To add a child, the operator `<=` was chosen for these reasons :

- it has the shape of a left arrow ; note that Python function annotations use a new operator `->` that was chosen for its arrow shape
- it looks like an augmented assignment because of the equal sign
- it can't be confused with "lesser or equal" because a line with `document <= elt` would be a no-op if it was "lesser or equal", which is always used in a condition or as the return value of a function
- we are so used to interpret the 2 signs `<` and `=` as "lesser or equal" that we forget that they are a convention for programming languages, to replace the real sign `???`
- in Python, `<=` is used as an operator for sets with a different meaning than "lesser or equal"
- the sign `<` is often used in computer science to mean something else than "lesser than" : in Python and many other languages, `<<` means left shift ; in HTML tags are enclosed with `<` and `>`
- Python uses the same operator `%` for very different operations : modulo and string formatting

