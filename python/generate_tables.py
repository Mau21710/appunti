# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""

import subprocess
import os.path
import funTTS


def create_minivideo(image_file, time_in_secs, video_file):
    subprocess.call(['avconv','-loop', '1', 
                    '-i' ,image_file, 
                    '-t', '{}s'.format(time_in_secs), 
                    '-c:v', 'libx264', '-preset', 'ultrafast', '-tune', 'film', '-s', '1280x720', '-c:a', 'copy', 
                    video_file])


def create_video(images, secs, out_dir, out_video_file):
    video_index = 0 
    for scene in range(len(secs)):
        outfile = os.path.join(out_dir,'vid{:02d}.mkv'.format(video_index))
        video_index += 1
        create_minivideo(images[scene], secs[scene],outfile )
    
    

def find_description(body,title):
    pos = body.find(title)
    if pos >-1:
        esec = '_Esecuzione_: '
        start = body.find(esec,pos) + len(esec)
        end = body.find(' +', start)
        #print pos, start, end, body[start:end]
        return body[start:end]
    else:
        return "ciccia"

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
    for elem in listed_table:
        image, sec = elem.split(' ')
        desc = find_description(orig_adoc,image.replace('_', ' '))
        pos_x = sec.find('x') # -1 not found
        times = 0 
        if pos_x > -1:
            times = int(sec[pos_x+1:])
            sec = sec[0:pos_x]
        images.append(image)
        descs.append(desc)
        secs.append(int(sec))
        adoc_table += "| image:figures/asana_yoga/{}.svg[role=right, pdfwidth=5cm] | {} | {} \n".format(image, desc, sec)
        for i in range(times-1):
            adoc_table += "| image:figures/asana_yoga/{}.svg[role=right, pdfwidth=5cm] | altro lato | {} \n".format(image, sec)
            images.append(image)
            descs.append('Cambia Lato')
            secs.append(int(sec))
    adoc_table += "|===\n"
    return images, descs, secs
    

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

titolo = 'yoga1'
orig_dir =  '/home/maurizio/GitBook/Library/maoz75/gli-appunti/'
adoc_file = os.path.join(orig_dir,'14_yoga.adoc')
img_dir = os.path.join(orig_dir, 'figures/asana_yoga/')
out_dir = "/tmp/av"
srt_file = os.path.join(out_dir, "{}.srt".format(titolo))
out_video_file = os.path.join(out_dir, "{}.flv".format(titolo))



images, descs, secs = generate_table()

# generation of SRT file
f = open(srt_file, 'w')
f.write(generate_srt_text(images, descs, secs))
f.close()

images_files = []
convert_file = lambda x: os.path.join(img_dir,'{}.jpg'.format(x))
for img in images:
    images_files.append(convert_file(img))
print(images_files)

create_video(images_files, secs, out_dir, out_video_file)

"""
/home/maurizio/SW/ffmpeg/ffmpeg -f concat -i <(for f in ./*.mkv; do echo "file '$PWD/$f'"; done) -c copy output.mkv
"""




        


