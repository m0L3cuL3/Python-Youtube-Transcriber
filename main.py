
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
import dearpygui.dearpygui as dpg
from dearpygui.dearpygui import *


author = 'Sean Baang'
version = '1.0.1'

dpg.create_context()

def get_transcription():
    data = yta.get_transcript(get_value("Youtube##ID"))
    transcript = ''

    for value in data:
        for key,val in value.items():
            if key == 'text':
                transcript += val

    l = transcript.splitlines()
    final_tra = " ".join(l)

    #### SAVE TO FILE ####
    # file = open("transcript.txt", 'w')
    # file.write(final_tra)
    # file.close()
    ######################

    # Display Transcript
    dpg.add_text(final_tra, parent="Main Window", wrap=500, tag="script")

def download_transcript():
    file = open("transcript.txt", 'w')
    file.write(get_value("script"))
    file.close()

def clear_all():
    dpg.delete_item("script")

with dpg.window(tag="Main Window", pos=(100,100)):
    dpg.add_text("Youtube Transcriber - {0}".format(version))
    dpg.add_text("Coded by {0}".format(author))

    dpg.add_spacer()
    dpg.add_separator()
    dpg.add_spacer()
    
    dpg.add_text("Youtube ID:")
    it1 = dpg.add_input_text(tag="Youtube##ID")
    dpg.add_same_line()
    b1 = dpg.add_button(label="Get Transcript", callback=get_transcription)
    b2 = dpg.add_button(label="Download Transcript", callback=download_transcript)
    dpg.add_same_line()
    bclear = dpg.add_button(label="Clear", callback=clear_all)

    dpg.add_spacer()
    dpg.add_separator()
    dpg.add_spacer()

with dpg.theme() as item_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (135, 135, 135), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 12, 5)

dpg.bind_item_theme(b1, item_theme)
dpg.bind_item_theme(b2, item_theme)
dpg.bind_item_theme(bclear, item_theme)
dpg.bind_item_theme(it1, item_theme)

dpg.create_viewport(
    title="Youtube Transciber", 
    width=550, 
    height=550, 
    resizable=False)  # create viewport takes in config options too!

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Main Window", True)
dpg.start_dearpygui()
dpg.destroy_context()