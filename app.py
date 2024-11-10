# from flask import Flask, request, render_template, send_file
# import cv2
# import numpy as np
# from PIL import Image
# from image_enhancement import enhance_image

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/enhance', methods=['POST'])
# def enhance():
#     file = request.files['image']
#     if file:
#         img_path = 'uploaded_image.jpg'
#         file.save(img_path)
#         # Enhance the image
#         enhanced_img = enhance_image(img_path)
#         output_path = 'enhanced_image.jpg'
#         cv2.imwrite(output_path, enhanced_img)
#         return send_file(output_path, as_attachment=True)
#     return "No file uploaded!"

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, render_template, send_file
import cv2
import numpy as np
from image_enhancement import enhance_image
import io
from PIL import Image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enhance', methods=['POST'])
def enhance():
    file = request.files['image']
    if file:
        img_path = 'uploaded_image.jpg'
        file.save(img_path)
        # Enhance the image
        enhanced_img = enhance_image(img_path)
        
        # Convert OpenCV image to PIL format and save it in memory
        _, buffer = cv2.imencode('.jpg', enhanced_img)
        image_stream = io.BytesIO(buffer)
        return send_file(image_stream, mimetype='image/jpeg')

    return "No file uploaded!", 400

if __name__ == "__main__":
    app.run(debug=True)
