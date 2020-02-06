import os
import sys

####################################################################################
# Get the argument about the test from command line 
# 'python runner.py smoke_tests' - smoke_tests is the 1st Argument sys.argv[1]
####################################################################################
test_suite_name = "smoke_tests" #sys.argv[1] + ".sikuli"

####################################################################################
# Asign paths to variables
# Get Current Working Dir - The folder where Python is operating at the moment - C:\framework
####################################################################################
root_dir = os.getcwd() 
tools_dir = os.path.join(root_dir, 'tools')
content_dir = os.path.join(root_dir, 'content')
sikuli_path = os.path.join(root_dir, 'sikuli', 'runsikulix.cmd')
tests_path = os.path.join(root_dir, 'tests', test_suite_name)

ffmpeg_path = os.path.join(tools_dir, 'video_recorder', 'ffmpeg.exe')
textbox_exe_path = os.path.join(tools_dir, 'textbox', 'Textbox.exe')
textbox_txt_path = os.path.join(tools_dir, 'textbox', 'textbox.txt')

####################################################################################
# PRECONDITIONS - Start Video Recording and Textbox
####################################################################################
os.system("taskkill /im ffmpeg.exe")
os.system("taskkill /im Textbox.exe")
os.system(r'start ' + textbox_exe_path + ' ' + textbox_txt_path)
os.system(r'start ' + ffmpeg_path + ' -f gdigrab -framerate 15 -i desktop -q:v 5 screenVideo.avi -y')

####################################################################################
# Assemble the command used to run the set
# call C:\ui-automation\Sikuli\runsikulix.cmd -r C:\ui-automation\Tests\smoke_tests.sikuli
####################################################################################
command ="call " + sikuli_path + " -r " + tests_path
print(command)

####################################################################################
# RUN TESTS
####################################################################################
os.system(command)

####################################################################################
# POSTCONDITIONS - Kill all leftovers - Video Recording + Textbox
####################################################################################
os.system("taskkill /im ffmpeg.exe")
os.system("taskkill /im Textbox.exe")

