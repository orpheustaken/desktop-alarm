from multiprocessing import Process

import subprocess


class Audio:
    audio_asset = "src/assets/marc.m4a"

    @staticmethod
    def mpv_audio():
        subprocess.run(
            "2>/dev/null 1>/dev/null " + "mpv --no-video --loop " + Audio.audio_asset, shell=True
        )

    audio_subprocess = Process(target=mpv_audio)

    @staticmethod
    def play_audio():
        Audio.audio_subprocess.start()

    @staticmethod
    def stop_audio():
        Audio.audio_subprocess.terminate()
        subprocess.run("kill $(pidof mpv)", shell=True)
