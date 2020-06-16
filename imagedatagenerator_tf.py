import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255)
valid_datagen = ImageDataGenerator(rescale=1./255)

train_dir = ''
valid_dir = ''

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size = (300,300),
    batch_size = 128,
    class_mode = 'binary',
)

valid_generator = valid_datagen.flow_from_directory(
    valid_dir,
    target_size=(300, 300),
    batch_size=128,
    class_mode='binary',
)


# Labels will be the names of the folders have that specific photo
# Ex: folder named human = photos of human and the label is human

# class_mode = binary if we are classifying two objects like humans or horses
