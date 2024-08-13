from flask import Flask, request, jsonify, render_template
import numpy as np
import cv2
from tensorflow.keras.models import load_model # type: ignore

app = Flask(__name__)
model = load_model('emotion_model.h5')
#model = load_model('emotion_model.keras')  #whichever is used take that line

emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

@app.route('/predict', methods=['POST'])
def predict_emotion():
    #process the uploaded or captured image
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    
    # Read the image file
    img = file.read()
    img_array = np.fromstring(img, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        return jsonify({'error': 'Invalid image file'}), 400
    
    # Preprocess the image
    img = cv2.resize(img, (48, 48)) / 255.0
    img = img.reshape(1, 48, 48, 1)
    
    # Predict emotion
    preds = model.predict(img)
    emotion = emotion_labels[np.argmax(preds)]
    
    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(debug=True)
