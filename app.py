import cv2
import numpy as np
import streamlit as st
from PIL import Image
import urllib.request

st.set_page_config(page_title="Pencil Sketch App", page_icon=":pencil:", layout="wide")

# Define a function to convert the input image to a pencil sketch
def convert_to_pencil_sketch(img):
    # Convert from BGR to RGB format
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_gray_img = 255 - gray_img

    # Apply Gaussian blur to the inverted image
    blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)

    # Convert the blurred image to pencil sketch using the divide blend mode
    pencil_sketch_img = cv2.divide(gray_img, 255 - blurred_img, scale=256)

    # Return the pencil sketch image
    return pencil_sketch_img

# Define the main function
def main():
    # Set the title and icon
    st.title("Pencil Sketch App")
    st.sidebar.title("Settings")
    st.sidebar.markdown("Upload an image and adjust the settings to convert it into a pencil sketch.")

    # Define the default image and load it
    #default_image_url = "https://images.unsplash.com/photo-1529318619245-5d91f86f1f1e"
    #filename = 'default.jpg'
    #urllib.request.urlretrieve(default_image_url, filename)
    #img = cv2.imread(filename)

    img_file_buffer = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if img_file_buffer is not None:
        # Read the image using OpenCV
        img = np.array(Image.open(img_file_buffer))
    else:
        # Use the default image
        #img = cv2.imread("android-chrome-192x192.png")
        st.warning('Please upload an image')  

    # Display the input image
    st.subheader("Input Image")
    st.image(img, caption="Input Image", use_column_width=True)

    # Convert the image to pencil sketch
    pencil_sketch_img = convert_to_pencil_sketch(img)

    # Display the pencil sketch image
    st.subheader("Pencil Sketch")
    st.image(Image.fromarray(pencil_sketch_img), caption="Pencil Sketch", use_column_width=True)

    # Save the output image
    cv2.imwrite("output_image.jpg", pencil_sketch_img)

if __name__ == "__main__":
    main()