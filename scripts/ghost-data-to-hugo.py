#!/usr/bin/env python

import json
import datetime
import os, os.path
_dir = os.path.dirname(os.path.abspath(__file__))

with open(_dir + '/../data/GhostData.json', 'rb') as data_file:
    ghost_data = json.load(data_file)

posts = ghost_data['db'][0]['data']['posts']

for post in posts:
    created_at = datetime.datetime.fromtimestamp(
        post['created_at']/1000).isoformat()
    title = post['title']
    meta_title = post['meta_title'] or ''
    meta_description = post['meta_description'] or ''
    slug = post['slug']
    markdown = post['markdown']
    #draft = 'false' if post['published_at'] else 'true'
    draft = 'true' if post['status']=='draft' else 'false'
    bDraft = draft=='true'
    bPage = bool(post['page'])
    published_at_ts = (
            post['published_at']/1000
        if post['published_at']
        else
            post['created_at']/1000
    )
    published_at_dt = (
        datetime.datetime.fromtimestamp(
            published_at_ts
        )
    )
    published_at = published_at_dt.isoformat()

    try:
        orig_published_at_ts = post['published_at']/1000
    except:
        orig_published_at_ts = False

    try:
        orig_created_at_ts   = post['created_at']/1000 or False
    except:
        orig_created_at_ts   = False

    try:
        orig_updated_at_ts   = post['updated_at']/1000 or False
    except:
        orig_updated_at_ts   = False

    file_time = orig_updated_at_ts if orig_updated_at_ts else published_at_ts

    if bPage:
        fileName = "content/%s.md" % slug
    else:
        if bDraft:
            fileName = "content/post/drafts/%s.md" % slug
        else:
            fileName = "content/post/%s.md" % slug

    with open(fileName, 'w') as post_file:
        post_file.write('+++\n')
        post_file.write('date = "%s"\n' %
                        published_at.encode('utf8'))
        if orig_created_at_ts:
            post_file.write('created_at = "%s"\n' % datetime.datetime.fromtimestamp(orig_created_at_ts).isoformat().encode('utf8'))
        if orig_published_at_ts:
            post_file.write('published_at = "%s"\n' % datetime.datetime.fromtimestamp(orig_published_at_ts).isoformat().encode('utf8'))
        if orig_updated_at_ts:
            post_file.write('updated_at = "%s"\n' % datetime.datetime.fromtimestamp(orig_updated_at_ts).isoformat().encode('utf8'))

        post_file.write('draft = "%s"\n' % draft.encode('utf8'))
        post_file.write('title = "%s"\n' % title.encode('utf8'))
        post_file.write('meta_title = "%s"\n' % meta_title.encode('utf8'))
        post_file.write('meta_description = "%s"\n' % meta_description.encode('utf8'))
        post_file.write('slug = "%s"\n' % slug.encode('utf8'))
        post_file.write('aliases = [ "/%s/" ]\n' % slug.encode('utf8'))
        post_file.write('author = "sebst"\n\n')
        post_file.write('+++\n\n')
        post_file.write(markdown.encode('utf8'))
    os.utime(fileName, (file_time, file_time))
