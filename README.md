# scratchpad
Basic notepad app with some built in calculator functions written in python using Tkinter.

Scratchpad can be used for notetaking and will automatically perform in-line math while you type.  For those interested, it basically finds any mathematical looking questions and throws them into python.

![Alt](./Screenshot.png "Screenshot1")  

### Supported Operations

* &nbsp;&nbsp; \+ &nbsp;&nbsp;&nbsp;&nbsp;(_addition_)
* &nbsp;&nbsp; \- &nbsp;&nbsp;&nbsp;&nbsp; (_subtract_)
* &nbsp;&nbsp; / &nbsp;&nbsp;&nbsp;&nbsp; (_divide_)
* &nbsp;&nbsp; \* &nbsp;&nbsp;&nbsp;&nbsp; (_multiply_)
* &nbsp;&nbsp; ** &nbsp;&nbsp;&nbsp;&nbsp; (_exponent_)
* &nbsp;&nbsp; () &nbsp;&nbsp;&nbsp;&nbsp; (_order of operations enforced by parenthesis_)
* &nbsp;&nbsp; == &nbsp;&nbsp;&nbsp;&nbsp; (_comparison, as in 6 == 2 * 3 => true_)


### How to install / run
#### Using this github repo / source code
Just download (clone or otherwise) everything here and run

`python3 scratchpad`

\-_or_\-

`./scratchpad`


#### Using PyPi package repo

`pip3 install scratchpad-deadmund`

`python3 -m scratchpad`


#### Generate a .deb and install that

_Still waiting to get package listed in Ubuntu_

`git clone https://github.com/fmresearchnovak/scratchpad`

`cd scratchpad`

`debuild --no-tgz-check`

`cd ../`

`sudo dpkg -i scratchpad_1.0_all.deb`

_then to run_

`scratchpad`