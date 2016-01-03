+++
date = "2016-01-03T13:37:00"
draft = "false"
title = "Moved to Hugo"
slug = "hello-hugo"
author = "sebst"
+++

**Hello, Hugo!**

Welcome to my blog. Things did not change that much, did they?

Well, actually, they did: I moved from Ghost to [Hugo](https://gohugo.io/). Hugo
is one of [many static site builders](https://staticsitegenerators.net/).

I started blogging around 2006 on WordPress, stopped it, and [came back]({{< ref "post/hello-world.md" >}}) to blogging
with Ghost in late 2014.

Eventually, I feel now really free. WordPress in the early days was a handy tool for bloggers in 2006-ish and became a
powerful tool for literally any use case you can imagine for a website. Basically, that's why Ghost was developed and
the developers kept their promise of delivering a handy tool for just bloggers. Bloggers – not real-estate agents,
news publishers or e-commerce retailers. Just bloggers.

However, for me that was software built upon an additional layer (as Ghost runs on node.js) with it's own dependencies,
database structures and so on. And as it is a dynamic site generator, this additional software running on my servers and thus,
opens a security sensitive intrusion vector to the machine.

Some things even annoyed me when working with Ghost. One thing is that the login does not work well together with the
Chrome password manager I use a lot. Another thing is that there is no good way for me to organize drafts. I am not saying that
this does not work in Ghost, it just does not work very well for me.

Now, I am on static pages. I left the ".html" extension and it annoys me that Hugo calls that "uglyURLs". Whats ugly in saying
where your roots are? ;-)

Anyway, I feel really interoperable right now. I chose the structure in which I store files (aka posts) and could easily parse
them with a few lines of scripting code if I ever wanted to switch to another engine in the future. (Compare and contrast: To move
my blog to Hugo I first had to update my customized Ghost installation to generate my "GhostData.json".)

I am even faster in extending my blog. For example if I wanted anything to happen when I added a blog post, I can now easily hook
on the files created instead of bothering with database scheme invented elsewhere or the API of a specific software.

Migrating to Hugo finally taught me that vendor-lockins can exist even if the products are open source.

If you want to move to a static site generator, you might find useful:

- [Blogging via iPhone](http://evanbrown.io/post/hugo-on-the-go/) - the dependency on static files on my laptop first prevented  me from considering static site generators an option, but does not anymore. Git, Travis and a loosely coupled toolset changed my mind.
- [Ghost to Hugo](http://caveconfessions.com/ghost-to-hugo/) - Converting your ghost installation to Hugo. Also have a look at [Migration](https://gohugo.io/tools/) section in the Hugo docs.
- [Rango](https://github.com/stayradiated/rango) - if you cannot live without a web interface.
