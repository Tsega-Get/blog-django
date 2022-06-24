from xml.dom.minidom import Identified
from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Grace-get",
        "date": date(2022,6,24),
        "title":"Mountain Hiking",
        "excerpt":"There's nothing like the views you get when hiking in the Mountains!",
        "content":"""
            Hiking is the preferred term in Canada and the United States; 
            the term walking is used in these regions for shorter, particularly urban walks. 
            In the United Kingdom and the Republic of Ireland, the word walking describes 
            all forms of walking, whether it is a walk in the park or backpacking in the Alps.
            
           The word hiking is also often used in the UK, along with rambling (a slightly old-fashioned term), 
           hillwalking, and fell walking (a term mostly used for hillwalking in.
           
        The term bushwalking is endemic to Australia, having been adopted by the Sydney 
        Bush Walkers club in 1927.
        Hiking is a long, vigorous walk, usually on trails or footpaths in the countryside.
        Walking for pleasure developed in Europe during the eighteenth century.[1] Religious
        pilgrimages have existed much longer but they involve walking long distances for a spiritual
        purpose associated with specific religions.
 
        """
    },
    {
        "slug": "Programmin-is-fun",
        "image":"programming.jpg",
        "author":"Grace-get",
        "date": date(2022,6,23),
        "title":"Programming Is Great",
        "excerpt":"Programming is the process of creating a set of instructions that tell a computer how to perform a task.",
        "content":"""
           Computer programming is the process of performing a particular computation (or more generally, accomplishing a specific computing result), usually by designing and building an executable computer program. Programming involves tasks such as analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms (usually in a chosen programming language, commonly referred to as coding).
 
        """
    },
    {
        "slug": "into-the-woods",
        "image":"woods.jpg",
        "author":"Tsegazeab",
        "date": date(2022,6,21),
        "title":"Nature At Its Best",
        "excerpt":"Nature is amazing! The amount of inspiration I get when walking in nature is great",
        "content":"""
           Over recent years there has been an increasing recognition of the benefits 
           that humans gain from contact with trees and nature. Modern society has 
           changed its relationship with nature. In the space of a single generation
           children’s play has moved from outdoors to indoors, the iconic backyard has shrunk,
           parents have become increasingly anxious about children’s safety, working hours and
           stress levels have risen and technology (especially screens) has encroached into almost
           all areas of life.
           
           Just dig into “Can’t Get Out” or “Fell So Hard” and it’s easy to spot the affable hooks 
           and fuzzed-out bass and third-eye winks and fun harmonies that Woods have produced reliably
           since way back ‘round 2004 (which, in the buzz-buzz world of psych-pop really is a grand
           achievement, too). But listen carefully, also, to the sound of our (and their) world in transition,
           the ambient humming of spring peepers behind “Where Do You Go When You Dream.”
        """
    },
]
def get_date(post):
    return post['date']
    
# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
       "posts":latest_posts 
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_detail(request, slug):
    identified_posts = next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html", {
        "post" : identified_posts
    })