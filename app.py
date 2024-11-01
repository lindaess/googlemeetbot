from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_transcription():
    data = request.get_json()
    
    # Check if the JSON payload has a "transcription" field
    if data and 'transcription' in data:
        transcription = data['transcription']
        print("Received transcription:", transcription)
        
        # Simulate processing the transcription
        response = {
            "status": "success",
            "message": "Transcription received successfully.",
            "received_text": transcription
        }
        return jsonify(response), 200
    else:
        return jsonify({"status": "error", "message": "No transcription provided."}), 400

if __name__ == "__main__":
    app.run(port=5000)
