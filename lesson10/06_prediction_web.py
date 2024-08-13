import streamlit as st 
from skimage import io
from skimage.transform import resize

import numpy as np
from keras._tf_keras import keras

model = keras.models.load_model('model.h5')

st.title("上傳圖片(0~9)辨識")

uploaded_file = st.file_uploader("上傳圖片(.png)", type="png")
if uploaded_file is not None:
    image1 = io.imread(uploaded_file, as_gray=True)
    image_resized = resize(image1, (28, 28), anti_aliasing=True)    
    X1 = image_resized.reshape(1,28, 28) #/ 255
    X1 = np.abs(1-X1)
    st.write("predict...")
    predictions = np.argmax(model.predict(X1), axis=-1)
    st.markdown(f"# {predictions[0]}")
    st.image(image1)
