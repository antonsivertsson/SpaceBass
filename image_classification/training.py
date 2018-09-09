import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout # components of network
from keras.models import Sequential # type of model

x_train_set_fpath = '../../../sat_dataset/X_train_sat4.csv'
y_train_set_fpath = '../../../sat_dataset/y_train_sat4.csv'
print ('Loading Training Data')
X_train = pd.read_csv(x_train_set_fpath)
print ('Loaded 28 x 28 x 4 images')


Y_train = pd.read_csv(y_train_set_fpath)
print ('Loaded labels')


X_train = X_train.as_matrix()
Y_train = Y_train.as_matrix()
print ('We have',X_train.shape[0],'examples and each example is a list of',X_train.shape[1],'numbers with',Y_train.shape[1],'possible classifications.')


#First we have to reshape each of them from a list of numbers to a 28*28*4 image.
X_train_img = X_train.reshape([99999,28,28,4]).astype(float)
print (X_train_img.shape)

model = Sequential([
    Dense(4, input_shape=(3136,), activation='softmax')
])


X_train = X_train/255


from keras.callbacks import ModelCheckpoint

filepath = "trained_model.h5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
model.fit(X_train,Y_train,batch_size=32, epochs=5, verbose=1, validation_split=0.01, callbacks=callbacks_list)


