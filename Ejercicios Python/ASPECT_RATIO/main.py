import requests
from PIL import Image
from io import BytesIO

def calculate_aspect_ratio(image_url):
    """
    Calculate the aspect ratio of an image from a URL.
    
    Args:
        image_url (str): URL of the image
        
    Returns:
        tuple: (width, height, aspect_ratio)
    """
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        image = Image.open(BytesIO(response.content))
        width, height = image.size
        aspect_ratio = width / height
        
        return width, height, aspect_ratio
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    url = input("Enter image URL: ")
    result = calculate_aspect_ratio(url)
    
    if result:
        width, height, ratio = result
        print(f"Width: {width}px")
        print(f"Height: {height}px")
        print(f"Aspect Ratio: {ratio:.2f} ({width}:{height})")