from app import app
from flask import render_template, request
from app.art_generator import art_creation, data_viz, image_manipulation, audio_manipulation, machine_learning

@app.route('/')
def index():
    artwork = art_creation.generate_random_art()
    return render_template('index.html', artwork=artwork)

@app.route('/visualization')
def visualization():
    chart = data_viz.generate_data_viz()
    return render_template('visualization.html', chart=chart)

@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        image = request.files['image']
        image_path = "app/static/uploaded_images/{}".format(image.filename)
        image.save(image_path)
        manipulated_image = image_manipulation.apply_filter(image_path)
        return render_template('upload_image.html', image=manipulated_image)
    return render_template('upload_image.html')

@app.route('/machine-learning')
def machine_learning_page():
    description = machine_learning.generate_description()
    return render_template('machine_learning.html', description=description)
