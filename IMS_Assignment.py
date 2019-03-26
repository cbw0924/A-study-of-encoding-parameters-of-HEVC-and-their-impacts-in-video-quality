import os
line = '------------------------------------------------------------------------------------------------'   #create a separator line
while 1:
    video = input('please input the video:')                                                                #input the native y4m video
    (videoname, extension) = os.path.splitext(video)                                                        #separate video name and extension
    
    if os.path.isfile(video) == True:                                                                       #check if the input video file exsit
        input_parameters = input('please input encoding parameters which you want to test:')               #input the encoding parameter
        
        if input_parameters == 'crf':
            while 1:
                crf_list = []
                
                while 1:
                    crf_value = input("input the vaule of crf:")                                             # input CRF value
                    if crf_value == 'exit':
                        break
                    if 0 <= int(crf_value) <= 51:
                        crf_list.append(crf_value)                                                           #put CRF value in the list
                    else:
                        print('please input again')
                        continue
                    
                for crf in crf_list:                                                                         #use all CRF value in the list to test
                    enc1 = os.system('./ffmpeg -i '+video+' -c:v libx265 -crf'+' '+crf+' '+videoname+'crf'+crf+'.mp4')                   #encode
                    print(enc1)
                    print(line)
                    dec1 = os.system('./ffmpeg -i '+videoname+'crf'+crf+'.mp4'+' '+videoname+'_dec_crf'+crf+'.y4m')                      #decode
                    print(dec1)
                    print(line)
                    psnr1 = os.system('./ffmpeg -i '+videoname+'_dec_crf'+crf+'.y4m'+' -i '+video+' -lavfi psnr=psnrlog_crf'+crf+' -f null -')  #measure psnr
                    print(psnr1)
                    print(line)
                    ssim1 = os.system('./ffmpeg -i '+videoname+'_dec_crf'+crf+'.y4m'+' -i '+video+' -lavfi ssim=simlog_crf'+crf+' -f null -')  #measure ssim
                    print(ssim1)
                    print(line)
                    vmaf1 = os.system('./ffmpeg -i '+videoname+'_dec_crf'+crf+'.y4m'+' -i '+video+' -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')  #measure vmaf
                    print(vmaf1)
                    print(line)
                    
                    
        elif input_parameters == 'preset':
            while 1:
                preset = input('input the preset:')
                ten_presets=['placebo','veryslow','slower','slow','medium','fast','faster','veryfast','superfast','ultrafast']  #put ten presets in the list
                if preset in ten_presets:
                    enc2 = os.system('./ffmpeg -i '+video+' -c:v libx265 -preset'+' '+preset+' '+videoname+'preset'+preset+'.mp4')
                    print(enc2)
                    print(line)
                    dec2 = os.system('./ffmpeg -i '+videoname+'preset'+preset+'.mp4'+' '+videoname+'_dec_preset'+preset+'.y4m')
                    print(dec2)
                    print(line)
                    psnr2 = os.system('./ffmpeg -i '+videoname+'_dec_preset'+preset+'.y4m'+' -i '+video+' -lavfi psnr=psnrlog_preset'+preset+' -f null -')
                    print(psnr2)
                    print(line)
                    ssim2 = os.system('./ffmpeg -i '+videoname+'_dec_preset'+preset+'.y4m'+' -i '+video+' -lavfi ssim=ssimlog_preset'+preset+' -f null -')
                    print(ssim2)
                    print(line)
                    vmaf2 = os.system('./ffmpeg -i '+videoname+'_dec_preset'+preset+'.y4m'+' -i '+video+' -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                    print(vmaf2)
                    break
                else:
                    print('please input again')
                    continue
                
        elif input_parameters == 'cbr':
            while 1:
                CBR_list=[]
                
                while  1: 
                    CBR_value = input('input the value of CBR:')   # input CBR 
                    if CBR_value == 'exit':
                        break
                    CBR_list.append(CBR_value)                  # put CBR values in the list
                    
                for CBR in CBR_list:
                    enc3 = os.system('./ffmpeg -i '+video+' -c:v libx265 '+" -x265-params 'nal-hrd=cbr' "+'-b:v'+' '+CBR+' -maxrate '+CBR+' -minrate '+CBR+' -bufsize '+CBR+' '+videoname+'CBR'+CBR+'.mp4')
                    print(enc3)
                    print(line)
                    dec3 = os.system('./ffmpeg -i '+videoname+'CBR'+CBR+'.mp4'+' '+videoname+'_dec_CBR'+CBR+'.y4m')
                    print(dec3)
                    print(line)
                    psnr3 = os.system('./ffmpeg -i '+videoname+'_dec_CBR'+CBR+'.y4m'+' -i '+video+' -lavfi psnr=psnrlog_CBR'+CBR+' -f null -')
                    print(psnr3)
                    print(line)
                    ssim3 = os.system('./ffmpeg -i '+videoname+'_dec_CBR'+CBR+'.y4m'+' -i '+video+' -lavfi ssim=ssimlog_CBR'+CBR+' -f null -')
                    print(ssim3)
                    print(line)
                    vmaf3 = os.system('./ffmpeg -i '+videoname+'_dec_CBR'+CBR+'.y4m'+' -i '+video+' -lavfi libvmaf="model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" -f null -')
                    print(vmaf3)
                    print(line)

        
        else:
            exit('Wrong')
    else:
        print('This file does not exist!')
        