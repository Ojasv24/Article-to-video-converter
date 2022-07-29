from google_images_download import google_images_download


def download_image(keywords):

    keywords = ''.join(e for e in keywords if e.isalnum() or e == " ").strip()

    response = google_images_download.googleimagesdownload()

    arguments = {"keywords": keywords, "limit": 1}

    absolute_image_paths = response.download(arguments)
  
    return list(absolute_image_paths[0].values())[0][0]
