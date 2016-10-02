# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""

import sys
this_path = '/home/maurizio/GitBook/Library/mau21710/gli-appunti/python/' # path 
sys.path.append(this_path)

import os.path
import subprocess
from funAsciidoc import generate_simple_table
try: #first pass
    from funTTS import create_mp3
except ImportError:
    print ('ImportError for create_mp3')
try: #second pass
    #from funBlender import create_scene
    from funBlender import put_images_on_sequencer
    from funBlender import put_sounds_on_sequencer
    from funBlender import set_movie_setting
    pass
except ImportError:
    print ('ImportError for create_scene and put_images_on_sequencer')




def _first_pass():
    title = 'Yoga, sequenza relax'
    txt_commands = "vajrasana 120, shashankasana 180, adho_mukha_svanasana 60, uttanasana 120, baddha_konasana 60, upavishta_konasana 120, janu_sirsasana 60x2, paschimottanasana 240, shavasana 60, halasana 30, sarvangasana 60, utthita_sarvangasana 60x2, karnapidasana 30, halasana 30, shavasana 30, supta_baddha_konasana 300, shavasana 300"
    base_path = '/home/maurizio/GitBook/Library/mau21710/gli-appunti' # path 
    orig_imgs="figures/asana_yoga"
    ext=".svg"
    dest_ext=".jpg"
    out_dir = "/tmp/aaa"
    start_sound="/home/maurizio/Mao/Progetti/Suoni/gesso.mp3"
    background_music="/home/maurizio/Downloads/Audio/relax-ben.mp3"
    orig_svg_dir = os.path.join(base_path,"figures")
    lista_titoli = ['head_titles.svg', 'tail_titles.svg']
    lista_titoli_png = ['head_titles.png', 'tail_titles.png']
    dest_img_format = '1280x720'
    absolute_orig_images = os.path.join(base_path,orig_imgs)
    if not os.path.exists(out_dir):
        subprocess.call(['mkdir', out_dir])  
    # --------------------------------------------------------------------------- Genero Tabelle
    images, descs, secs, adoc_table = generate_simple_table(title, txt_commands, orig_imgs, ext)
    # ---------------------------------------------------------------------------- File Audio    
    mp3_files = []
    tmp = os.path.join(out_dir,'tmp.mp3')
    for i in range(len(descs)):
        mp3_name=os.path.join(out_dir, "{:03d}_{}.mp3".format(i,images[i]))
        mp3_files.append(mp3_name)
        if not os.path.exists(mp3_name): #If already made no need to do it again!
            create_mp3(descs[i],mp3_name)
            subprocess.call(['sox', start_sound, mp3_name, tmp])
            subprocess.call(['mv', tmp, mp3_name])
    mp3_files.append(start_sound)
    mp3_files.append(start_sound)
    mp3_files.append(background_music)
    # ----------------------------------- Generazione lista files grafici
    imagefile_names = [lista_titoli_png[0]]
    for i in images:
        imagefile_names.append("{}{}".format(i,ext))
    imagefile_names.append(lista_titoli_png[1])
    secs_full = [15]
    secs_full.extend(secs)
    secs_full.append(15)
    #-------------------------------------- genero i trunk video
    converted_images=[]
    for img in imagefile_names:
        new_name = os.path.join(out_dir,os.path.basename(img)).replace(ext, dest_ext)
        if not os.path.exists(new_name):
            subprocess.call(['convert','+antialias', '-density', '1000',
                                 os.path.join(absolute_orig_images,img), 
                                 '-resize', dest_img_format, 
                                 '-background', 'white', '-gravity', 'center', 
                                 '-extent', dest_img_format, 
                                 new_name])
        converted_images.append(new_name)
        #'-transparent-color', 'white', '-flatten' , '-scale',         
    # ------------------------------ Generazione Header e Footer
    duration = 0
    for s in secs_full:
        duration += s
    duration = int(duration/60)
    lista_sostituzioni = [
        ['esteso', 'sequenza yoga rilassante'],
        #['mau21710', 'nome autore'],
        ['fitness', 'yoga'],
        ['Durata: 0 min', 'Durata: {} min'.format(duration)],
        ['titolo_sequenza', 'un pò di relax'],
        ['thanks for watching!', 'grazie per l\'attenzione'],
        ]
    for l in lista_titoli:
        orig = os.path.join(orig_svg_dir, l)
        dest = os.path.join(out_dir,l)
        dest_png = os.path.join(out_dir,lista_titoli_png[lista_titoli.index(l)])
        if not os.path.exists(dest_png): #If already made no need to do it again!
            subprocess.call(['cp', orig, dest])
            f = open(dest,'r')
            all_svg=f.read()
            f.close()
            for l in lista_sostituzioni:
                all_svg = all_svg.replace(l[0],l[1])
            f = open(dest,'w')
            f.write(all_svg)
            f.close()    
            subprocess.call(['convert', '-scale', dest_img_format, dest, dest_png])
    print("converted_images = {}".format(converted_images))
    print("secs_full = {}".format(secs_full))
    print("mp3_files = {}".format(mp3_files))
    #put_images_on_sequencer(converted_images,"",secs_full)
    #put_sounds_on_sequencer(mp3_files,"",secs_full)
    

def _second_pass():

    converted_images = ['/tmp/aaa/head_titles.png', '/tmp/aaa/vajrasana.jpg', '/tmp/aaa/shashankasana.jpg', '/tmp/aaa/adho_mukha_svanasana.jpg', '/tmp/aaa/uttanasana.jpg', '/tmp/aaa/baddha_konasana.jpg', '/tmp/aaa/upavishta_konasana.jpg', '/tmp/aaa/janu_sirsasana.jpg', '/tmp/aaa/janu_sirsasana.jpg', '/tmp/aaa/paschimottanasana.jpg', '/tmp/aaa/shavasana.jpg', '/tmp/aaa/halasana.jpg', '/tmp/aaa/sarvangasana.jpg', '/tmp/aaa/utthita_sarvangasana.jpg', '/tmp/aaa/utthita_sarvangasana.jpg', '/tmp/aaa/karnapidasana.jpg', '/tmp/aaa/halasana.jpg', '/tmp/aaa/shavasana.jpg', '/tmp/aaa/supta_baddha_konasana.jpg', '/tmp/aaa/shavasana.jpg', '/tmp/aaa/tail_titles.png']
    secs_full = [15, 120, 180, 60, 120, 60, 120, 60, 60, 240, 60, 30, 60, 60, 60, 30, 30, 30, 300, 300, 15]
    mp3_files = ['/tmp/aaa/000_vajrasana.mp3', '/tmp/aaa/001_shashankasana.mp3', '/tmp/aaa/002_adho_mukha_svanasana.mp3', '/tmp/aaa/003_uttanasana.mp3', '/tmp/aaa/004_baddha_konasana.mp3', '/tmp/aaa/005_upavishta_konasana.mp3', '/tmp/aaa/006_janu_sirsasana.mp3', '/tmp/aaa/007_janu_sirsasana.mp3', '/tmp/aaa/008_paschimottanasana.mp3', '/tmp/aaa/009_shavasana.mp3', '/tmp/aaa/010_halasana.mp3', '/tmp/aaa/011_sarvangasana.mp3', '/tmp/aaa/012_utthita_sarvangasana.mp3', '/tmp/aaa/013_utthita_sarvangasana.mp3', '/tmp/aaa/014_karnapidasana.mp3', '/tmp/aaa/015_halasana.mp3', '/tmp/aaa/016_shavasana.mp3', '/tmp/aaa/017_supta_baddha_konasana.mp3', '/tmp/aaa/018_shavasana.mp3', '/home/maurizio/Mao/Progetti/Suoni/gesso.mp3', '/home/maurizio/Mao/Progetti/Suoni/gesso.mp3', '/home/maurizio/Downloads/Audio/relax-ben.mp3']
    put_images_on_sequencer(converted_images,"",secs_full,2)
    put_sounds_on_sequencer(mp3_files,"",secs_full,2)
    set_movie_setting('~/Videos/test.avi')


if __name__ == "__main__":
     # _first_pass() # primo passaggio
     _second_pass()  
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


