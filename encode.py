import os
import subprocess

def ffmpegEncode(folder_path, file_name, action):
    if action == 0:  # 不轉檔
        return
    elif action == 1:  # Intel VAAPI GPU轉檔 (HD620 i5-7200U)
        os.chdir(folder_path)
        input_file = f'{file_name}.mp4'
        out_tmp = f'f_{file_name}.mp4'
        # VAAPI所需环境变量
        va_env = os.environ.copy()
        va_env["LIBVA_DRIVER_NAME"] = "iHD"
        va_env["VAAPI_DRM_DEVICE"] = "/dev/dri/renderD129"

        # cmd = [
        #     'ffmpeg',
        #     '-hwaccel', 'vaapi',
        #     '-hwaccel_device', '/dev/dri/renderD129',
        #     '-i', input_file,
        #     '-vf', 'hwupload_vaapi',
        #     '-c:v', 'h264_vaapi',
        #     '-low_power', '1',
        #     '-b:v', '6000K',
        #     '-threads', '5',
        #     '-nostdin',
        #     out_tmp
        # ]
        cmd = [
            'ffmpeg',
            '-hwaccel', 'vaapi',
            '-hwaccel_device', '/dev/dri/renderD129',
            '-i', input_file,
            '-vf', 'hwupload,format=vaapi',
            '-c:v', 'h264_vaapi',
            '-low_power', '1',
            '-b:v', '6000K',
            '-threads', '5',
            '-nostdin',
            out_tmp
        ]
        print("\n\n ffmpeg cmd:", cmd, "\n\n")
        try:
            ret = subprocess.call(cmd, env=va_env)
            if ret == 0:
                os.remove(os.path.join(folder_path, input_file))
                os.rename(os.path.join(folder_path, out_tmp), os.path.join(folder_path, input_file))
                print("VAAPI GPU轉檔成功!")
            else:
                print("VAAPI GPU轉檔失敗! ffmpeg返回非0代码")
        except Exception as e:
            print(f"VAAPI GPU轉檔異常! {e}")

    elif action == 2:  # CPU轉檔(不变)
        os.chdir(folder_path)
        try:
            subprocess.call([
                'ffmpeg', '-i', f'{file_name}.mp4',
                '-c:v', 'libx264', '-b:v', '3M',
                '-threads', '5', '-preset', 'superfast',
                f'f_{file_name}.mp4'
            ])
            os.remove(os.path.join(folder_path, f'{file_name}.mp4'))
            os.rename(os.path.join(folder_path, f'f_{file_name}.mp4'), os.path.join(folder_path, f'{file_name}.mp4'))
            print("CPU轉檔成功!")
        except Exception as e:
            print(f"CPU轉檔失敗! {e}")
    else:
        return
