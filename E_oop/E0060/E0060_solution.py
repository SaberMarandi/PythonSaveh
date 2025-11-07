class Media:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
    def play(self):
        return f"پخش {self.title}"

class Video(Media):
    def __init__(self, title, duration, resolution):
        super().__init__(title, duration)
        self.resolution = resolution
    
    def play(self):
        return f"{super().play()} با کیفیت {self.resolution}"

class Audio(Media):
    def __init__(self, title, duration, bitrate):
        super().__init__(title, duration)
        self.bitrate = bitrate
    
    def play(self):
        return f"{super().play()} با بیت‌ریت {self.bitrate}"

# دریافت ورودی
media_type = input()
title = input()
duration = int(input())

if media_type == "video":
    resolution = input()
    media = Video(title, duration, resolution)
elif media_type == "audio":
    bitrate = input()
    media = Audio(title, duration, bitrate)

print(media.play())
print(f"مدت: {media.duration} دقیقه")
