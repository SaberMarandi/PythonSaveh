#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ابزار ردیابی پیشرفت کاربر در پروژه PythonSaveh
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional

class ProgressTracker:
    """کلاس ردیابی پیشرفت یادگیری کاربر"""
    
    def __init__(self, user_id: str = "default"):
        self.user_id = user_id
        self.progress_file = f"data/progress_{user_id}.json"
        self.progress_data = self._load_progress()
    
    def _load_progress(self) -> Dict:
        """بارگذاری داده‌های پیشرفت از فایل"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "user_id": self.user_id,
            "start_date": datetime.now().isoformat(),
            "completed_problems": [],
            "current_level": "مبتدی",
            "total_score": 0,
            "time_spent": 0,
            "categories": {
                "A_basics": {"completed": 0, "total": 200},
                "B_data_structures": {"completed": 0, "total": 100},
                "C_functions_modules": {"completed": 0, "total": 100},
                "D_file_data": {"completed": 0, "total": 150},
                "E_oop": {"completed": 0, "total": 150},
                "F_standard_modules": {"completed": 0, "total": 150}
            }
        }
    
    def _save_progress(self):
        """ذخیره داده‌های پیشرفت در فایل"""
        os.makedirs(os.path.dirname(self.progress_file), exist_ok=True)
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress_data, f, ensure_ascii=False, indent=2)
    
    def mark_completed(self, problem_id: str, category: str, score: int = 10):
        """علامت‌گذاری مسئله به عنوان تکمیل شده"""
        if problem_id not in self.progress_data["completed_problems"]:
            self.progress_data["completed_problems"].append(problem_id)
            self.progress_data["total_score"] += score
            
            if category in self.progress_data["categories"]:
                self.progress_data["categories"][category]["completed"] += 1
            
            self._update_level()
            self._save_progress()
            return True
        return False
    
    def _update_level(self):
        """به‌روزرسانی سطح کاربر بر اساس تعداد مسائل حل شده"""
        completed_count = len(self.progress_data["completed_problems"])
        
        if completed_count < 10:
            level = "مبتدی"
        elif completed_count < 50:
            level = "ابتدایی"
        elif completed_count < 100:
            level = "متوسط"
        elif completed_count < 200:
            level = "پیشرفته"
        else:
            level = "حرفه‌ای"
        
        self.progress_data["current_level"] = level
    
    def get_progress_report(self) -> Dict:
        """تولید گزارش پیشرفت"""
        total_problems = sum(cat["total"] for cat in self.progress_data["categories"].values())
        completed_problems = len(self.progress_data["completed_problems"])
        completion_percentage = (completed_problems / total_problems) * 100
        
        return {
            "user_id": self.user_id,
            "level": self.progress_data["current_level"],
            "completed_problems": completed_problems,
            "total_problems": total_problems,
            "completion_percentage": round(completion_percentage, 2),
            "total_score": self.progress_data["total_score"],
            "categories_progress": self.progress_data["categories"],
            "recent_problems": self.progress_data["completed_problems"][-5:]
        }
    
    def get_recommendations(self) -> List[str]:
        """پیشنهاد مسائل بعدی بر اساس پیشرفت"""
        recommendations = []
        
        # بررسی هر دسته‌بندی
        for category, data in self.progress_data["categories"].items():
            if data["completed"] < data["total"]:
                next_problem = f"{category.split('_')[0].upper()}{data['completed']+1:04d}"
                recommendations.append(f"مسئله بعدی در {category}: {next_problem}")
        
        return recommendations[:3]  # فقط 3 پیشنهاد اول

def main():
    """تست ابزار ردیابی پیشرفت"""
    tracker = ProgressTracker("test_user")
    
    # تست علامت‌گذاری مسائل
    tracker.mark_completed("A0001", "A_basics", 10)
    tracker.mark_completed("A0002", "A_basics", 10)
    
    # نمایش گزارش
    report = tracker.get_progress_report()
    print("گزارش پیشرفت:")
    print(f"سطح: {report['level']}")
    print(f"مسائل حل شده: {report['completed_problems']}/{report['total_problems']}")
    print(f"درصد تکمیل: {report['completion_percentage']}%")
    print(f"امتیاز کل: {report['total_score']}")
    
    # نمایش پیشنهادات
    recommendations = tracker.get_recommendations()
    print("\nپیشنهادات:")
    for rec in recommendations:
        print(f"- {rec}")

if __name__ == "__main__":
    main()