# Ararabots Univector Field 
by ***[Ararabots]***

Univector Field navigation is a navigation algorithm developed for dynamic environments. This project was implemented by Ararabots team's members, from UFMS, based on article ***[Evolutionary Univector Field-based Navigation
with Collision Avoidance for Mobile Robot]***, published on IFAC's world congress.
Beside the univector field algorithm, the project also has a plot system, to make possible display the generated field.


### Installation

In order to make use of Ararabots Univector Field, is necessary ***[Python]*** 3.5 version or latest.
To display the vector field is also required the installation of ***[OpenCV]***.

The code was developed modularly, so is necessary to configure the environment variable PYTHONPATH, to allow python to use code in other directories. Follow the steps below to configure the variable:
On Terminal, type
``` sh
echo $PYTHONPATH
```
Is EXTREMELY IMPORTANT to verify in the variable is not empty. If the command above returns nothing but an empty line, there is nothing in the variable. Otherwise, there is data in the variable. Keep in mind this information.
Now, type
``` sh
nano ~/.bashrc
```
In case you use Atom or VSCode, you can replace nano by ***atom*** or ***code*** keywords, respectively.
On ***.bashrc***, below the last line, if the environment variable is empty, type
``` sh
export PYTHONPATH = the/absolute/path/of/project/root
```
If the variable is filled, type
``` sh
export PYTHONPATH = PYTHONPATH:the/absolute/path/of/project/root
```
And, it's done! Restart your terminal, and, it works!
Anyway, feel free to put all code in one file, to avoid all this work. But is very prettier this way.


### Implementation

To use the Ararabots Univector Field, import the ***univector***.***py*** file. The code is basically divided into four folders. The files on the root folder contain the univector implementation functions, as well as some necessary math functions. These files are the only one required to make use of the univector. Don't worry, the parameters and operation of each function are specified on comments. 
The abstract_module folder contains parameters, constants and variable used to generate the univector. Is not really necessary, if you pass these values as parameters for the univector functions. In draw_modules, you can see a bunch of draw functions. 
Finally, the folder debug_module stores a demo file for each univector field. There is a lot of files, but what matters to us, is ***composition.py***. Run this file, take a coffee and enjoy!


License
----

MIT


**Free Software, Hell Yeah!**

### Check our social media:
###### [Facebook]
###### [Twitter]
###### [Instagram]