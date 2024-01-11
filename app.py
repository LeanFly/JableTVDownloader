


from download import download
from movies import movieLinks


if __name__ == "__main__":
    links = movieLinks()
    
    for link in links:
        download(link)
