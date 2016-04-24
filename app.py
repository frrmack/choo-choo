from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def choochoo():
    return render_template('choochoo.html')


@app.route('/video/<vidname>')
def video_player(vidname):
    return render_template('video_player.html',
                           vidname=vidname)


if __name__ == '__main__':
    app.debug=True
    app.run()
