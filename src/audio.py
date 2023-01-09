from multiprocessing import Process

import subprocess

audio_asset = "../assets/marc.m4a"


def mpv_audio():
    subprocess.run(
        "2>/dev/null 1>/dev/null " + "mpv --no-video --loop " + audio_asset, shell=True
    )


play_audio_process = Process(target=mpv_audio)


def play_audio():
    play_audio_process.start()


def stop_audio():
    play_audio_process.terminate()
    subprocess.run("kill $(pidof mpv)", shell=True)
