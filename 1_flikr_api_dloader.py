from Space.space import *   #My own little utility package
import flickr_api as Flickr
import requests
import json

#https://www.flickr.com/services/api/explore/flickr.photos.search# or use methods
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
secret = 'xxxxxxxxxxxxxxxx'

Flickr.set_keys(api_key,secret)

url = ''
response = requests.get(url)
print(type(response))
print(response)
lprint(type(response.json()))#1

data = response.json()

photos = data['photos']['photo']

print('id\t\t\t\t','owner\t\t','title')
lprint(len(photos))#2

lprint(json.dumps(photos[0], indent=4, sort_keys=True))
photo=photos[0]
pic_id = photo['id']
pic = Flickr.Photo(id=pic_id)
pSizes = pic.getSizes()
lprint(json.dumps(pSizes, indent=4, sort_keys=True))
#lprint(pSizes['Site MP4']['url'])
count=0
for photo in photos:
    ext = str(count)
    count+=1
    print(count,photo['id'],photo['owner'],photo['title'])
    pic_id = photo['id']
    pic = Flickr.Photo(id=pic_id)
    pSizes = pic.getSizes()
    #print(pSizes['Site MP4']['url'])#####################
    if "Large" in pSizes:
        try:
            pic.save(data_path('chihuahuas\\chihuahua{}'.format(ext)), size_label="Large")  #Data path is from my own
                                                                                        #utilities library Space.space
                                                                                        #it points to my data folder
            print('Large jpg Sucess!!!!!')
        except:

            pass
    elif "Medium" in pSizes:
        try:
            pic.save(data_path('chihuahuas\\chihuahua{}'.format(ext)), size_label="Medium")  #
            print('Medium jpg Sucess!!!!!')
        except:

            pass
    else:
        print('FAIL!!!!!')
        continue