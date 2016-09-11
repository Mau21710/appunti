# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""

import os
import time
try:
    import bpy, bpy.data, bpy.ops #, bpy.props, bpy.types, bpy.context, bpy.utils, bgl, blf, mathutils
except ImportError:
    print ('not imported bpy')
    pass

"""
import sys
sys.path.append("/home/maurizio/GitBook/Library/maoz75/gli-appunti/python")
import blender_tests
import importlib
importlib.reload(blender_tests)
"""

def get_yoga_files(base_dir="/home/maurizio/GitBook/Library/maoz75/gli-appunti/figures/asana_yoga/"):
    raw_list_of_files = os.listdir(base_dir)
    list_of_files = []
    for l in raw_list_of_files :
        if l.find('.jpg')>-1:
            list_of_files.append(l)
    return list_of_files
    
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
    
def put_images_on_sequencer(images, folder, secs):
    bpy.context.area.type = 'SEQUENCE_EDITOR'
    start=1
    fps=24
    for i in range(len(images)):
        stop=fps*secs[i]
        bpy.ops.sequencer.image_strip_add(
            directory=folder, files=[{"name":images[i]}], 
            relative_path=True, show_multiview=False, frame_start=1, frame_end=24, channel=i%10)


def right_sequence():
    #blender_tests.set_camera_down(bpy.data.objects['Camera'])
    set_camera_down(bpy.data.objects['Camera'])
    # blender_tests.set_camera_down(bpy.data.objects['Lamp'])
    bpy.data.objects['Camera'].select=True
    # bpy.data.objects['Lamp'].select=True    
    #blender_tests.load_image_list_in_blender()
    load_image_list_in_blender()
    create_timeline()


images=['vajrasana', 'shashankasana', 'adho_mukha_svanasana', 'uttanasana', 'baddha_konasana', 'upavishta_konasana', 'janu_sirsasana', 'janu_sirsasana', 'paschimottanasana', 'shavasana', 'halasana', 'sarvangasana', 'utthita_sarvangasana', 'utthita_sarvangasana', 'karnapidasana', 'halasana', 'shavasana', 'supta_baddha_konasana', 'shavasana']  

    
