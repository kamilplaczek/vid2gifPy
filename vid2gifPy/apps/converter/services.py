from moviepy.editor import *
from .models import Size, Quality, CaptionPosition, LoopMode, Speed
import string
from moviepy.config import change_settings
# TODO: fix paths
change_settings({"IMAGEMAGICK_BINARY": r"D:\imagemagick\convert.exe"})


class VidConvertService:
    @staticmethod
    def time_symetrize(clip):
        """ Returns the clip played forwards then backwards. In case
        you are wondering, vfx (short for Video FX) is loaded by
        >>> from moviepy.editor import * """
        return concatenate([clip, clip.fx(vfx.time_mirror)])

    def get_size(self, size: int):
        switcher = {
            Size.original.value: 1,
            Size.smaller.value: 0.5,
            Size.bigger.value: 1.5
        }
        return switcher.get(size, 1)

    def get_fps(self, quality: int):
        switcher = {
            Quality.regular.value: 15,
            Quality.high.value: 30,
            Quality.low.value: 60
        }
        return switcher.get(quality, 30)

    def get_speed(self, quality: int):
        switcher = {
            Speed.normal.value: 1,
            Speed.fast.value: 1.5,
            Speed.slow.value: 0.5
        }
        return switcher.get(quality, 1)

    def get_text_offset(self, pos: int):
        switcher = {
            CaptionPosition.top.value: 'top',
            CaptionPosition.middle.value: 'center',
            CaptionPosition.bottom.value: 'bottom'
        }
        return switcher.get(pos, 'top')


    def save_thumb(self, vid, id):
        small_vid = vid.resize(height=200)
        small_vid.save_frame('static/thumbs/{0}.jpg'.format(id))

    def convert_to_gif(self, vidPath: string, id: int, size: int, speed: int, quality: int, loopMode: int,
                       captionPos: int, caption: string = None) -> string:
        size = self.get_size(size)
        fps = self.get_fps(quality)
        speed = self.get_speed(speed)

        if loopMode == LoopMode.symmetrical.value:
            vid = VideoFileClip(vidPath).resize(size).speedx(speed).fx(VidConvertService.time_symetrize)
        else:
            vid = VideoFileClip(vidPath).resize(size).speedx(speed)

        composition = None;
        if caption is not None:
            text = (TextClip(caption,
                             fontsize=24, color='white',
                             font='Arial', interline=-25)
                .set_pos(("center", self.get_text_offset(captionPos)))
                .set_duration(vid.duration))
            composition = CompositeVideoClip([vid, text])

        filename = '{0}.gif'.format(id)
        path = 'static/results/' + filename
        self.save_thumb(vid, id)
        # TODO: figure out ImageMagick output dir and use it, optimize output
        if composition is not None:
            composition.write_gif(path,fps=fps)
        else:
            vid.write_gif(path, fps=fps)
        return filename
