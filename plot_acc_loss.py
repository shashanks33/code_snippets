%matplotlib inline

import matplotlib.image  as mpimg
import matplotlib.pyplot as plt

# If, history = model.fit_generator is used with validation_generator too then use the below code
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

# No of epochs
epochs = range(len(acc))

# Plot the training and validation accuracy per epoch
plt.plot(epochs, acc, 'r', 'Training accuracy')
plt.plot(epochs, val_acc, 'b', 'Validation accuracy')
plt.title('Training and validation accuracy')
plt.figure()

plt.plot(epochs, loss, 'r', "Training Loss")
plt.plot(epochs, val_loss, 'b', "Validation Loss")
plt.title('Training and validation loss')
plt.figure()
