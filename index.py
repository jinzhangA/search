from imutils import paths
import cv2
import descriptor

INDEXING_FILE = 'index.csv'
DATA_SET = 'ukbench'

bin_numbers = (2, 2, 3)
output = open(INDEXING_FILE, "w")
images = list(paths.list_images(DATA_SET))

# iterate through the dataset, extract the features to form a indexing file
# This part of code took some reference from:
# http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/
for (i, imagePath) in enumerate(images):
    filename = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    features = descriptor.extract_feature(image, bin_numbers)
    features = map(str, features)
    output.write("{},{}\n".format(filename, ",".join(features)))
output.close()
