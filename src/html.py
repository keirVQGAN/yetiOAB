from PIL import Image as PILImage
import base64
import os

def html(title, text, image_path):
    """
    Create an HTML file for a manifesto with the specified title, text, and image.

    Args:
    - title (str): The title of the manifesto.
    - text (str): The main text of the manifesto.
    - image_path (str): The path to the image file.

    Returns:
    - None
    """
    # Load the HTML template
    with open('./ini/html/manifesto_template.html') as f:
        html_template = f.read()

    # Convert the text to HTML
    body_html = ''.join([f'<p>{p.strip()}</p>' for p in text.split('\n\n')])

    # Load the image
    with PILImage.open(image_path) as img:
        # Resize the image to fit inside the box and maintain the aspect ratio
        width, height = img.size
        aspect_ratio = height / width
        new_width = 300
        new_height = int(new_width * aspect_ratio)
        img = img.resize((new_width, new_height))

        # Convert the image to a base64-encoded string for embedding in the HTML
        with open('temp_image.png', 'wb') as f:
            img.save(f, format='png')
        with open('temp_image.png', 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')

        # Remove the temporary image file
        os.remove('temp_image.png')

    # Replace the placeholders with the specified title, text, and image
    html_content = html_template.replace("{{ title }}", title).replace("{{ text }}", body_html).replace("{{ image }}", f'data:image/png;base64,{image_data}')

    # Save the HTML content to a file with a unique name based on the title
    filename = f'{title.lower().replace(" ", "_")}.html'
    with open(f'/content/drive/MyDrive/yetiChat/out/{title}/{filename}', 'w') as f:
        f.write(html_content)  
