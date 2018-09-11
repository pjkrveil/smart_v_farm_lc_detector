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

    python pano.py ./txtlists/filename_.txt


### Other WebSources for Images : 
Base paper for panorama using scale invariant features :

[1] "Automatic Panoramic Image Stitching using Invariant Features", Download.springer.com, 2016. [Online]. Available: matthewalunbrown.com/papers/ijcv2007.pdf
