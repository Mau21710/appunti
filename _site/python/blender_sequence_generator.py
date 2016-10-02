# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""



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








# ---------------------------------------------- End Steps - Summary

try:
    import bpy
except ImportError:
    print('No BPY')

import os.path


  

def z_whole_sequence_yoga(title='yoga1'):
    # initiate variables
    orig_dir =  "/home/maurizio/GitBook/Library/maoz75/gli-appunti/"
    img_dir = os.path.join(orig_dir, "figures/asana_yoga/")
    out_dir = "/tmp/av"
    # generation of tables
    adoc_file = os.path.join(orig_dir,'14_yoga.adoc')
    txt_commands="vajrasana 120, shashankasana 180, adho_mukha_svanasana 60, uttanasana 120, baddha_konasana 60, upavishta_konasana 120, janu_sirsasana 60x2, paschimottanasana 240, shavasana 60, halasana 30, sarvangasana 60, utthita_sarvangasana 60x2, karnapidasana 30, halasana 30, shavasana 30, supta_baddha_konasana 300, shavasana 300"
    images, descs, long_names, secs = generate_table(txt_commands, adoc_file)
    # generation of SRT file
    srt_file = os.path.join(out_dir, "{}.srt".format(title))
    f = open(srt_file, 'w')
    f.write(generate_srt_text(images, descs, secs))
    f.close()
    # inserting in blender images and sounds
    # generate doings
    snd_dir="/home/maurizio/Downloads/Audio/3h_relax.m4a"
    sounds_files=[]
    for i in range(len(secs)-1):
        sounds_files.append("chalk.wav")
    sounds_files.append("3h_relax.m4a")
    bpy.context.area.type = 'SEQUENCE_EDITOR'
    put_sounds_on_sequencer(sounds_files, snd_dir, secs)
    put_images_on_sequencer(images,img_dir,secs)
    # bpy.context.area.type = 'CONSOLE'
    
def z_whole_sequence_stretching(title='stretching_running'):
    # Step 1 
    body = """Corpo dell' ADOC"""
    img_dir = "/home/maurizio/GitBook/Library/maoz75/gli-appunti/figures/stretching/"
    seq = "arco_plantare 20x2, gambe_posteriore 20x2, popliteo 20x2, adduttori 20x2, quadricipiti 20x2, anche 20x2, base_tronco_e_glutei 20, dorso 20, collo 20, pettorali 20x2, spalle 20x2, braccia 20x2"
    # initiate variables
    orig_dir =  "/home/maurizio/GitBook/Library/maoz75/gli-appunti/"
    img_dir = os.path.join(orig_dir, "figures/stretching/")
    out_dir = "/tmp/av"
    # generation of tables
    adoc_file = os.path.join(orig_dir,'14_yoga.adoc')
    txt_commands="vajrasana 120, shashankasana 180, adho_mukha_svanasana 60, uttanasana 120, baddha_konasana 60, upavishta_konasana 120, janu_sirsasana 60x2, paschimottanasana 240, shavasana 60, halasana 30, sarvangasana 60, utthita_sarvangasana 60x2, karnapidasana 30, halasana 30, shavasana 30, supta_baddha_konasana 300, shavasana 300"
    images, descs, long_names, secs = generate_table(txt_commands, adoc_file)
    
    # generation of SRT file
    srt_file = os.path.join(out_dir, "{}.srt".format(title))
    f = open(srt_file, 'w')
    f.write(generate_srt_text(images, descs, secs))
    f.close()
    # inserting in blender images and sounds
    # generate doings
    snd_dir="/home/maurizio/Downloads/Audio/"
    sounds_files=[]
    for i in range(len(secs)-1):
        sounds_files.append("chalk.wav")
    sounds_files.append("3h_relax.m4a")
    bpy.context.area.type = 'SEQUENCE_EDITOR'
    put_sounds_on_sequencer(sounds_files, snd_dir, secs)
    put_images_on_sequencer(images,img_dir,secs)
    # bpy.context.area.type = 'CONSOLE'
    


    out_video_file = os.path.join(out_dir, "{}.flv".format(title))
    audio = "/home/maurizio/Downloads/Audio/3h_relax.m4a"
    pass
                    
    
"""
sounds_files = ['chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav', 'chalk.wav','3h_relax.m4a']
secs = [120, 180, 60, 120, 60, 120, 60, 60, 240, 60, 30, 60, 60, 60, 30, 30, 30, 300, 300, 0]
"""
    
    
    

# ---------------------------------------------- Bibliography

def reload():
    """
    import sys
    sys.path.append("/home/maurizio/GitBook/Library/maoz75/gli-appunti/python")
    import blender_tests
    import importlib
    importlib.reload(blender_tests)
    """
    pass
    
def load_sequence(list_of_files):
    list_of_files_for_planes=[]
    for l in list_of_files:
        list_of_files_for_planes.append({'name':l})
    return list_of_files_for_planes

def insert_text(name='Text01', text='Text'):
    myFontCurve = bpy.data.curves.new(type="FONT",name="myFontCurve")
    myFontOb = bpy.data.objects.new(name,myFontCurve)
    myFontOb.data.body = text
    bpy.context.scene.objects.link(myFontOb)
    bpy.context.scene.update()    

def select_camera():    
    bpy.ops.object.select_pattern(pattern="Camera")
    
def select_selection():
    return bpy.context.selected_objects

def set_camera_down(camera):
    camera.location[0] = 0
    camera.location[1] = 0
    camera.location[2] = 2
    camera.rotation_euler[0] = 0
    camera.rotation_euler[1] = 0
    camera.rotation_euler[2] = 0

def some_uts():
    help(bpy.data.objects)
    list(bpy.data.objects) #lists data objects present in blender file.
    bpy.data.objects['Camera'].location[0] = 0
    Blender.Scene.GetCurrent().getChildren() # This returns all objects from the current scene.
    Blender.Object.GetSelected() # which returns selected objects on visible layers in the current scene.


def load_all_in_blender():
    base_dir="/home/maurizio/GitBook/Library/maoz75/gli-appunti/figures/asana_yoga/"
    sequenza = load_sequence(get_yoga_files(base_dir))
    bpy.ops.import_image.to_plane(files=sequenza,
        directory=base_dir, 
        filter_image=True, filter_movie=True, filter_glob="", force_reload=True, 
        use_shadeless=True, use_transparency=True, transparency_method='Z_TRANSPARENCY', alpha_mode='PREMUL', 
        relative=False)
    set_camera_down()
    
def load_image_list_in_blender(image_list=['vajrasana', 'shashankasana', 'adho_mukha_svanasana', 'uttanasana', 'baddha_konasana', 'upavishta_konasana', 'janu_sirsasana', 'janu_sirsasana', 'paschimottanasana', 'shavasana', 'halasana', 'sarvangasana', 'utthita_sarvangasana', 'utthita_sarvangasana', 'karnapidasana', 'halasana', 'shavasana', 'supta_baddha_konasana', 'shavasana'],
    base_dir="/home/maurizio/GitBook/Library/maoz75/gli-appunti/figures/asana_yoga/"):
    filelist=[]
    for img in image_list:
        filelist.append({'name':"{}.jpg".format(img)})
    print(filelist)
    bpy.ops.import_image.to_plane(files=filelist,
        directory=base_dir, 
        filter_image=True, filter_movie=True, filter_glob="", size_mode='ABSOLUTE', 
        relative=False)
        #filter_image=True, filter_movie=True, filter_glob="", force_reload=True, 
        #use_shadeless=False, use_transparency=True, transparency_method='Z_TRANSPARENCY', alpha_mode='PREMUL', 
        #relative=False)    
    filelist=[{"name":"adduttori.png"}]
    base_dir="/home/maurizio/GitBook/Library/maoz75/gli-appunti/figures/stretching/"
    img1 = bpy.ops.import_image.to_plane(files=filelist,
        directory=base_dir, 
        filter_image=True, filter_movie=True, filter_glob="", size_mode='ABSOLUTE', 
        relative=False)


#secs = [120, 180, 60, 120, 60, 120, 60, 60, 240, 60, 30, 60, 60, 60, 30, 30, 30, 300, 300]
def create_timeline(secs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    transition_time = 1,
                    fps=24,
                    translation_x=-1.77):
    # Standstill for transition_time frames
    time_index = transition_time * fps
    timing_scenes = [time_index]
    bpy.context.scene.frame_current = time_index
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
    #bpy.ops.anim.keyframe_insert_menu(type='__ACTIVE__', confirm_success=True)
    for scene in range(len(secs)):
        # Set keyframe on end scene
        time_index += secs[scene] * fps
        bpy.context.scene.frame_current = time_index
        bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
        # Set keyframe on end transition
        time_index += transition_time * fps
        timing_scenes.append(time_index)
        bpy.context.scene.frame_current = time_index
        bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
        bpy.ops.transform.translate(value=(translation_x, 0, 0)) 
    bpy.context.scene.frame_end = time_index
    # bpy.context.scene.file_format = 'H264'
    bpy.context.scene.render.filepath = "/tmp/temp4.avi"
    bpy.context.scene.render.resolution_x = 640
    bpy.context.scene.render.resolution_y = 360
    

def right_sequence():
    #blender_tests.set_camera_down(bpy.data.objects['Camera'])
    set_camera_down(bpy.data.objects['Camera'])
    # blender_tests.set_camera_down(bpy.data.objects['Lamp'])
    bpy.data.objects['Camera'].select=True
    # bpy.data.objects['Lamp'].select=True    
    #blender_tests.load_image_list_in_blender()
    load_image_list_in_blender()
    create_timeline()

    
