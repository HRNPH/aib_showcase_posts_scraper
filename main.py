from facebook_scraper import get_posts
import pandas as pd
from tqdm import tqdm
import re

cookies = './cookies.json'
if cookies:
    spliter = '-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-'
else:
    spliter = '--------------------------------'

# create dummy dataframe
dataframe = pd.DataFrame(columns=['title', 'ID', 'summary', 'title_image', 'images', 'links', 'reason', 'author', 'fulltext', 'post_url'])
# loop through posts in ai builders facebook page
counter = 0
for post in get_posts('aibuildersx', pages=60, cookies=cookies): # specify more page for more posts
    post_data = {'title': None, 'summary': None, 'ID': None, 'title_image': None, 'images': None, 'links': None, 'reason': None, 'fulltext': None, 'author': None, 'post_url': None}
    
    post_data['title'] =  [False]
    try:
        full_textsplit = post['text'].split('\n')
        post_data['title'] = full_textsplit[0]

    except:
        post_data['title'] =  [False]

    if '#AIBuilders' in post_data['title']:
        print('----------------------------')
        print('Post found: ', post['post_url'])
        counter += 1 # we'll do early stop if we got all posts
        # identify each section of post data
        post_data['ID'] = post_data['title'].split('#')[2].split('-')[0].strip(' ')
        # post_data['title'] = post_data['title'].split('-')[-1]
        post_data['title'] = full_textsplit[0].replace(f'#AIBuilders Showcase Series #{post_data["ID"]} -', '')
        # print(post_data['title'])
        # print(post_data['ID'])
        post_data['fulltext'] = post['text']
        post_data['title_image'] = post['image']
        post_data['images'] = post['images']
        post_data['post_url'] = post['post_url']
        # section spltting
        section_split = post['text'].split(spliter) # if there is a problem take a look at spliter (using cookies make scraped data different)
        post_data['summary'] = section_split[0].split('\n')[1:]
        # print(post['text'])
        post_data['links'] = section_split[1]
        # get author from first line of section 3
        section3 = section_split[2].split('\n')
        post_data['author'] = section3[1].split('-')[-1]
        post_data['reason'] = section3[2:]
        # connect to dataframe to be exported as csv
        # dataframe = dataframe.append(post_data, ignore_index=True)
        # concat
        dataframe = pd.concat([dataframe, pd.DataFrame([post_data])], ignore_index=True)
        # report
        print('Post ', post_data['ID'], ' found.', post_data['title'])
        # early stop
        if counter == 65:
            print('Early stopping.')
            break

print('Reportedly: ', len(dataframe), ' posts found.')
# export to csv
print('Exporting to CSV...')
dataframe.to_csv('showcase_data.csv', index=False)  