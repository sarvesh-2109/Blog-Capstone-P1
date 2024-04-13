from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post = Post()


@app.route('/')
def home():
    return render_template("index.html", posts=post.response)


@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    return render_template("post.html",
                           title=post.blog_title(blog_id),
                           subtitle=post.blog_subtitle(blog_id),
                           body=post.blog_body(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
