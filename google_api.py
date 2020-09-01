from googlesearch import search


def google_search(query):
    result = search(query, tld="com", num=5, start=0, stop=5, pause=1)
    response = []
    for j in result:
        response.append(j)
    return response
