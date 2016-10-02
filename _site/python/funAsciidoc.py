# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""




"""
def get_yoga_files(base_dir="/home/maurizio/GitBook/Library/maoz75/gli-appunti/figures/asana_yoga/",
                   extension = '.png'):
    raw_list_of_files = os.listdir(base_dir)
    list_of_files = []
    for l in raw_list_of_files :
        if l.find(extension)>-1:
            list_of_files.append(l)
    return list_of_files
"""


# ---------------------------------------------- Step 1 Extraction of the sequence
def generate_table(txt_commands="vajrasana 120, shashankasana 180, adho_mukha_svanasana 60, uttanasana 120, baddha_konasana 60, upavishta_konasana 120, janu_sirsasana 60x2, paschimottanasana 240, shavasana 60, halasana 30, sarvangasana 60, utthita_sarvangasana 60x2, karnapidasana 30, halasana 30, shavasana 30, supta_baddha_konasana 300, shavasana 300", 
                   orig_adoc='/home/maurizio/GitBook/Library/maoz75/gli-appunti/14_yoga.adoc'):
    f=open(orig_adoc)
    orig_adoc = f.read()
    f.close()
    listed_table = txt_commands.split(', ')
    adoc_table = """.Tabella
    [header=yes, cols="^1,2,1"]
    |===
    | Posizione | Descrizione | Secondi
    """
    images=[]
    secs=[]
    descs=[]
    long_names=[]
    for elem in listed_table:
        image, sec = elem.split(' ')
        desc = find_description(orig_adoc,image.replace('_', ' '))
        long_name = find_long_name(orig_adoc,image.replace('_', ' '))
        pos_x = sec.find('x') # -1 not found
        times = 0 
        if pos_x > -1:
            times = int(sec[pos_x+1:])
            sec = sec[0:pos_x]
        images.append(image)
        descs.append(desc)
        secs.append(int(sec))
        long_names.append(long_name)
        adoc_table += "| image:figures/asana_yoga/{}.svg[role=right, pdfwidth=5cm] | {} | {} \n".format(image, desc, sec)
        for i in range(times-1):
            adoc_table += "| image:figures/asana_yoga/{}.svg[role=right, pdfwidth=5cm] | altro lato | {} \n".format(image, sec)
            images.append(image)
            descs.append('Cambia Lato')
            long_names.append('Cambia')
            secs.append(int(sec))
    adoc_table += "|===\n"
    print(adoc_table)
    return images, descs, long_names, secs


def generate_simple_table(title = 'Stretching',
                txt_commands="arco_plantare 20x2, gambe_posteriore 20x2, popliteo 20x2, adduttori 20x2, quadricipiti 20x2, anche 20x2, base_tronco_e_glutei 20, dorso 20, collo 20, pettorali 20x2, spalle 20x2, braccia 20x2", 
                orig_imgs="figures/stretching",
                ext=".png"):
    """
    return 
        images     list of image files
        descs      list of descs
        secs       list of scene times
        adoc_table txt for asciidoc table    
    """
    listed_table = txt_commands.split(', ')
    adoc_table = ".{} footnote:[{}]\n[header=yes, cols=\"^1,2,1\"]\n|===\n| Posizione | Descrizione | Secondi".format(
        title, txt_commands)
    images=[]
    secs=[]
    descs=[]
    for elem in listed_table:
        image, sec = elem.split(' ')
        desc = image.replace('_', ' ')
        pos_x = sec.find('x') # -1 not found
        times = 0 
        if pos_x > -1:
            times = int(sec[pos_x+1:])
            sec = sec[0:pos_x]
        images.append(image)
        descs.append(desc)
        secs.append(int(sec))
        adoc_table += "| image:{}/{}{}[role=right, pdfwidth=5cm] | {} | {} \n".format(orig_imgs, image, ext, desc, sec)
        for i in range(times-1):
            adoc_table += "| image:{}/{}{}[role=right, pdfwidth=5cm] | altro lato | {} \n".format(orig_imgs, image, ext, sec)
            images.append(image)
            descs.append('Cambia Lato')
            secs.append(int(sec))
    adoc_table += "|===\n"
    print(adoc_table)
    return images, descs, secs, adoc_table


def find_description(body,title, start='_Esecuzione_: ', end=' +'):
    find_section(body, title, start, end)


def find_long_name(body,title,start='_Sinonimi_: _((', end='))'):
    find_section(body, title, start, end)


def find_section(body,title, start='_Esecuzione_: ', end=' +'):
    """ returns body[pos_start:pos_end]
    """
    pos = body.find(title)
    if pos >-1:
        pos_start = body.find(start,pos) + len(start)
        pos_end = body.find(end, pos_start)
        return body[pos_start:pos_end]
    else:
        return "ciccia"


# ---------------------------------------------- Step 2 Creation of SRT File
def generate_srt_text(images, descs, secs, transition=1):
    """
    A numeric counter identifying each sequential subtitle
    The time  (00:00:00,000) that the subtitle should appear on the screen, followed by --> and the time it should disappear
    Subtitle text itself on one or more lines
    A blank line containing no text, indicating the end of this subtitle[9]
    """
    srt_text = ""
    act_time = transition
    for i in range (len(images)):        
        srt_text+="{:02d}\n00:{:02d}:{:02d},000-->00:{:02d}:{:02d},000\n{}: {}\n\n".format(
            i+1, 
            int(act_time/60), act_time%60, 
            int((act_time+secs[i])/60), (act_time+secs[i])%60, 
            images[i], descs[i])
        act_time+=secs[i]
    return srt_text



