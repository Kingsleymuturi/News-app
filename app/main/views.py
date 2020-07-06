from flask import render_template,redirect,request,url_for
from . import main
# from app import app
from ..news_requests import get_sources,get_articles,search_articles,articles_source

@main.route('/')
def HomePage():
    """
    Views thats renders news sources to the home page
    """
    general_news = get_sources("general")
    business_news = get_sources("business")
    sports_news = get_sources("sports")
    technology_news = get_sources("technology")
    entertainment_news = get_sources("entertainment")
    return render_template('sources.html',general=general_news,business=business_news,sports=sports_news,technology=technology_news,entertainment=entertainment_news)


@main.route('/articles/<id>')
def sourceArticles(id):
    all_articles = articles_source(id)
    print(all_articles)
    source = id
    return render_template('sourcearticles.html', articles = all_articles, source = source)


@main.route('/search/<keyword_name>')
def keyword(keyword_name):
    '''
    View function to display the search results
    '''
    keyword_name_list = keyword_name.split(" ")
    keyword_name_format = "+".join(keyword_name_list)
    searched_keyword = get_keyword(keyword_name_format)
    title = f'{keyword_name.title()}'
    display_keyword = keyword_name.upper()

    return render_template('search.html', keyword = searched_keyword, title = title, display_keyword=display_keyword )