# Automated Gender Analysis of New Yorker Bylines

## Introduction

This is an automated analysis of how bylines in *The New Yorker* break down by gender. From this (fairly rough estimate) it looks like about 1/3 of articles (and fiction stories. and poems.) are written by women and 2/3 by men. This ratio is pretty consistent from the 1920s to the present (though data from the magazine's earlier years is sparse).

## Methodology and caveats

#### Acquiring bylines

`fetch_new_yorker_bylines.py` scrapes the bylines of pieces of writing published in **the print magazine** edition of *The New Yorker* (not articles that have only been published online). It finds them on table of contents pages like
```
http://www.newyorker.com/magazine/reporting/page/12
```
In addition to `reporting`, which covers most non-fiction from the magazine, the script also scrapes the `shouts-murmurs` (Shouts & Murmurs, a humor feature), `fiction`, `poems`, `critics`, and `talk-of-the-town` (short, reported essays) sections.

`reporting`, `talk-of-the-town`, and `critics` seem to have pretty complete data back to 2007, with a few older pieces also listed. `shouts-murmurs` seems complete back to 1992, the start of the feature's modern incarnation; there are also 202 bylines from Alexander Woollcott, the writer of [the original Shouts & Murmurs column](http://www.newyorker.com/books/double-take/the-original-shouts-murmurs), in the 1920s and 1930s. The listings for `fiction` and `poems` seem to be complete all the way back to magazine's inception in 1925 (!) with over 12,000 bylines for each section.

#### Gender Detection

[As Dan put it](https://github.com/compciv/gendered-pulitzer-board/blob/master/README.md), the gender detection uses a “dirt-cheap super naive and ethnocentric algorithm developed in the [babynames-gender-detector homework](http://www.compciv.org/assignments/exercise-sets/0020-gender-detector-set).” Basically, it tries to match up the first name of each byline with baby name records from the Social Security Administration and categorizes each byline as male or female or unclassified, depending on whether the name appeared more for boys or girls in the baby name dataset (unclassified if it didn't appear at all).

I am not super confident in this classifier's accuracy (many names are used for many genders). Also, I'd like to acknowledge that it's a bit sad/backward that our government records people with this gender binary—but there are still insights to be found within this structure.

## Past research and articles

I'll steal [Dan's citation that points out that women tend to get far fewer bylines on newspaper front pages than men](http://www.womensmediacenter.com/pages/the-problem).

I also think [Who Writes for the New York Times?](http://www.whowritesfor.com/), which I found via our course website, is quite enlightening: it gives a rough, day-by-day gender breakdown of *New York Times* bylines.

[Inequitable representation](http://publiceditor.blogs.nytimes.com/2014/05/12/still-talking-about-it-where-are-the-women/) of women in journalism is fairly [well-documented](http://niemanreports.org/articles/where-are-the-women/), though I didn't find anything about representation in magazines in particular.

*The New Yorker* (increasingly?) has a reputation of as relatively progressive publication, and most of my favorite *New Yorker* writers are women. Nevertheless …

## How to use it

#### Downloading

You can't easily `git clone` this project since it's a subfolder of a larger git repo. But amazingly this works:
```
svn export https://github.com/alecglassford/compciv
-2016/trunk/projects/gender-detector-data
```

#### Dependencies

You need Python 3. The external packages `requests` and `beautifulsoup4` are needed for webscraping. `matplotlib` is needed for graphs, but the code should (??) run without the graphing part if you don't have it. I think this should take care of everything:
```
pip install requests beautifulsoup4 matplotlib
```

#### Running the thing

If you run, `python run.py`, it should do everything. Just sit back and watch (until you get to the analyze stage). To clarify, that script just runs the follow scripts:

* `fetch_gender_data.py` downloads and unzips the Social Security administration baby names data into `tempdata/gender/`.

* `wrangle_gender_data.py` counts the baby names over all the available years and labels names as male or female accordingly; this is all saved in `tempdata/gender/wrangledbabynames.csv`

* `fetch_new_yorker_bylines.py` scrapes `newyorker.com` as described above. This takes a **long** time. Maybe an hour? There was one point when I got an HTTP error, and I thought I was maybe being blocked for bombarding the server, but then I redownloaded everything later and it worked fine. If necessary, you can edit `settings.py` to download one, or a few, sections at a time. All the raw HTML from the table of contents pages for each section is concatenated and stored in `tempdata/sections/`.

* `wrangle_new_yorker_bylines.py` finds author names and dates of publication in the downloaded files and stores them neatly in CSVs in`tempdata/wrangled_sections/`

* `classify.py` classifies each byline as male, female, or unclassified with the methodology described above. The augmented CSVs are stored in `tempdata/classified_sections/`

* `analyze.py` gives a command line interface that lets you explore different facets of the data: You can filter by a particular section (or look at all the sections at once), you can choose how far back in time you want to look, and you can adjust the granularity of the data (per 5-year interval, per year, per month, or per issue of the magazine). It prints a table with gender data and produces a stacked graph if you have `matplotlib`.

After you have run `run.py` (or all the scripts sequentially) once, you should just use `analyze.py` to explore different facets of the data. It's fast!

## Analysis

First, we can look at all the sections by month from 2007 to the present (the period for which we have most complete data):

![Figure 1][figure_1]

```
Fraction of New Yorker bylines from 2007-01 to 2016-03
(for ['reporting', 'talk-of-the-town', 'shouts-murmurs', 'critics', 'fiction', 'poems'])
------------------------------------------
Date           Female  Male    Unclass.Total
------------------------------------------
2007-01        15      43      1       59
               (25%)   (73%)   (2%)    

2007-02        17      38      1       56
               (30%)   (68%)   (2%)    

2007-03        28      52      1       81
               (35%)   (64%)   (1%)    

2007-04        30      58      3       91
               (33%)   (64%)   (3%)    
```
…
```
2016-01        24      43      1       68
               (35%)   (63%)   (1%)    

2016-02        22      45      6       73
               (30%)   (62%)   (8%)    

2016-03        20      32      1       53
               (38%)   (60%)   (2%)    

------------------------------------------
Overall: (33%) female, (64%) male, (3%) unclassified
```

We can see that about 1/3 of bylines are classified as female, and 2/3 are classified as male. Bummer. But maybe this is a huge improvement over the even less equitable olden days? Here's year by year from the start of the dataset:

![Figure 2][figure_2]

In fact, it looks like the percentage of *New Yorker* articles written by women hasn't changed that much since the magazine was founded in 1925. Of course, this graph should be taken with a boulder of salt: since the graph is of percentages, it's not obvious from it that the data from earlier years is much more sparse than from recent years (e.g. 217 total entries from 1970 compared to 1040 from 2012), and most of the earlier data is from fiction and poetry; the little bit of reporting from 20th century is that which has been hand-chosen for indexing on *The New Yorker*'s website. Nevertheless, it's interesting to see that the peak of female representation (at least when we weight fiction and poetry heavily) was in 1988 (44% of bylines)—and that it actually seemed to dip after that, during the editorship of Tina Brown, the magazine's first female editor, from 1992-1998.

Which section of *The New Yorker* has the highest female representation? Well, here is the Critics section from 2007 to the present:
![Figure 3][figure_3]
Its bylines are 39% female. Unfortunately, avid *New Yorker* readers may realize that 143 of these bylines belong to [Sasha Frere-Jones](http://www.newyorker.com/contributors/sasha-frere-jones), whom the classifier misclassifies as female. Without those bylines, the proportion is closer to 35%.

#### Conclusion

It looks like we have a lot of work to do if we want to see gender equity in the journalistic/literary world—and I hope we really do. In the future, I'd love to repeat this analysis on the *New Yorker*'s granular (and sometimes absurdly specific) "departments" (e.g. Profiles, Annals of Technology, A Reproter at Large, Onward and Upward with the Arts, Letter for Chicago), as well as articles published solely online. I'm curious how the gender breakdown differs between these different subdomains.

[figure_1]: graphs/figure_1.png "Figure 1"
[figure_2]: graphs/figure_2.png "Figure 2"
[figure_3]: graphs/figure_3.png "Figure 3"
