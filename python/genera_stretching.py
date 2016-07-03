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
try:
    from funTTS import create_mp3
except ImportError:
    print ('ImportError for create_mp3')
try:
    #from funBlender import create_scene
    from funBlender import put_images_on_sequencer
    from funBlender import put_sounds_on_sequencer
    pass
except ImportError:
    print ('ImportError for create_scene and put_images_on_sequencer')




def _tested():
    title = 'Stretching'
    txt_commands = "arco_plantare 20x2, gambe_posteriore 20x2, popliteo 20x2, adduttori 20x2, quadricipiti 20x2, anche 20x2, base_tronco_e_glutei 20, dorso 20, collo 20, pettorali 20x2, spalle 20x2, braccia 20x2"
    base_path = '/home/maurizio/GitBook/Library/mau21710/gli-appunti' # path 
    orig_imgs="figures/stretching/"
    ext=".png"
    dest_ext=".jpg"
    out_dir = "/tmp/aaa"
    start_sound="/home/maurizio/Mao/Progetti/Suoni/gesso.mp3"
    background_music="/home/maurizio/Downloads/Audio/relax-ben.mp3"
    orig_svg_dir = os.path.join(base_path,"figures")
    lista_titoli = ['head_titles.svg', 'tail_titles.svg']
    lista_titoli_png = ['head_titles.png', 'tail_titles.png']
    dest_img_format = '960x720'
    lista_sostituzioni = [
        ['esteso', 'stretching post corsa'],
        #['mau21710', 'nome autore'],
        ['fitness', 'stretching'],
        ['Durata: 0 min', 'Durata: 30 min'],
        ['titolo_sequenza', 'Post Running'],
        ['thanks for watching!', 'grazie per l\'attenzione'],
        ]
    absolute_orig_images = os.path.join(base_path,orig_imgs)
    if not os.path.exists(out_dir):
        subprocess.call(['mkdir', out_dir])  
    # ------------------------------ Generazione Header e Footer
    for l in lista_titoli:
        orig = os.path.join(orig_svg_dir, l)
        dest = os.path.join(out_dir,l)
        dest_png = os.path.join(absolute_orig_images,lista_titoli_png[lista_titoli.index(l)])
        if not os.path.exists(dest_png): #If already made no need to do it again!
            subprocess.call(['cp', orig, dest])
            f = open(dest,'r')
            all_svg=f.read()
            f.close()
            for l in lista_sostituzioni:
                all_svg = all_svg.replace(l[0],l[1])
            f = open(dest,'w')
            all_svg=f.write(all_svg)
            f.close()    
            subprocess.call(['convert', '-scale', dest_img_format, dest, dest_png])
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
    secs_full = [10]
    secs_full.extend(secs)
    secs_full.append(10)
    #-------------------------------------- genero i trunk video
    converted_images=[]
    for img in imagefile_names:
        new_name = os.path.join(out_dir,os.path.basename(img)).replace(ext, dest_ext)
        if not os.path.exists(new_name):
            subprocess.call(['convert', '-transparent-color', 'white', 
                                 '-flatten' , '-scale', 
                                 dest_img_format, os.path.join(absolute_orig_images,img), 
                                 new_name])
        converted_images.append(new_name)
    put_images_on_sequencer(converted_images,"",secs_full)
    put_sounds_on_sequencer(mp3_files,"",secs_full)
    

if __name__ == "__main__":
    _tested()
    pass
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


