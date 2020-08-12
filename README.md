# MyWay - AI Search Problems

***
in this project , we will find the route with the shortest expected travel time, where travel time at 
A section is estimated by the average velocity in that section. <br>

the application will work with a data file "israel.csv" representing the Israeli road network .<br> We downloaded a map
from [openstreetmap](www.openstreetmap.org) website and conversion to a format that will be convenient to work .<br>
> db/israel.csv
<br>
<img width="450" height="190" alt="1" src="https://user-images.githubusercontent.com/69496372/89975585-cbaf5480-dc6e-11ea-93f5-52cbbfb990ba.png">
<br>

### structure :
israel.csv includes 944800 **rows** , each row describe a singe junction in israel .<br>
**first column** : junction index : [from 0 to 944799] <br>
**second column** : junction's latitude value .<br>
**3rd column** : junction's longitude value  .<br>
each column after that, describe a **Link** By 3 parameters separated by @ : 
* first parameter : Destination junction's index . 
* second parameter : link's length . 
* 3rd parameter : link's type . <br>

where link types defined in **info.py** file : there are 13 types : <br>
<img width="200" alt="Untitled" src="https://user-images.githubusercontent.com/69496372/89976329-d0750800-dc70-11ea-88bd-9e4d4eb38a1e.png">
<br>
## example : (openstreet map) : <br>
we choose a random junction in _Acre_ , marked in red , with coordinates : (32.9233454, 35.0712851). <br>
we see that there are a link between this junction and another 2 junctions : <br>
<img width="350"  height="250" alt="1" src="https://user-images.githubusercontent.com/69496372/89976742-edf6a180-dc71-11ea-9d00-d55de6cb7616.png">

this junction in israel.csv described with 626203 index : <br>
<img width="468" alt="2" src="https://user-images.githubusercontent.com/69496372/89976746-f058fb80-dc71-11ea-819b-59e8c97e75ef.png">
<br>
we see there are a path from this junction to : 626204 and 943029 : <br>
<img width="500" alt="3" src="https://user-images.githubusercontent.com/69496372/89976747-f0f19200-dc71-11ea-9c97-c6e474b496cd.png"><br>
we search about these two junctions (by a coordinates) in map to see if it matches: <br>
<img width="550" height="250" alt="4" src="https://user-images.githubusercontent.com/69496372/89976748-f18a2880-dc71-11ea-931c-b887e15fbdc1.png">
<br>

***
> problems.csv
<br>
include 100 row , each row consists of _source junction_ and _destination junction_

***
> stats.py
<br>
map_statistics function prints some information about roads graph <br>
to run : <br>

```
$ python stats.py
```
<br>
<img width="650" height="120" alt="Untitled" src="https://user-images.githubusercontent.com/69496372/89977424-c3a5e380-dc73-11ea-9a94-78a1956e25a1.png">
<br>
<br>
> main.py
<br>

## we want to compute the shortest expected travel time from source junction to destination junction :

# UCS
<br>
find_ucs_route function in UCS.py expect two parameters source junction index and destination index , and compute the shortest expected travel time from source to 
destination according to UCS algorithm <br>
we choose some problems from problems.csv and output the result to UCSRuns.txt 
<br>
in main.py , we can compute the path itself from source to destination junctions : <br>

```
$ python main.py ucs 30 50  
// 30 21 44 73 55
```

# A*
<br>
find_ucs_route function in Astar.py expect four parameters source junction index ,destination index , f function and heuristic function .
 and compute the shortest expected travel time from source to 
destination according to A* algorithm <br>
we choose some problems from problems.csv and output the result to AStarRuns.txt 
<br>

# IDA*

<br>
find_ucs_route function in IDAStar.py expect four parameters source junction index ,destination index , f function and heuristic function .
 and compute the shortest expected travel time from source to 
destination according to IDA* algorithm <br>
we choose some problems from problems.csv and output the result to IDAStarRuns.txt 
<br>

***

with draw.plot(path) function in ways/draw.py we draw the paths from two junctions : <br>
(these images in solution_img folder) <br>

<img width="500" height="300" src="https://user-images.githubusercontent.com/69496372/89978566-7c6d2200-dc76-11ea-801f-009754751bc4.png">
<img width="500" height="300" src="https://user-images.githubusercontent.com/69496372/89978574-7f681280-dc76-11ea-9d41-43afd7f21a2f.png">
<img width="500" height="300" src="https://user-images.githubusercontent.com/69496372/89978579-80993f80-dc76-11ea-9928-517e2b17fa6e.png">
<img width="500" height="300" src="https://user-images.githubusercontent.com/69496372/89978651-ab839380-dc76-11ea-88c8-bd25fbb8576c.png">

