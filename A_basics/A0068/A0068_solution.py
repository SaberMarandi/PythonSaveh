# A0068 - تبدیل ثانیه به روز
# تبدیل ثانیه به فرمت روز:ساعت:دقیقه:ثانیه

seconds = int(input())
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
secs = seconds % 60
print(f"{days}:{hours}:{minutes}:{secs}")
