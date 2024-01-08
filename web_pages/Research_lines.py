import json
# RESEARCH
title_research = 'Research lines&#128300'


# Research lines
def get_intro(file_path):
    with open(file_path, encoding='utf8') as f:
        intro = f.read()
    return intro


def get_research_data(file):
    with open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
    titles = [value['title'] for k1, value in data.items()]
    descriptions = [value['description'] for k2, value in data.items()]
    return titles, descriptions


def research_line(title, description):
    r_line = """
         <div>
             <h6 style = "text-align: justify; font-size:20px; font-family: Montserrat, sans-serif;"> {} </h6>
             <div style = "text-align: justify; font-family: Montserrat, sans-serif;"> {} </div>
         </div>
    """.format(title, description)
    return r_line


# FUNDING AGENCIES
title_fundings = 'Funding agencies &#128176'


def _get_funding_agencies(file):
    with open(file, 'r', encoding='utf8') as f:
        funding_agencies = json.load(f)
    return funding_agencies


def funding_agencies_logo(file):
    imgs = _get_funding_agencies(file)

    funding_agencies = """
       <div class="container">            
           <div class="row">
             <div class="column">
               <img src="{}" 
               width="150" height="130">
             </div>
             <div class="column">
               <img src="{}" 
               width="150" height="130">
             </div>
             <div class="column">
               <img src="{}" 
               width="150" height="130">
             </div>
             <div class="column">
               <img src="{}" 
               width="150" height="130"> 
             </div>
           </div>
           <br/>
           <div class="row">
             <div class="column1">
               <img src="{}" 
               width="200" height="60">
             </div>
             <div class="column1">
               <img src="{}" 
               width="200" height="70">
             </div>
             <div class="column1">
               <img src="{}" 
               width="200" height="60">
             </div>
           </div>
       </div>
       """.format(imgs['INDRE'],
                  imgs['laCaixa'],
                  imgs['AGAUR'],
                  imgs['MariaMaeztu'],
                  imgs['LaMarato'],
                  imgs['LeJeune'],
                  imgs['MICINN'])
    return funding_agencies
