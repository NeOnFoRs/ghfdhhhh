from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

texts = [{'text': 'Пример текста', 'style': {'left': '50px', 'top': '50px', 'color': '#000000', 'transform': 'scale(1)'}}]

@app.route('/')
def index():
    return render_template('input.html', texts=texts)

@app.route('/output')
def output():
    return render_template('output.html', texts=texts)

@app.route('/api/update_text', methods=['GET', 'POST'])
def update_text():
    global texts
    if request.method == 'POST':
        texts = request.json 
        return jsonify({'success': True})
    elif request.method == 'GET':
        return jsonify(texts)
    else:
        return jsonify({'error': 'Method Not Allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)