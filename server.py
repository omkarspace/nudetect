import logging
import os.path

from flask import Flask, request, render_template, send_file
from flask_cors import CORS

import main

template_dir = os.path.abspath('./page/')
app = Flask(__name__, template_folder=template_dir)
CORS(app)
app.logger.setLevel(logging.INFO)
handler = logging.FileHandler('app.log')
app.logger.addHandler(handler)


@app.route('/', methods=['GET'])
def get_home():
    return render_template('index.html')


@app.route('/from-video', methods=['POST'])
def from_video():
    app.logger.info(request.files['video'])
    main.clean()
    file = request.files['video']
    filename = file.filename
    file_path = './inputs/video/' + filename

    # Save the video file
    file.save(file_path)

    # Check if the file was saved correctly
    if not os.path.exists(file_path):
        app.logger.error("File not saved correctly.")
        return "File not saved", 500

    # Proceed with prediction if the file exists
    out = main.predict_per_frame()
    src = main.video_to_output(out)
    app.logger.info(f"Source: {src}")
    return src, 200



@app.route('/from-yt', methods=['POST'])
def from_yt():
    main.clean()
    out = main.ytvideo_predict_per_frame(request.get_json()['url'])
    src = main.video_to_output(out)
    app.logger.info(f"Source: {src}")
    return src, 200


@app.route('/output/video/video.mp4')
def return_video():
    return send_file('./output/video/video.mp4', mimetype='video/mp4')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
