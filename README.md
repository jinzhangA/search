# A image search engine of UKbench dataset
# Description
This is a image search engine base on HSV color histogram.
To perform a search:
```bash
python search.py -i INDEX
```
where INDEX is a number between. This project took a subset of the UKbench dataset. A valid INDEX would be a number 
between 4000 and 4999. Each image has 3 other images representing the same object.

The first result would always be the image itself and followed by 5 other images. There first 4 images are expected to 
be the images representing a same object. However, as this is not a perfect model, the results may appear after the 4th image. 
As a result, the 5th and 6th image are displayed for reference.

If there is no index.csv file, the index.py need to be run at the first time.

# Package
Most of the required packages, like numpy and ski-learn are included in Anaconda distribution.
Another required package for this project is openCV 2.4, which can be installed with conda as:
```bash
conda install -c menpo opencv=2.4.11
```
A useful image processing tool included in this project, imutils, can be installed with
```bash
[sudo] pip install imutils
```

