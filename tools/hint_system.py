#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سیستم راهنمایی هوشمند برای مسائل پروژه PythonSaveh
"""

import re
import random
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class Hint:
    """کلاس راهنمایی"""
    level: int  # سطح راهنمایی (1: کلی، 2: متوسط، 3: تفصیلی)
    text: str
    code_example: Optional[str] = None

class HintSystem:
    """سیستم راهنمایی هوشمند"""
    
    def __init__(self):
        self.hint_templates = self._load_hint_templates()
        self.concept_hints = self._load_concept_hints()
    
    def _load_hint_templates(self) -> Dict:
        """بارگذاری قالب‌های راهنمایی"""
        return {
            "basic_io": {
                1: "برای دریافت ورودی از کاربر از تابع input() استفاده کنید",
                2: "برای نمایش خروجی از تابع print() استفاده کنید",
                3: "مثال: name = input('نام خود را وارد کنید: ')"
            },
            "arithmetic": {
                1: "از عملگرهای ریاضی +، -، *، / استفاده کنید",
                2: "توجه کنید که input() همیشه رشته برمی‌گرداند، باید به عدد تبدیل کنید",
                3: "مثال: result = int(input()) + int(input())"
            },
            "conditions": {
                1: "از ساختار if-else برای تصمیم‌گیری استفاده کنید",
                2: "از عملگرهای مقایسه ==، !=، <، >، <=، >= استفاده کنید",
                3: "مثال: if number % 2 == 0: print('زوج')"
            },
            "loops": {
                1: "برای تکرار از حلقه‌های for یا while استفاده کنید",
                2: "حلقه for برای تعداد مشخص، while برای شرط مناسب است",
                3: "مثال: for i in range(1, 11): print(i)"
            },
            "strings": {
                1: "رشته‌ها در پایتون قابل تغییر نیستند",
                2: "از متدهای رشته مثل .upper()، .lower()، .strip() استفاده کنید",
                3: "مثال: text.replace('قدیمی', 'جدید')"
            },
            "lists": {
                1: "لیست‌ها مجموعه‌ای مرتب از عناصر هستند",
                2: "از متدهای .append()، .remove()، .sort() استفاده کنید",
                3: "مثال: numbers = [1, 2, 3]; numbers.append(4)"
            }
        }
    
    def _load_concept_hints(self) -> Dict:
        """بارگذاری راهنمایی‌های مفهومی"""
        return {
            "factorial": [
                "فاکتوریل n برابر است با n × (n-1) × (n-2) × ... × 1",
                "می‌توانید از حلقه for یا بازگشت استفاده کنید",
                "مثال: 5! = 5 × 4 × 3 × 2 × 1 = 120"
            ],
            "fibonacci": [
                "دنباله فیبوناچی: هر عدد مجموع دو عدد قبلی است",
                "شروع: 0, 1, 1, 2, 3, 5, 8, 13, ...",
                "فرمول: F(n) = F(n-1) + F(n-2)"
            ],
            "prime": [
                "عدد اول فقط بر 1 و خودش بخش‌پذیر است",
                "برای بررسی، عدد را بر اعداد 2 تا جذر آن تقسیم کنید",
                "اگر هیچ‌کدام باقیمانده صفر نداشت، عدد اول است"
            ],
            "palindrome": [
                "پالیندروم از راست و چپ یکسان خوانده می‌شود",
                "رشته را معکوس کنید و با اصل مقایسه کنید",
                "مثال: 'radar' معکوس شده 'radar' است"
            ],
            "sorting": [
                "مرتب‌سازی: چیدن عناصر به ترتیب صعودی یا نزولی",
                "الگوریتم‌های مختلف: حبابی، انتخابی، درجی",
                "در پایتون می‌توانید از .sort() یا sorted() استفاده کنید"
            ]
        }
    
    def get_problem_hints(self, problem_id: str, problem_content: str, level: int = 1) -> List[Hint]:
        """دریافت راهنمایی برای یک مسئله خاص"""
        hints = []
        
        # تشخیص نوع مسئله
        problem_type = self._detect_problem_type(problem_id, problem_content)
        
        # راهنمایی‌های عمومی
        general_hints = self._get_general_hints(problem_type, level)
        hints.extend(general_hints)
        
        # راهنمایی‌های مفهومی
        concept_hints = self._get_concept_hints(problem_content, level)
        hints.extend(concept_hints)
        
        # راهنمایی‌های خاص مسئله
        specific_hints = self._get_specific_hints(problem_id, level)
        hints.extend(specific_hints)
        
        return hints[:3]  # حداکثر 3 راهنمایی
    
    def _detect_problem_type(self, problem_id: str, content: str) -> str:
        """تشخیص نوع مسئله"""
        content_lower = content.lower()
        
        if any(word in content_lower for word in ['input', 'ورودی', 'دریافت']):
            return 'basic_io'
        elif any(word in content_lower for word in ['جمع', 'تفریق', 'ضرب', 'تقسیم', '+', '-', '*', '/']):
            return 'arithmetic'
        elif any(word in content_lower for word in ['if', 'شرط', 'اگر', 'condition']):
            return 'conditions'
        elif any(word in content_lower for word in ['for', 'while', 'حلقه', 'loop']):
            return 'loops'
        elif any(word in content_lower for word in ['string', 'رشته', 'text']):
            return 'strings'
        elif any(word in content_lower for word in ['list', 'لیست', 'array']):
            return 'lists'
        else:
            return 'general'
    
    def _get_general_hints(self, problem_type: str, level: int) -> List[Hint]:
        """دریافت راهنمایی‌های عمومی"""
        hints = []
        
        if problem_type in self.hint_templates:
            template = self.hint_templates[problem_type]
            for hint_level in range(1, min(level + 1, 4)):
                if hint_level in template:
                    hints.append(Hint(
                        level=hint_level,
                        text=template[hint_level]
                    ))
        
        return hints
    
    def _get_concept_hints(self, content: str, level: int) -> List[Hint]:
        """دریافت راهنمایی‌های مفهومی"""
        hints = []
        content_lower = content.lower()
        
        for concept, concept_hints in self.concept_hints.items():
            if concept in content_lower or any(word in content_lower for word in concept.split('_')):
                for i, hint_text in enumerate(concept_hints[:level]):
                    hints.append(Hint(
                        level=i + 1,
                        text=hint_text
                    ))
                break
        
        return hints
    
    def _get_specific_hints(self, problem_id: str, level: int) -> List[Hint]:
        """دریافت راهنمایی‌های خاص مسئله"""
        specific_hints = {
            "A0001": [
                Hint(1, "فقط یک خط کد نیاز دارید", 'print("Hello, World!")'),
                Hint(2, "از تابع print استفاده کنید", None),
                Hint(3, "دقیقاً همین متن را چاپ کنید: Hello, World!", None)
            ],
            "A0002": [
                Hint(1, "دو عدد بگیرید و جمع کنید"),
                Hint(2, "input() رشته برمی‌گرداند، به int تبدیل کنید"),
                Hint(3, "مثال: a = int(input()); b = int(input()); print(a + b)")
            ],
            "A0012": [
                Hint(1, "از عملگر باقیمانده % استفاده کنید"),
                Hint(2, "اگر عدد % 2 == 0 باشد، زوج است"),
                Hint(3, "if number % 2 == 0: print('زوج') else: print('فرد')")
            ],
            "A0018": [
                Hint(1, "فاکتوریل n = n × (n-1) × ... × 1"),
                Hint(2, "از حلقه for با range(1, n+1) استفاده کنید"),
                Hint(3, "result = 1; for i in range(1, n+1): result *= i")
            ]
        }
        
        if problem_id in specific_hints:
            return specific_hints[problem_id][:level]
        
        return []
    
    def get_progressive_hints(self, problem_id: str, problem_content: str, attempt_count: int) -> Hint:
        """دریافت راهنمایی تدریجی بر اساس تعداد تلاش"""
        if attempt_count <= 2:
            level = 1  # راهنمایی کلی
        elif attempt_count <= 4:
            level = 2  # راهنمایی متوسط
        else:
            level = 3  # راهنمایی تفصیلی
        
        hints = self.get_problem_hints(problem_id, problem_content, level)
        
        if hints:
            return random.choice(hints)
        else:
            return Hint(1, "سعی کنید مسئله را قدم به قدم حل کنید")
    
    def get_error_based_hint(self, error_message: str) -> Hint:
        """راهنمایی بر اساس پیغام خطا"""
        error_hints = {
            "SyntaxError": "خطای نحوی: بررسی کنید که پرانتزها و نقل‌قول‌ها بسته شده باشند",
            "NameError": "متغیر تعریف نشده: مطمئن شوید که متغیر را قبل از استفاده تعریف کرده‌اید",
            "TypeError": "نوع داده اشتباه: بررسی کنید که نوع داده‌ها مناسب عملیات باشند",
            "ValueError": "مقدار نامعتبر: ورودی را بررسی کنید، ممکن است نیاز به تبدیل نوع داشته باشد",
            "IndentationError": "خطای تورفتگی: بررسی کنید که خطوط درست تورفته شده باشند",
            "ZeroDivisionError": "تقسیم بر صفر: مطمئن شوید که مخرج صفر نیست"
        }
        
        for error_type, hint_text in error_hints.items():
            if error_type in error_message:
                return Hint(2, hint_text)
        
        return Hint(1, "خطای ناشناخته: کد خود را دوباره بررسی کنید")

def main():
    """تست سیستم راهنمایی"""
    hint_system = HintSystem()
    
    # تست راهنمایی برای مسئله A0001
    hints = hint_system.get_problem_hints("A0001", "Hello World problem", 2)
    print("راهنمایی‌های A0001:")
    for hint in hints:
        print(f"سطح {hint.level}: {hint.text}")
        if hint.code_example:
            print(f"مثال: {hint.code_example}")
    
    # تست راهنمایی تدریجی
    progressive_hint = hint_system.get_progressive_hints("A0002", "جمع دو عدد", 3)
    print(f"\nراهنمایی تدریجی: {progressive_hint.text}")
    
    # تست راهنمایی بر اساس خطا
    error_hint = hint_system.get_error_based_hint("NameError: name 'x' is not defined")
    print(f"\nراهنمایی خطا: {error_hint.text}")

if __name__ == "__main__":
    main()