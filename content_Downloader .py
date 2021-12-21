import requests
import pytube

url_img = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fxakep.ru%2F2021%2F03%2F10%2Fcodeby-python-for-ethical' \
          '-hacking%2F&psig=AOvVaw3QLRCfjRQZOEnNKXc0Xf0x&ust=1640164374941000&source=images&cd=vfe&ved' \
          '=0CAsQjRxqFwoTCLDi3cvG9PQCFQAAAAAdAAAAABAD '

url_video = 'https://youtu.be/x7X9w_GIm1s'


def download_img(url=''):
    """Скачивает изображение через url"""
    try:
        response = requests.get(url=url)
        with open("req_img.jpg", "wb") as file:
            file.write(response.content)
        return "IMG Successfully Downloaded."
    except ValueError:
        return "Error. Check the URL!!!"


def download_video(url=''):
    """Скачивает Видео YouTube через url"""
    try:
        yt = pytube.YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        return "Video Successfully Downloaded."
    except ValueError:
        return "Error. Check the URL!!!"


def main():
    print(download_img(url=url_img))
    print(download_video(url=url_video))


if __name__ == '__main__':
    main()
