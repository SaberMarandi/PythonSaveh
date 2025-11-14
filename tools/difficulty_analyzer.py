#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ابزار تحلیل سختی مسائل در پروژه PythonSaveh
"""

import os
import re
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class ProblemInfo:
    """اطلاعات یک مسئله"""
    id: str
    title: str
    difficulty: int
    category: str
    concepts: List[str]
    estimated_time: int  # دقیقه

class DifficultyAnalyzer:
    """کلاس تحلیل سختی مسائل"""
    
    def __init__(self):
        self.difficulty_keywords = {
            1: ["hello", "جمع", "تفریق", "ضرب", "تقسیم", "print", "input"],
            2: ["if", "else", "شرط", "مقایسه", "زوج", "فرد", "بزرگترین"],
            3: ["for", "while", "حلقه", "فاکتوریل", "فیبوناچی", "جدول"],
            4: ["list", "لیست", "آرایه", "مرتب‌سازی", "جستجو", "الگوریتم"],
            5: ["function", "تابع", "بازگشت", "recursive", "پیچیده"],
            6: ["class", "کلاس", "oop", "پیشرفته", "بهینه‌سازی", "الگوریتم پیچیده"]
        }
        
        self.time_estimates = {
            1: 5,   # 5 دقیقه
            2: 10,  # 10 دقیقه
            3: 20,  # 20 دقیقه
            4: 30,  # 30 دقیقه
            5: 45,  # 45 دقیقه
            6: 60   # 60 دقیقه
        }
    
    def analyze_problem_file(self, file_path: str) -> ProblemInfo:
        """تحلیل یک فایل مسئله"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # استخراج اطلاعات پایه
            problem_id = self._extract_problem_id(file_path)
            title = self._extract_title(content)
            category = self._extract_category(file_path)
            concepts = self._extract_concepts(content)
            difficulty = self._calculate_difficulty(content, concepts)
            estimated_time = self.time_estimates.get(difficulty, 30)
            
            return ProblemInfo(
                id=problem_id,
                title=title,
                difficulty=difficulty,
                category=category,
                concepts=concepts,
                estimated_time=estimated_time
            )
        
        except Exception as e:
            print(f"خطا در تحلیل فایل {file_path}: {e}")
            return None
    
    def _extract_problem_id(self, file_path: str) -> str:
        """استخراج شناسه مسئله از مسیر فایل"""
        match = re.search(r'([A-Z]\d{4})', file_path)
        return match.group(1) if match else "UNKNOWN"
    
    def _extract_title(self, content: str) -> str:
        """استخراج عنوان مسئله"""
        lines = content.split('\n')
        for line in lines[:10]:  # جستجو در 10 خط اول
            if line.strip().startswith('#') and not line.startswith('#!/'):
                return line.strip('# ').strip()
        return "بدون عنوان"
    
    def _extract_category(self, file_path: str) -> str:
        """استخراج دسته‌بندی از مسیر فایل"""
        if 'A_basics' in file_path:
            return 'مبانی'
        elif 'B_data_structures' in file_path:
            return 'ساختار داده'
        elif 'C_functions_modules' in file_path:
            return 'توابع و ماژول‌ها'
        elif 'D_file_data' in file_path:
            return 'فایل و داده'
        elif 'E_oop' in file_path:
            return 'شی‌گرایی'
        elif 'F_standard_modules' in file_path:
            return 'ماژول‌های استاندارد'
        return 'نامشخص'
    
    def _extract_concepts(self, content: str) -> List[str]:
        """استخراج مفاهیم برنامه‌نویسی از محتوا"""
        concepts = []
        content_lower = content.lower()
        
        concept_patterns = {
            'متغیر': ['variable', 'متغیر', '='],
            'شرط': ['if', 'else', 'elif', 'شرط'],
            'حلقه': ['for', 'while', 'حلقه', 'loop'],
            'تابع': ['def', 'function', 'تابع'],
            'لیست': ['list', 'لیست', '[', ']'],
            'رشته': ['string', 'str', 'رشته', '"', "'"],
            'عدد': ['int', 'float', 'عدد', 'number'],
            'ورودی': ['input', 'ورودی'],
            'خروجی': ['print', 'خروجی', 'output'],
            'حلقه for': ['for', 'range'],
            'حلقه while': ['while'],
            'آرایه': ['array', 'آرایه'],
            'دیکشنری': ['dict', 'دیکشنری', '{', '}']
        }
        
        for concept, patterns in concept_patterns.items():
            if any(pattern in content_lower for pattern in patterns):
                concepts.append(concept)
        
        return concepts
    
    def _calculate_difficulty(self, content: str, concepts: List[str]) -> int:
        """محاسبه سطح سختی بر اساس محتوا و مفاهیم"""
        content_lower = content.lower()
        scores = []
        
        # امتیازدهی بر اساس کلمات کلیدی
        for difficulty, keywords in self.difficulty_keywords.items():
            score = sum(1 for keyword in keywords if keyword in content_lower)
            if score > 0:
                scores.append(difficulty)
        
        # امتیازدهی بر اساس تعداد مفاهیم
        concept_count = len(concepts)
        if concept_count <= 2:
            scores.append(1)
        elif concept_count <= 4:
            scores.append(2)
        elif concept_count <= 6:
            scores.append(3)
        elif concept_count <= 8:
            scores.append(4)
        else:
            scores.append(5)
        
        # امتیازدهی بر اساس طول کد
        line_count = len([line for line in content.split('\n') if line.strip()])
        if line_count <= 10:
            scores.append(1)
        elif line_count <= 20:
            scores.append(2)
        elif line_count <= 40:
            scores.append(3)
        elif line_count <= 60:
            scores.append(4)
        else:
            scores.append(5)
        
        # میانگین امتیازها
        return min(6, max(1, round(sum(scores) / len(scores))))
    
    def analyze_directory(self, directory: str) -> List[ProblemInfo]:
        """تحلیل تمام مسائل در یک دایرکتوری"""
        problems = []
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    file_path = os.path.join(root, file)
                    problem_info = self.analyze_problem_file(file_path)
                    if problem_info:
                        problems.append(problem_info)
        
        return sorted(problems, key=lambda x: x.id)
    
    def generate_difficulty_report(self, problems: List[ProblemInfo]) -> Dict:
        """تولید گزارش سختی مسائل"""
        difficulty_counts = {i: 0 for i in range(1, 7)}
        category_counts = {}
        total_time = 0
        
        for problem in problems:
            difficulty_counts[problem.difficulty] += 1
            category_counts[problem.category] = category_counts.get(problem.category, 0) + 1
            total_time += problem.estimated_time
        
        difficulty_labels = {
            1: "🟢 مبتدی",
            2: "🟡 ابتدایی", 
            3: "🟠 متوسط",
            4: "🔴 متوسط به بالا",
            5: "🟣 پیشرفته",
            6: "⚫ خیلی پیشرفته"
        }
        
        return {
            "total_problems": len(problems),
            "difficulty_distribution": {
                difficulty_labels[k]: v for k, v in difficulty_counts.items()
            },
            "category_distribution": category_counts,
            "estimated_total_time": f"{total_time // 60} ساعت و {total_time % 60} دقیقه",
            "average_difficulty": round(sum(p.difficulty for p in problems) / len(problems), 2)
        }

def main():
    """تست ابزار تحلیل سختی"""
    analyzer = DifficultyAnalyzer()
    
    # تحلیل دایرکتوری A_basics
    if os.path.exists("A_basics"):
        problems = analyzer.analyze_directory("A_basics")
        report = analyzer.generate_difficulty_report(problems)
        
        print("گزارش تحلیل سختی مسائل:")
        print(f"تعداد کل مسائل: {report['total_problems']}")
        print(f"میانگین سختی: {report['average_difficulty']}")
        print(f"زمان تخمینی کل: {report['estimated_total_time']}")
        
        print("\nتوزیع سختی:")
        for difficulty, count in report['difficulty_distribution'].items():
            print(f"  {difficulty}: {count} مسئله")
        
        print("\nتوزیع دسته‌بندی:")
        for category, count in report['category_distribution'].items():
            print(f"  {category}: {count} مسئله")

if __name__ == "__main__":
    main()