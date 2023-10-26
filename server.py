from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def cajas_1():
    return render_template('index.html', num=3, color='#0530ad')

@app.route('/play/<int:num>')
def cajas_2(num):
    return render_template('index.html', num=num, color = '#0530ad')

@app.route('/play/<int:num>/<string:color>')
def cajas_3(num, color):
    return render_template('index.html', num=num, color=color)
    
if __name__ == "__main__":
    app.run(debug=True)