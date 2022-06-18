from flask import Flask, render_template
from post import Post
import requests
from list_file import poke, new_onlyfiles

posts = requests.get("https://api.npoint.io/9113bc850b6da1d9b5c7").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
#     클래스 객체가 들어가 있는 리스트가 생성됨 (해당 클래스 객체는 4개의 속성을 가짐)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/seal/<int:index>')
def seal_make(index):
    start_index = index*25
    # 각페이지로 보내줄 리스트 슬라이싱
    onlyfiles = list(poke.keys())
    onlyfiles_slice = onlyfiles[start_index:start_index+25]
    new_onlyfiles_2 = new_onlyfiles[start_index:start_index+25]

    print(len(onlyfiles_slice))
    print(onlyfiles_slice)
    new_onlyfiles
    # 0~24 / 25~49
    return render_template("book_layout.html", onlyfiles_slice=onlyfiles_slice, poke=poke, new_onlyfiles_2=new_onlyfiles_2)


if __name__ == "__main__":
    app.run(debug=True)


