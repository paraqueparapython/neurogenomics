# import streamlit as st
import json

title = 'FUNCTIONAL NEURODEVELOPMENT AND GENOMICS LAB'


# Read data from file
def get_data(file):
    with open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


# Header
def intro(photo, text1, text2):
    """
    Load data from one member of the 4_team and place all in
    a container with image in the left side and text next to it.
    :param photo: path to member image
    :param text: text to write
    :return: All the data in a html format
    """
    introduction = """
        <div class="image-left">
            <img src= {}  
            alt="organoid"
            width="195"
            class=image1>
            <div style = "text-align: justify; font-family: Montserrat, sans-serif;"> {}{} </div>
        </div>
        """.format(photo, text1, text2)
    return introduction


# Brain organoids image gallery
title2 = 'Brain organoids'


def get_gallery(file):
    with open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
    images = [value for key, value in data.items()]
    gallery = """
    <div class="container"> 
        <div class="row">
         <div class=column>
                <video class ="video" autoplay loop>
                 <source src="{}" type="video/mp4"></video>
           </div>           
           <div class=column>
                <img src={} class="image">   
           </div>  
           <div class=column>
                <img src={} class="image">
            </div>
        </div>
        <br/>
        <div class="row"> 
             <div class=column>
                <img src={} class="image">   
           </div>
           <div class=column>
                <div class=img>
                    <img src={} class="image">
                </div>
           </div>    
           <div class=column>
                <video class ="video" autoplay loop>
                 <source src="{}" type="video/mp4"></video>
           </div>
        </div>
        <br/>
    </div>
    """.format(images[0], images[1],
               images[2], images[3],
               images[4], images[5])

    return gallery


# INSTITUTIONS
title3 = "Institutions"


# Institutions images
def _get_institutions(file):
    with open(file, 'r', encoding='utf8') as f:
        institutions = json.load(f)
    return institutions


def institutions_logo(file):
    imgs = _get_institutions(file)

    institutions = """
       <div class="container">            
           <div class="row">
             <div class="column1">
               <img src="{}" 
               width="200" height="100">
             </div>
             <div class="column1">
               <img src="{}" 
               width="200" height="100">
             </div>
             <div class="column1">
               <img src="{}" 
               width="200" height="100">
             </div>
           </div>
       </div>
       """.format(imgs['institut_neurociencies'],
                  imgs['ub'],
                  imgs['idibell'])
    return institutions


# Latest news
title4 = 'Latest news'


def _get_news(file):
    with open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
    news = [value for key, value in data.items()]
    return news


def latest_news(file):
    news = _get_news(file)
    string = "<ul>\n"
    for s in news:
        string += "<li>" + str(s) + "</li><br/>"
    string += "</ul>"
    return string
