from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    transcript = ""
    # Accepting the File to Transcribe
    if request.method == "POST":
        print("FORM DATA RECIEVED")

        
        if "file" not in request.files:
            return redirect(request.url)
        
        # File Must Be Included if not it takes user back to the home page
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        # Init SR
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            
            # Applying the SR APIs. Using Google Cloud
            transcript = recognizer.recognize_google(data, key=None)
            

    return render_template('index.html', transcript=transcript)

    


if __name__ == "__main__":
    app.run(debug=True, threaded=True)