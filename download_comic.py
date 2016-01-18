import json
import urllib
import os
# from unicodedata import normalize

print "Finished crawling images"

with open("ListImages.json") as images_file:
    try:
        chapters = json.load(images_file)
    except ValueError:
        chapters = []

for chapter in chapters:
    comic_folder = chapter['name']
    if not os.path.exists(comic_folder):
        original_umask = os.umask(0)
        os.makedirs(comic_folder, 0777)

    chapter_folder = ("%s/%s") % (comic_folder, chapter['chap'])
    if not os.path.exists(chapter_folder):
        original_umask = os.umask(0)
        os.makedirs(chapter_folder, 0777)
    images = chapter['images']
    i_image = 1
    print "Downloading %s with %s picture" % (chapter['chap'], len(images))
    print len(images)
    for image in images:
        filename = ("%s/%s.jpg") % (chapter_folder, i_image)
        with open(filename, "wb") as f:
            f.write(urllib.urlopen(str(image)).read())
        i_image += 1
