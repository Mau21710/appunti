# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""
try:
    import bpy
except ImportError:
    print ('ImportError for bpy')

# ---------------------------------------------- Step 3 Get Images list
def create_scene(name="Scena_A"):
    bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 4), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.context.object.name = "Camera_A"    
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(0, 0, 4), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.context.object.name = "Punto_Luce_A"
    bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.context.object.name = "Piano_A"
    bpy.ops.transform.resize(value=(1.81885, 1.81885, 1.81885), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    # bpy.context.space_data.context = 'MATERIAL'
    bpy.data.objects['Piano_A'].material.new()
    bpy.context.object.active_material.specular_intensity = 0.1
    bpy.context.object.active_material.diffuse_intensity = 0.9
    # bpy.context.space_data.context = 'MATERIAL'
    bpy.context.object.name = "immagine"


    
def put_images_on_sequencer(images, folder, secs, fps=24):
    bpy.context.area.type = 'SEQUENCE_EDITOR'
    start= 1
    for i in range(len(images)):
        stop= start + (fps*secs[i]) # - fps #-fps is to generate overlaps
        print(images[i])
        print(folder)
        bpy.ops.sequencer.image_strip_add(
            directory=folder, files=[{"name":images[i]}], 
            relative_path=True, show_multiview=False, frame_start=start, frame_end=stop, channel=int((i%3)+1))
        start = stop + 1 #- fps
    

def put_sounds_on_sequencer(sounds, folder, secs, fps=24):
    try:
        start= 1
        bpy.ops.sequencer.sound_strip_add(filepath=folder, 
                                          files=[{"name":sounds[-1]}], 
                                          relative_path=True, frame_start=start, channel=4)
        # ToDo bpy.ops.sequencer.cut(frame=47474, type='SOFT', side='RIGHT')
        for i in range(len(secs)):
            start += (fps*secs[i]) + 1
            bpy.ops.sequencer.sound_strip_add(filepath=folder, 
                                              files=[{"name":sounds[i]}], 
                                              relative_path=True, frame_start=start, channel=int((i%3)+6))
    except:
        print("OOOPS!")


def put_texts_on_sequencer(texts, secs):
    try: # non vaaaaaaaaaa!
        start= 1
        fps=24
        for i in range(len(texts)):
            stop= start + (fps*secs[i]) # - fps #-fps is to generate overlaps
            print(texts[i])
            bpy.ops.sequencer.effect_strip_add(filepath="/tmp/aaa/text.txt", frame_start=1, frame_end=10000, channel=11, type='TEXT')
            start = stop + 1 #- fps
    except:
        print("OOOPS! text on sequencer")
        

def set_movie_setting(filename = '/tmp/video_99.avi'):
    bpy.ops.sequencer.select(extend=False, linked_handle=False, left_right='NONE', linked_time=False)
    bpy.context.scene.render.filepath = "/home/maurizio/Videos/test.avi"
    bpy.context.scene.file_format = 'XVID'
    bpy.context.scene.format = 'XVID'
    bpy.context.scene.audio_codec = 'AAC'
    bpy.context.scene.audio_codec = 'MP3'
    bpy.context.scene.audio_bitrate = 192
    bpy.context.scene.use_audio_scrub = True
    bpy.context.scene.use_audio_sync = True
    bpy.context.scene.use_frame_drop = True
    bpy.context.scene.render.resolution_x = 1280
    bpy.context.scene.render.resolution_y = 720
    bpy.context.scene.render.resolution_percentage = 100
    bpy.context.scene.render.pixel_aspect_x = 1
    bpy.context.scene.render.pixel_aspect_y = 1
    bpy.context.scene.render.fps = 2
    bpy.context.scene.render.fps_base = 1
    bpy.context.scene.render.use_antialiasing = False
    bpy.context.scene.render.use_textures = False
    bpy.context.scene.render.use_shadows = False
    bpy.context.scene.render.use_sss = False
    bpy.context.scene.render.use_envmaps = False
    bpy.context.scene.render.use_raytrace = False
    bpy.context.scene.render.filepath = "/home/maurizio/Videos/yoga_4.avi"
    bpy.context.scene.render.image_settings.file_format = 'H264'
    #bpy.context.scene.file_format = 'XVID'
    bpy.context.scene.render.image_settings.color_mode = 'RGB'
    bpy.context.scene.render.ffmpeg.audio_codec = 'MP3'
    bpy.context.scene.render.ffmpeg.audio_bitrate = 192
    
    

def load_sequence_for_planes(list_of_files):
    """return list_of_files_for_planes
    """
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

def select_camera(name="Camera"):    
    bpy.ops.object.select_pattern(pattern=name)
    
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
    bpy.context.scene.objects.active = obj #attiva l'oggetto richiesto


def load_all_in_blender():
    base_dir="/home/maurizio/GitBook/Library/maoz75/gli-appunti/figures/asana_yoga/"
    #sequenza = load_sequence(get_yoga_files(base_dir))
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

    
