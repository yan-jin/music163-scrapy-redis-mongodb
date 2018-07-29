from scrapy_redis.spiders import RedisSpider
from scrapy import Request
from scrapy import FormRequest
from music163.settings import DEFAULT_REQUEST_HEADERS
import json
from music163.items import Music163Item
import logging
import logging.handlers


class Music163(RedisSpider):
    name = 'music163'
    allow_domains = ['163.com']
    base_url = 'http://music.163.com'
    ids = ['1001', '1002', '1003',
           '2001', '2002', '2003',
           '6001', '6002', '6003',
           '7001', '7002', '7003',
           '4001', '4002', '4003']
    initials = [i for i in range(65, 91)]
    initials.append(0)

    def __init__(self):
        logger_1 = logging.getLogger('scrapy.core.engine')
        f_handler_1 = logging.handlers.TimedRotatingFileHandler('./music163_debug.log', when='H', interval=1,
                                                                backupCount=0)
        f_handler_1.setLevel(logging.DEBUG)
        f_handler_1.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s'))
        logger_1.setLevel(logging.DEBUG)
        logger_1.addHandler(f_handler_1)

        logger_2 = logging.getLogger('scrapy.core.scraper')
        f_handler_2 = logging.handlers.TimedRotatingFileHandler('./music163_debug.log', when='H', interval=1,
                                                                backupCount=0)
        f_handler_2.setLevel(logging.DEBUG)
        f_handler_2.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s'))
        logger_2.setLevel(logging.DEBUG)
        logger_2.addHandler(f_handler_2)

    def start_requests(self):
        for id_ in self.ids:
            for initial in self.initials:
                url = '{0}/discover/artist/cat?id={1}&initial={2}'.format(self.base_url, id_, initial)
                yield Request(url, callback=self.parse_index)

    def parse_index(self, response):
        artists = response.xpath('//*[@id="m-artist-box"]/li/div/a/@href').extract()
        for artist in artists:
            artist_url = self.base_url + '/artist' + '/album?' + artist[8:]
            yield Request(artist_url, callback=self.parse_all_album_indexs)

    def parse_all_album_indexs(self, response):
        indexs = response.xpath('//*[@class="u-page"]/a/@href').extract()[:-2]
        for index in indexs:
            index_url = self.base_url + index
            yield Request(index_url, callback=self.parse_artist)

    # 获得某一页所有专辑的url
    def parse_artist(self, response):
        albums = response.xpath('//*[@id="m-song-module"]/li/div/a[@class="msk"]/@href').extract()
        for album in albums:
            album_url = self.base_url + album
            yield Request(album_url, callback=self.parse_album)

    def parse_album(self, response):
        musics = response.xpath('//ul[@class="f-hide"]/li/a/@href').extract()
        for music in musics:
            music_id = music[9:]
            music_url = self.base_url + music

            yield Request(music_url, meta={'id': music_id}, callback=self.parse_music)

    # 获得音乐信息
    def parse_music(self, response):
        music_id = response.meta['id']
        music = response.xpath('//div[@class="tit"]/em[@class="f-ff2"]/text()').extract_first()
        artist = response.xpath('//div[@class="cnt"]/p[1]/span/a/text()').extract_first()
        album = response.xpath('//div[@class="cnt"]/p[2]/a/text()').extract_first()
        '''
        data = {
            'csrf_token': '',
            'params': '5TGiujjtp8lkQcvyK1A7tAFHQ1AEC0/14UA56blnxJPDhSzbxwikmF087LR+Ac3HHbiyN6OLCBM5zVLm9j+ITt/z4Q8TfaNEbMg9xfhJo2TcGi3dmStbmG1YevievexXKzT2yt304OejB3AF4Xm00LtLCa5KRAq8Epn3n4ZenHucIvYR2lABYk/En4JxJOsE',
            'encSecKey': '4792833bf7cfbbbd0415252c219da1d7537d43bd075b9878cb0751739ce12d7913c612fd96b1aa850ed82746b693226f578c3eb99773514404f31a08a708d86d1309c0150ba8bf650f303bff9dfc852f147835fa48532957b06d9c96b8f8cfc26214cc3dc4e8e4482a51dae9461db5ab0546fc01bec30a13a93b5bbd7280145f'
        }
        DEFAULT_REQUEST_HEADERS['Referer'] = self.base_url + '/playlist?id=' + str(music_id)
        music_comment = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(music_id)
        '''

        item = Music163Item()
        item['music_id'] = music_id
        item['artist'] = artist
        item['album'] = album
        item['music'] = music
        yield item
        '''
        yield FormRequest(music_comment, meta={'id': music_id, 'music': music, 'artist': artist, 'album': album},
                          callback=self.parse_comment, formdata=data)

    def parse_comment(self, response):
        music_id = response.meta['id']
        music = response.meta['music']
        artist = response.meta['artist']
        album = response.meta['album']
        result = json.loads(response.text)
        comments = []
        if 'hotComments' in result.keys():
            for comment in result.get('hotComments'):
                hotcomment_author = comment['user']['nickname']
                hotcomment = comment['content']
                hotcomment_like = comment['likedCount']
                # 这里我们将评论的作者头像也保存，如果大家喜欢这个项目，我后面可以做个web端的展现
                hotcomment_avatar = comment['user']['avatarUrl']
                data = {
                    'nickname': hotcomment_author,
                    'content': hotcomment,
                    'likedcount': hotcomment_like,
                    'avatarurl': hotcomment_avatar
                }
                comments.append(data)
        else:
            comments.append('This song has no hot comments')
        item = Music163Item()
        item['music_id'] = music_id
        item['artist'] = artist
        item['album'] = album
        item['music'] = music
        item['comments'] = comments
        yield item
        '''
