# عملگرهای منطقی 🧠

## ترکیب شرط‌ها

گاهی باید چند شرط رو با هم ترکیب کنیم. مثلاً: "اگه سن بالای 18 **و** کارت ملی داشته باشی، می‌تونی رای بدی"

## 🎯 عملگرهای منطقی

### 1. و (and)
هر دو شرط باید درست باشن

```python
# هر دو باید True باشن
age = 20
has_id = True

can_vote = age >= 18 and has_id
print(can_vote)  # True

# مثال
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
    print("هوا عالیه برای پیک‌نیک! 🌞")
```

### 2. یا (or)
حداقل یکی از شرط‌ها باید درست باشه

```python
# یکی True باشه کافیه
is_weekend = True
is_holiday = False

can_rest = is_weekend or is_holiday
print(can_rest)  # True

# مثال
has_cash = False
has_card = True

if has_cash or has_card:
    print("می‌تونی خرید کنی! 💳")
```

### 3. نه (not)
شرط رو برعکس می‌کنه

```python
# برعکس کردن
is_raining = False
can_play_outside = not is_raining
print(can_play_outside)  # True

# مثال
is_busy = False

if not is_busy:
    print("می‌تونی بیای بیرون! 🎉")
```

## 🎮 مثال‌های کاربردی

### مثال 1: بررسی دسترسی
```python
print("🔐 سیستم ورود")

username = input("نام کاربری: ")
password = input("رمز عبور: ")
age = int(input("سن: "))

# هر سه شرط باید درست باشه
if username == "admin" and password == "1234" and age >= 18:
    print("✅ ورود موفق!")
    print("خوش آمدید!")
else:
    print("❌ دسترسی رد شد!")
```

### مثال 2: بررسی تخفیف
```python
print("🎁 بررسی تخفیف")

is_student = input("دانشجو هستی؟ (yes/no): ") == "yes"
is_senior = int(input("سن: ")) >= 60
purchase_amount = float(input("مبلغ خرید: "))

# دانشجو یا سالمند تخفیف می‌گیره
if (is_student or is_senior) and purchase_amount > 50000:
    discount = purchase_amount * 0.15
    final_price = purchase_amount - discount
    print(f"🎉 تخفیف 15%: {discount} تومان")
    print(f"قیمت نهایی: {final_price} تومان")
else:
    print(f"قیمت: {purchase_amount} تومان")
```

### مثال 3: بررسی آب و هوا
```python
print("🌤️ پیشنهاد لباس")

temperature = float(input("دما (سانتیگراد): "))
is_raining = input("داره بارون میاد؟ (yes/no): ") == "yes"
is_windy = input("باد زیاده؟ (yes/no): ") == "yes"

if temperature < 10 and (is_raining or is_windy):
    print("🧥 کاپشن ضخیم و چتر ببر!")
elif temperature < 10:
    print("🧥 کاپشن ببر!")
elif is_raining:
    print("☂️ چتر فراموش نشه!")
elif temperature > 30:
    print("👕 لباس نازک بپوش!")
else:
    print("👔 لباس معمولی کافیه!")
```

### مثال 4: بازی ورود به پارک
```python
print("🎢 ورود به پارک تفریحی")

age = int(input("سن: "))
height = float(input("قد (سانتیمتر): "))
has_ticket = input("بلیط داری؟ (yes/no): ") == "yes"

# شرط‌های ورود
can_enter = has_ticket and age >= 5 and height >= 120

if can_enter:
    print("✅ می‌تونی وارد بشی!")
    
    # بررسی سواری‌های خاص
    if age >= 12 and height >= 140:
        print("🎢 می‌تونی سواری ترسناک هم بری!")
    else:
        print("🎠 فقط سواری‌های ساده!")
else:
    if not has_ticket:
        print("❌ اول بلیط بخر!")
    elif age < 5:
        print("❌ خیلی کوچیکی!")
    else:
        print("❌ قدت کمه!")
```

## 💡 نکات مهم

### 1. جدول صحت and
```python
# True and True = True
print(True and True)    # True

# True and False = False
print(True and False)   # False

# False and True = False
print(False and True)   # False

# False and False = False
print(False and False)  # False
```

### 2. جدول صحت or
```python
# True or True = True
print(True or True)     # True

# True or False = True
print(True or False)    # True

# False or True = True
print(False or True)    # True

# False or False = False
print(False or False)   # False
```

### 3. جدول صحت not
```python
# not True = False
print(not True)   # False

# not False = True
print(not False)  # True
```

### 4. اولویت عملگرها
```python
# not بالاترین اولویت رو داره
result = not False and True
print(result)  # True

# با پرانتز واضح‌تر می‌شه
result = (not False) and True
print(result)  # True
```

### 5. ترکیب پیچیده
```python
# می‌تونی همه رو ترکیب کنی
age = 25
has_license = True
has_car = False
is_raining = True

can_drive = age >= 18 and has_license and has_car and not is_raining
print(can_drive)  # False (چون ماشین نداره یا بارون میاد)
```

## 🎯 تمرین‌های عملی

### تمرین 1: بررسی عدد
```python
# یه برنامه بنویس که:
# - یه عدد بگیره
# - بگه آیا عدد بین 10 تا 20 هست
# - بگه آیا عدد زوج هست

num = int(input("یه عدد وارد کن: "))

# ادامه بده...
```

### تمرین 2: سیستم امتیازدهی
```python
# یه برنامه بنویس که:
# - نمره 3 درس رو بگیره
# - اگه همه بالای 10 بودن، "قبول"
# - اگه حتی یکی زیر 10 بود، "مردود"
# - میانگین رو هم نشون بده

math = float(input("نمره ریاضی: "))
physics = float(input("نمره فیزیک: "))
chemistry = float(input("نمره شیمی: "))

# ادامه بده...
```

### تمرین 3: بررسی رمز عبور
```python
# یه برنامه بنویس که بررسی کنه رمز عبور قوی هست یا نه:
# - حداقل 8 کاراکتر
# - حداقل یه عدد داشته باشه
# - حداقل یه حرف بزرگ داشته باشه

password = input("رمز عبور: ")

# ادامه بده...
# راهنمایی: از len() و متدهای رشته استفاده کن
```

### تمرین 4: محاسبه بیمه
```python
# یه برنامه بنویس که:
# - سن راننده رو بگیره
# - سابقه رانندگی رو بگیره
# - تعداد تصادفات رو بگیره
# - اگه سن < 25 یا تصادف > 2، بیمه گرونه
# - اگه سابقه > 5 و تصادف = 0، بیمه ارزونه

age = int(input("سن: "))
experience = int(input("سابقه رانندگی (سال): "))
accidents = int(input("تعداد تصادفات: "))

# ادامه بده...
```

## 🌟 چالش: سیستم ورود پیشرفته

یه سیستم ورود بساز که:
1. نام کاربری و رمز عبور بگیره
2. 3 بار فرصت بده
3. اگه 3 بار اشتباه وارد کرد، حساب قفل بشه
4. اگه درست وارد کرد، منوی کاربری نشون بده

```python
print("🔐 سیستم ورود امن")
print("-" * 40)

correct_username = "admin"
correct_password = "python123"
max_attempts = 3
attempts = 0

# ادامه بده...
```

## 📊 جدول خلاصه

| عملگر | معنی | مثال | نتیجه |
|-------|------|------|-------|
| and | و (هر دو) | True and False | False |
| or | یا (حداقل یکی) | True or False | True |
| not | نه (برعکس) | not True | False |

## 🎨 نکته طلایی

از پرانتز استفاده کن تا کدت واضح‌تر بشه:

```python
# ❌ گیج‌کننده
result = age > 18 and has_id or is_vip and not is_banned

# ✅ واضح
result = (age > 18 and has_id) or (is_vip and not is_banned)
```

## ➡️ مرحله بعد

حالا که با عملگرهای منطقی آشنا شدی، بیا یاد بگیریم اولویت عملگرها چطوریه!
برو به [اولویت عملگرها](04_precedence.md)
