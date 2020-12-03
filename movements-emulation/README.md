## You need to install PyQt  
>  conda install -c anaconda pyqt
## Usage
### Run
> <pre>python __main__.py</pre>
### Record Movements
Click record to record a new movements  
Drag and drop the circles to move them around : it is the movement
Once you release the click the movement is finished  
Do this as many times as you want, every movement will be given the same output for training  
Click stop recording when you recorded enough times this movement  
You can then record another movement following the same process
### Saving
Don't forget to stop recording and once you're done click the Save to file button  
All the recorded movement matrices are saved in the dataset.csv file  
The file will be automatically overwritten so be careful
## Nota Bene
If you record only one movement one time, the program will crash when saving :)
