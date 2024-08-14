import pandas as pd
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load and preprocess the FER-2013 dataset
def load_fer2013_data(file_path):
    # Load data from CSV file
    df = pd.read_csv(file_path)
    
    # Extract features and labels
    X = df['pixels'].values
    y = df['emotion'].values
    
    # Process the images
    X_processed = []
    for pixel_sequence in X:
        pixels = np.fromstring(pixel_sequence, sep=' ', dtype=np.uint8)
        img = pixels.reshape(48, 48)
        img = cv2.resize(img, (48, 48))
        X_processed.append(img)
    
    X_processed = np.array(X_processed)
    X_processed = X_processed.reshape(-1, 48, 48, 1) / 255.0  # Normalize
    
    # Convert labels to categorical
    y_categorical = to_categorical(y, num_classes=7)
    
    return X_processed, y_categorical

# Build the CNN model
def build_model():
    model = Sequential([
        Conv2D(64, (3, 3), activation='relu', input_shape=(48, 48, 1)),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(7, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Train the model
def train_model():
    # Load and preprocess data
    file_path = 'fer2013.csv'  # Path to your dataset file
    X, y = load_fer2013_data(file_path)
    
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Data augmentation
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    train_generator = datagen.flow(X_train, y_train, subset='training')
    validation_generator = datagen.flow(X_train, y_train, subset='validation')
    
    # Build and train the model
    model = build_model()
    model.fit(
        train_generator,
        epochs=25,
        validation_data=validation_generator
    )
    
    # Save the model
    model.save('emotion_model.h5')

if __name__ == '__main__':
    train_model()
