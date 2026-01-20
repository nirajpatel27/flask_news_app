from flask import Flask, render_template, request
from services.news_service import get_top_headlines, search_news

app = Flask(__name__)

@app.route("/")
def home():
    page = request.args.get("page", 1, type=int)
    category = request.args.get("category")
    query = request.args.get("q")

    if query:
        articles, total_results = search_news(query=query, page=page)
    else:
        articles, total_results = get_top_headlines(
            category=category,
            page=page
        )

    return render_template(
        "home.html",
        articles=articles,
        page=page,
        total_results=total_results,
        category=category,
        query=query
    )

if __name__ == "__main__":
    app.run(debug=True)
