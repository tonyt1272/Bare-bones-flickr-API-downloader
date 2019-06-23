from Space.space import *   #My own little utility package
import flickr_api as Flickr
import requests
import json

#https://www.flickr.com/services/api/explore/flickr.photos.search# to get url, or use methods

api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
secret = 'xxxxxxxxxxxxxxxx'

Flickr.set_keys(api_key,secret)

url = ''

response = requests.get(url)
data = response.json()
photos = data['photos']['photo']

print(len(photos))
print(json.dumps(photos[0], indent=4, sort_keys=True))


photo=photos[0]
pic_id = photo['id']
pic = Flickr.Photo(id=pic_id)
pSizes = pic.getSizes()
print('\n')
print(json.dumps(pSizes, indent=4, sort_keys=True))
#print(pSizes['Site MP4']['url'])

print('\t\tid\t\t\t\t','owner\t\t\t','title')
count=0
for photo in photos:
    ext = str(count)
    count+=1
    print(str(count)+':  ',photo['id'],photo['owner'],photo['title'])
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