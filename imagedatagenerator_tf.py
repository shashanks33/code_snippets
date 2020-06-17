import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rotation_range = 40, # rotation upto 40 degrees out of 180
    rescale = 1./255,
    width_shift_range = 0.2, #alters the width
    height_shift_range = 0.2, # alters the height
    shear_range = 0.2, # shears the image with a range on 0-20 percent
    zoom_range = 0.2, # Zoom's into the image with a range on 0-20 percent
    horizontal_flip = True, #Flips the image horizontally
    fill_mode = 'nearest' #Fills pixels that might be lost in this process
    )
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
