import os
import random

def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
    files = []
    for filename in os.listdir(SOURCE):
        file = SOURCE + filename
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename + " is zero length, so ignoring.")
    
    training_length = int(len(files) * SPLIT_SIZE) # length of training data
    testing_length = int(len(files) - training_length) # lenght of testing data
    shuffled_set = random.sample(files, len(files)) 
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[-testing_length:]

    for filename in training_set:
        this_file = SOURCE + filename
        destination = TRAINING + filename
        copyfile(this_file, destination)

    for filename in testing_set:
        this_file = SOURCE + filename
        destination = TESTING + filename
        copyfile(this_file, destination)

label1_source_dir = 'path of label1 data'
training_label1_dir = '/data/train/label1'
testing_label1_dir = '/data/test/label1'

label2_source_dir = 'path of label2 data'
training_label2_dir = '/data/train/label2'
testing_label2_dir = '/data/test/label2'

split_size = 0.75 # 75p train data and 25p test data

