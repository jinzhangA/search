import sklearn
from sklearn import model_selection
from search import search
import csv

bin_numbers = (2, 2, 3)

INDEXING_FILE = 'index.csv'
indexes = open(INDEXING_FILE)
reader = csv.reader(indexes)

# split he dataset into training(tuning) and testing dataset
train, test = model_selection.train_test_split(range(250), random_state=1)

total_correct = 0
# by default, training:testing = 0.75:0.25, so the total number of the samples is 1000*4*0.75
total_count = 4000.0*0.25
for sample in test:
    # train is samples from 0-250, convert it to a index between 4000 and 4999
    sample_indexs = map(lambda x: x+4000+sample*4, range(4))
    for i in sample_indexs:
        # formating the file index
        sample_index = '%05d' % (i)
        image_path = 'ukbench/ukbench%s.jpg' % (sample_index)
        results = search(image_path, INDEXING_FILE, bin_numbers)

        # each sample will return 4 results, iterate through them to check if they are correct
        # for example, for sample 4008, the correct result should be 4009, 4010, 4011 and 4008
        correct_count = 0
        for distance, image in results:
            result_index = int(image[7:12])
            if result_index in sample_indexs:
                correct_count += 1

        total_correct += correct_count
# accuracy = correct number / total number
print total_correct/total_count
