import os

from pprint import pprint

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {} # 裝載key為字幕檔案名 值為字幕字典(key為字幕 value is time
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR,caption_file), "r") as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip() #刪除前後空白
                    if "-->" in line:
                        time_line = True #找到時間那一行就做記號
                        time = line
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False # reset
            data[caption_file] = captions
        pprint(data)
        return data

