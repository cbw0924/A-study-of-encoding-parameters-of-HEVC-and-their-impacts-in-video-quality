# A-study-of-encoding-parameters-of-HEVC-and-their-impacts-in-video-quality

This is an assignment of Internet Multimedia Systems, Department of Electronic & Electrical Engineering, UCL

These three steps guide users how to use this program.

Step 1:
The whole process are done in Ubuntu.
Compile (using: g++ psnr_seq.cpp –o psnr_seq) the psnr.cpp tool provided by the module organizer here: http://www.ee.ucl.ac.uk/~iandreop/psnr_seq.zip.

Install the precompiled Linux FFmpeg binary from here:http://www.ee.ucl.ac.uk/~iandreop/ffmpeg_static_with_VMAF.zip. This precompiled binary can also be used for PSNR SSIM and VMAF measurements. 

Step 2:
Put the python file, FFmpeg, video files which you want to test in one folder.

Step 3:
Run python file.
User should input the y4m video which he/she wants to test. Then, choose encoding parameters (input the cbr, crf or preset). 

The range of crf is from 0-51. User can input several crf values and program will encode,decode and meausre psnr,ssim and vmaf automately. For exmaple, user wants to test crf :0, 10,20 and 40. He/she can input values and input "exit" again. Then, the program will start to run.

There are ten presets. User can just input any one of them and the program is going to run.

For cbr, user can input several cbr values and input "exit" to stop inputing cbr. It must be pointed out here that user has to input the unit. For example, if user want to test 1M cbr, he/she should input 1M rather than 1. 
