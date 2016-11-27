from moviepy.editor import *
import uuid


class VidConvertService:
    def convert_to_gif(self, vidPath, id):
        vid = (VideoFileClip(vidPath).resize(0.5))
        path = 'static/results/{0}.gif'.format(id)
        vid.write_gif(path)
