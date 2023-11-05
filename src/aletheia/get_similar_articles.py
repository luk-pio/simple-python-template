from langchain.document_loaders import BraveSearchLoader

from aletheia.get_article import get_article_content

api_key = "BSAt2nmuC57jmjrGEY9-JNAyAHTU6Z5"

def get_urls_on_topic(topic, count=3):
    docs = search(topic, count=count)
    urls = [doc.metadata["link"] for doc in docs]
    print("Got urls for topic: " + topic + " : " + str(urls))
    return urls

def get_articles_from_urls(urls):
    articles = get_article_content(urls)
    return articles

def get_articles_on_topic(topic, count=3):
    return get_articles_from_urls(get_urls_on_topic(topic, count=count))

def search(topic, count=3):
    loader = BraveSearchLoader(
        query=topic, api_key=api_key, search_kwargs={"count": count}
    )
    return loader.load()

if __name__ == "__main__":
    print(get_articles_from_urls(get_urls_on_topic("hamas and isreal conflict")))