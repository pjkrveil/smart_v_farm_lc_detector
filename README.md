# Image stitching with Python

This repository contains an implementation of multiple image stitching. For explanation refer my blog post : [Creating a panorama using multiple images]

### Requirements : 

- Python 3.6
- Numpy >= 1.11
- OpenCV 3.4.3


### Project Structure : 
	
		|_ code -|
		|		 |-- pano.py
		|		 |-- txtlists-|
		|		 			  |--files1.txt .... 
		|	
		|_ images - |
		|			|- img1.jpg
		|			|- abc.jpg 
		|			.... and so on ... 

Demo txtfile : 
files2.txt :

        ../../images/1.jpg
        ../../images/2.jpg
        ../../images/3.jpg
        ../../images/4.jpg

### To run : 

    `python pano.py <txtlists/filename_.txt>`


## Outputs !! 

<center>
<img src="lunchroom_ultimate.jpg" ><br>
<caption>Stitching with Lunchroom example</caption>
<br><br>
<img src="wd123.jpg" ><br>
<caption>Stitching with home example</caption>
<br><br>
<img src="test.jpg" ><br>
<caption>Stitching with building example</caption>
<br><br>
<img src="test12.jpg"><br>
<caption>Stitching using Hill example</caption>
<br><br>
<img src="test1.jpg" ><br>
<caption>Stitching using room example</caption>
<br>
</center>

### Other WebSources for Images : 
Base paper for panorama using scale invariant features :

[1] "Automatic Panoramic Image Stitching using Invariant Features", Download.springer.com, 2016. [Online]. Available: matthewalunbrown.com/papers/ijcv2007.pdf
