from flask import Flask, render_template, request
from crawler import crawl_website

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        keyword = request.form.get("keyword")

        results = crawl_website(url, keyword)
        return render_template("results.html", results=results, url=url, keyword=keyword)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
