from PIL import Image, ImageFilter

def apply_filter(image_path):
    img = Image.open(image_path)
    img = img.convert("L")  # Convertir en noir et blanc
    img = img.filter(ImageFilter.GaussianBlur(5))  # Appliquer un flou
    img.save(image_path)  # Enregistrer l'image modifiée
    return image_path
