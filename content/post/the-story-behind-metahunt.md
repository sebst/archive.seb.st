+++
date = "2015-07-13T15:54:22"
created_at = "2015-04-26T18:09:25"
published_at = "2015-07-13T15:54:22"
updated_at = "2015-07-13T22:11:05"
draft = "false"
title = "The Story Behind metahunt.co"
meta_title = ""
meta_description = ""
slug = "the-story-behind-metahunt"
aliases = [ "/the-story-behind-metahunt/" ]
author = "sebst"

+++

ProductHunt, BetaList, TechCrunch, Hacker News, Reddit and other sites all have a huge impact on the traction a startup or a bootstrapped micro service might gain at the very beginning.

I was looking for some metrics of how successfull startups will become after they have been featured on those sites. So I played around with ProductHunt, CrunchBase and Angellist APIs to get some insights into the data.

One of my first ideas included a small site where you could track the performance of products featured one year ago on ProductHunt. When I was testing the prototype of this site - which I named "[metahunt.co](http://metahunt.co)", I used dates from around the year's beginning for testing around. 

What a coincidence I stumbled upon [ProductHop](http://www.producthop.com/) (featured on PH on Jan, 2, 2015) which is, basically, the same thing I intended to create. While ProductHop did not leverage other APIs to track performance, I felt like my idea of metahunt was too close to that to get some traction in the ProductHunt community which - of course - I identified as the possibly most interested group for my project.

My first intention was to create "metahunt/jobs - Land your dream job at a company featured on ProductHunt" instead. Guess what: Of course, PH implemented a job board on [their own](http://www.producthunt.com/jobs). (Bottom line: Companies have a lack of skilled people - Build education startups instead of job boards because job boards won't fix excess demand for qualified work force! That's nothing for a weekend project, though.)

To build something useful, I decided to create a bigger project, although this would exceed my weekend. And I came up with "metahunt: time machine, statistics and jobs". 

Meanwhile, Marc Köhlbrugge from [Betalist](http://betalist.com/) sent me an access code to their private API, so I could integrate more seed data than just those from ProductHunt. I was eager to see what happened.

And if that wasn't enough, I needed to re-apply for the CrunchBase API since they rolled out a new version of their API...

I began ro realize that metahunt.co became bigger than I thought.

So, I added most of the features I was thinking of in seperate places and recapped my initial idea of getting some metrics out of the API. I investigeted a bit and made [metahunt.co/stats](http://metahunt.co/stats) the place that holds the most interesting numbers.

So, mission accomplished? I played around with some APIs, did a bit stats p0rn and let it go?

No, there was another thing I wanted to learn from developing the project: The *social dynamics* of the ProductHunt community. Metahunt was my first submission to ProductHunt which I am affiliated  with. 

The first thing I already knew from looking at the API: There are **lots** of submissions to Product Hunt. So how to set apart?

### Twitter

ProductHunt has this nice little Tweet-Button and is not known to devaluate upvotes with an external referrer - in contrast to Hacker News. So, I decided to use the share button and put some money in it to promote this tweet with Twitter Ads. Primary audience: People who follow @producthunt. That created some buzz and resulted in some 5-ish upvotes. Metahunt did not make it to the front page of course.

### Personal

Since metahunt is a project which should flatter the PH community (as it puts PH to its center), I started to ping out some people with a high impact on the community (http://www.producthunt.com/about). [That](https://twitter.com/sebastiansteins/status/596281989206044672) worked out ! Bram put it to the front page (thanks again!)

### Slack

I stumbled upon a [directory of slack communities](http://chats.directory/) a few days earlier, so that I decided to gain some feedback from startup related groups.
I adapted the site from the feedback. Among other things, I created a newsletter signup button with [sumome](http://sumome.com/) just to test the willingness to sign up to a newsletter run by a hobbyist. As of today, there are 20 signups, which is noteworthy, because the newsletter itself was not advertised on the page anywhere, only the signup box appears from time to time (randomly).

### Stats, again 

The first days of metahunt (May, 7 till May, 10) resulted in a bit more than 2,000 visitors.

![the first 96 hours in Google analytics](/content/images/2015/07/metahuntstats.png)

| 1,643 | May, 07, 2015 |
|   355 | May, 08, 2015 |
|    90 | May, 09, 2015 |
|    80 | May, 10, 2015 |


### Conclusion

Metahunt itself got [126 upvotes on Product Hunt](http://metahunt.co/hunt/meta-hunt/) so far, which is not enough to make it to one of the [leaderboards](http://metahunt.co/leaderboard). However, metahunt was a successful weekend project. A weekend full of fun, a few adaptions in the week afterwards and a Product Hunt front page placement attraction 2,000 people does not sound that bad. 

Given that startups might create more useful products than metahunt, it turns out that a first traction is relatively easy to achieve with the help of the great startup community on Twitter, ProductHunt and Slack. The challenge, as always, is to wrap up with your projects, a task which metahunt somehow failed at, but is somewhat out of scope for a weekend project on the other side.