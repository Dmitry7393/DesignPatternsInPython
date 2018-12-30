

class MediaPlayer(object):

    def __init__(self):
        pass

    def play(self, audio_type, file_name):
        pass


class AdvancedMediaPlayer(object):

    def play_vlc(self, file_name):
        pass

    def play_mp4(self, file_name):
        pass


class VlcPlayer(AdvancedMediaPlayer):

    def play_vlc(self, file_name):
        print('Playing vlc file', file_name)

    def play_mp4(self, file_name):
        pass


class Mp4Player(AdvancedMediaPlayer):

    def play_mp4(self, file_name):
        print('Playing mp4 file', file_name)

    def play_vlc(self, file_name):
        pass


class MediaAdapter(MediaPlayer):

    def __init__(self, audio_type):
        MediaPlayer.__init__(self)

        if audio_type == 'vlc':
            self.advanced_media_player = VlcPlayer()
        if audio_type == 'mp4':
            self.advanced_media_player = Mp4Player()

    def play(self, audio_type, file_name):
        if audio_type == 'vlc':
            self.advanced_media_player.play_vlc(file_name)
        elif audio_type == 'mp4':
            self.advanced_media_player.play_mp4(file_name)


class AudioPlayer(MediaPlayer):

    def __init__(self):
        self.media_adapter = None

    def play(self, audio_type, file_name):

        if audio_type == 'mp3':
            print('Playing mp3 file', file_name)
        elif audio_type == 'mp4':
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, file_name)
        elif audio_type == 'vlc':
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, file_name)


def main():
    audio_player = AudioPlayer()

    audio_player.play('mp3', 'test1.mp3')
    audio_player.play('mp4', 'test2.mp4')
    audio_player.play('vlc', 'test3.vlc')
    return 0


if __name__ == "__main__":
    main()