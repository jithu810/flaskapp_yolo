from flask import Flask,render_template,request,make_response,jsonify,session,redirect,flash
app = Flask(__name__)



from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
import os
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import torch
import cv2






@app.route('/',methods=['GET','POST'])
def Home():
    if request.method == 'POST':
        file = request.files['f']  
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template("home.html", uploaded_image=filename)

    return render_template("home.html")






if __name__=="__main__":
    app.run()
    app.run(debug=True)