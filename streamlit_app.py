from PIL import Image
import requests
from io import BytesIO
import streamlit as st

def crop_bottom_of_image_from_url(url: str, crop_ratio: float = 0.15) -> Image.Image:
    """
    Downloads an image from a URL and crops a percentage from the bottom.
    
    Args:
        url (str): URL of the image.
        crop_ratio (float): Fraction of the image height to crop from the bottom (0.0 to 1.0).
    
    Returns:
        PIL.Image.Image: The cropped image.
    """
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    width, height = img.size
    cropped_height = int(height * (1 - crop_ratio))
    return img.crop((0, 0, width, cropped_height))


st.title("Voici ton rébus ! 👰‍♀️")


st.image(
    "https://www.univers-musique.fr/wp-content/uploads/2017/04/partition-piano.png"
)

st.image(
    "https://media.istockphoto.com/vectors/woman-in-trouble-with-extreme-sweating-constitution-sweat-that-does-vector-id1314001476?k=20&m=1314001476&s=612x612&w=0&h=G3QHn3QnApdUSrzXpGb00yrzrH3ZIeC7xys8FduKkpw="
)

st.image(
    "https://static.vecteezy.com/system/resources/previews/017/399/394/original/a-pair-of-ace-playing-poker-cards-on-white-background-illustration-of-two-aces-winning-aces-vector.jpg"
)

st.image(
    "https://i.ytimg.com/vi/R2njjO007_I/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGEQgZShDMA8=&rs=AOn4CLDfv74j-JIOrH3cFSwMvXtEJ8doHQ"
)

st.image(
    "https://www.techowns.com/wp-content/uploads/2022/04/Pi-Symbol-on-Keyboard.jpg"
)

st.image(
    crop_bottom_of_image_from_url("https://c8.alamy.com/compfr/2fkdx60/illustration-vectorielle-de-dessin-anime-de-scie-a-main-isolee-2fkdx60.jpg")
)

st.image(
    crop_bottom_of_image_from_url("https://thumbs.dreamstime.com/z/rope-knot-vector-rope-knot-vector-eps-146466384.jpg")
)
