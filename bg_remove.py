import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Eliminador de fondo de imagen", page_icon=":dog:")

st.write("## Borrar el fondo de la Imagen 3")
st.write(
    ":dog: Intenta subir una imagen para ver cómo se elimina mágicamente el fondo. Las imágenes de alta calidad se pueden descargar desde el panel lateral."
)
st.sidebar.write("## Subir imagen para descargar :gear:")


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Imagen original :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Imagen ajustada :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Descargar imagen ajustada", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Subir una imagen", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./mini-yoda.jpg")
