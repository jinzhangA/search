import csv
from descriptor import chi2_distance
from descriptor import extract_feature
import cv2
import argparse
from matplotlib import pyplot as plt


def search(image_to_search, index_path, bin_numbers, plot=False, number_of_results=4):

    # open the index file
    indexes = open(index_path)
    reader = csv.reader(indexes)

    # load the image and extract the features
    image_to_search = cv2.imread(image_to_search)
    features_to_search = extract_feature(image_to_search, bin_numbers)
    results = {}

    # for each row, which is a recorded sample, calculate the distance with the searching image
    for row in reader:
        features = row[1:]
        features = map(float, features)
        d = chi2_distance(features, features_to_search)
        results[row[0]] = d

    indexes.close()

    # sort the result and find the first 'number_of_results' results
    results = sorted([(v, k) for (k, v) in results.items()])
    results = results[:number_of_results]

    # display the result if plot is true
    if plot:
        for (i, (distance, image_name)) in enumerate(results):
            image_path = 'ukbench/' + image_name
            image = cv2.imread(image_path)

            plot_index = 231 + i
            plt.subplot(plot_index)
            plt.imshow(image)
            plt.axis('off')

        plt.show()

    return results

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--index", required=True, help="The index of the image to be searched")
    args = vars(ap.parse_args())
    image_index = int(args['index'])
    image_index = '%05d'%(image_index)

    if not (int(image_index) >= 4000 and int(image_index) < 5000):
        print "Warning, illegal index number."
        exit()

    INDEXING_FILE = 'index.csv'
    image_path = 'ukbench/ukbench%s.jpg'%(image_index)

    indexes = open(INDEXING_FILE)
    bin_numbers = (2, 2, 3)
    print search(image_path, INDEXING_FILE, bin_numbers, True, 6)
