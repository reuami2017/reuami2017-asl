import urllib.request

def get_file(filename):
    """
    gets the mp3 at that location and stores it in the proper folder
    :param filename:
    :return:
    """
    url = "https://ssl.gstatic.com/dictionary/static/sounds/de/0/" + filename + ".mp3"
    localname = "sound/" +  filename + ".mp3"
    urllib.request.urlretrieve(url, localname)

get_file("cat")
