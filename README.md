# Ararabots Univector Field 
by ***[Ararabots]***

Univector Field navigation is a navigation algorithm developed for dynamic environments. This project was implemented by Ararabots team's members, from UFMS, based on article ***[Evolutionary Univector Field-based Navigation
with Collision Avoidance for Mobile Robot]***, published on IFAC's world congress.
Beside the univector field algorithm, the project also has a plot system, to make possible display the generated field.


### Installation

In order to make use of Ararabots Univector Field, is necessary ***[Python]*** 3.5 version or latest.
To display the vector field, is also required the installation of ***[OpenCV]***.

The code was developed modularly, so is necessary to configure the environment variable PYTHONPATH, to allow python to use code in others directories. Follow the steps below to corfigure the variable:
On Terminal, type
``` sh
echo $PYTHONPATH
```
Is EXTREMELY IMPORTANT verify in the variable is not empty, . If the command above returns nothing but a empty line, there is nothing in the variable. Otherwise, there is data in the variable. Keep in mind this information.
Now, type
``` sh
nano .bashrc
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
And, it's done!
Anyway, fell free to put all code in one file, to avoid all this work. But is very prettier this way.


### Implementation

To use the Ararabots Univector Field, import the ***univector***.***py*** file. There is a lot of functions on file, but what matter to us, is ***generateUnivectorField***. Call this function, take a coffee and enjoy!


License
----

MIT


**Free Software, Hell Yeah!**

### Check our social media:
###### [Facebook]
###### [Twitter]
###### [Instagram]

[Facebook]:<https://www.facebook.com/ararabots>
[Twitter]:<https://twitter.com/ararabots>
[Instagram]:<https://www.instagram.com/ararabots/>
   [Evolutionary Univector Field-based Navigation
with Collision Avoidance for Mobile Robot]: <https://pdfs.semanticscholar.org/2a9c/19f306bc82a8ac22ee285f3a213e27c1e968.pdf>
[Python]: <https://www.python.org/downloads/>
[OpenCV]: <https://opencv.org/releases/>
[Ararabots]: <http://lia.facom.ufms.br/ararabots/2019/03/processo-seletivo-resultado-online/>
