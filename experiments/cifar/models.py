"""CNN model."""
from __future__ import print_function
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Lambda
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.advanced_activations import LeakyReLU


def CNN(input_shape, num_classes):
    """Return a simple CNN."""
    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding='same',
                     input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    return model

def VGG8(input_shape, num_classes, t_vec=None):

    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding='same', kernel_initializer='he_normal',
                                input_shape=input_shape))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2D(32, (3, 3), padding='same', kernel_initializer='he_normal'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(64, (3, 3), padding='same', kernel_initializer='he_normal'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2D(64, (3, 3), padding='same', kernel_initializer='he_normal'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.3))

    model.add(Conv2D(128, (3, 3), padding='same', kernel_initializer='he_normal'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2D(128, (3, 3), padding='same', kernel_initializer='he_normal'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))

    model.add(Flatten())
    model.add(Dense(512, kernel_initializer='he_normal'))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(num_classes, kernel_initializer='he_normal'))
    # output translate (tensorflow only)
    if t_vec is not None:
        def translate(x):
            return x - t_vec
        model.add(Lambda(lambda x: translate(x)))
    model.add(Activation('softmax'))

    return model


