from newspaper import Article


def filter_url(url):
    filter_url_list = ['wsj.com', 'aljazeera.com', 'bbc.co.uk', 'techcrunch.com', 'nytimes.com', 'bloomberg.com',
                       'businessinsider.com',
                       'cbc.ca', 'cnbc.com', 'cnn.com', 'ew.com', 'espn.go.com', 'espncricinfo.com', 'foxnews.com',
                       'apnews.com',
                       'news.nationalgeographic.com', 'nymag.com', 'reuters.com', 'rte.ie', 'thehindu.com',
                       'huffingtonpost.com',
                       'irishtimes.com', 'timesofindia.indiatimes.com', 'washingtonpost.com', 'time.com',
                       'medicalnewstoday.com',
                       'ndtv.com', 'theguardian.com', 'dailymail.co.uk', 'firstpost.com', 'thejournal.ie',
                       'hindustantimes.com',
                       'economist.com', 'news.vice.com', 'usatoday.com', 'telegraph.co.uk', 'metro.co.uk',
                       'mirror.co.uk', 'news.google.com']

    for link in filter_url_list:
        url_matched = link in url

        if url_matched:
            return True
        else:
            continue

    return False


def get_story(item):
    story = {
        'title': item.title,
        'link': item.link,
        'published': item.published,

    }

    return story


def get_article(newsitem):
    try:
        page = Article(newsitem["link"])
        page.download()
        page.parse()
        return True, str(page.text)

    ##To Do.. We may get 403 error while getting the actual article.. this is just a placeholder to return "InvalidArticle"
    except Exception:
        return False, ""
