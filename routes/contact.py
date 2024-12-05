from app import app, render_template


@app.route('/contactus')
def contactus():  # put application's code here
    return render_template('Contactus.html')
