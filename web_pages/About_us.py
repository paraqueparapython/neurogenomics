import json


# MEET THE TEAM
title1 = "Meet the team &#128522"


def get_data(file):
    """
    Load data from json with 4_team member information
    :param file: file path
    :return: names, roles, image paths and bios from al 4_team members
    """
    with open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
    names = [value['name'] for k1, value in data.items()]
    roles = [value['role'] for k2, value in data.items()]
    photos = [value['photo'] for k3, value in data.items()]
    bios = [value['bio'] for k4, value in data.items()]
    return names, roles, photos, bios


def team_member(photo, name, role, bio):
    """
    Load data from one member of the 4_team and place all in
    a container with image in the left side and text next to it.
    :param photo: path to member image
    :param name: string containing the name of the member
    :param role: string containing the role of the member
    :param bio: string containing the brief bio of the member
    :return: All the data in a html format
    """
    member = """
    <div class="container">
        <div class="image-left">
            <img src= {}  
            alt="Member"
            width="150"
            class="image1">
            <div>
                <h5 style = "text-align: left; font-family: Montserrat, sans-serif; color: black;"> {} ({}) </h5>
                <div style = "text-align: justify; font-family: Montserrat, sans-serif; color: black;"> {} </div>
            </div>
        </div>
    </div>
        """.format(photo, name, role, bio)
    return member


# OUTSIDE THE LAB

title3 = 'Outside the lab &#128526'

gallery = """           
   <div class=column1>
        <img src="http://drive.google.com/uc?export=view&id=1kpkgrKcEZNfcABaT2zBtglu91bq5Zv77" class="image">   
   </div>
   <div class=column1>
        <div class=img>
            <img src="http://drive.google.com/uc?export=view&id=1Ihg_CIOh-adSFgSt9eYHOqcf37qWMBAm" class="image">
        </div>
   </div>    
   <div class=column2>
        <img src="http://drive.google.com/uc?export=view&id=1qkDUw15DDWH4PKlGsKb_tm9ZYtLXSmuu" class="image">
    </div>
   """