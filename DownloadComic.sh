python create_json_file.py
scrapy crawl comic -o ListComic.json --nolog
scrapy crawl chapter -o ListImages.json --nolog
python download_comic.py
