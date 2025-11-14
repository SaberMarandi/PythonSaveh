#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ابزار تولید گزارش‌های جامع برای پروژه PythonSaveh
"""

import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass

@dataclass
class ReportData:
    """داده‌های گزارش"""
    user_id: str
    report_date: str
    total_problems: int
    completed_problems: int
    completion_rate: float
    time_spent: int  # دقیقه
    categories: Dict[str, Dict]
    recent_activity: List[Dict]

class ReportGenerator:
    """کلاس تولید گزارش‌های مختلف"""
    
    def __init__(self):
        self.report_templates = {
            'daily': self._generate_daily_report,
            'weekly': self._generate_weekly_report,
            'monthly': self._generate_monthly_report,
            'progress': self._generate_progress_report,
            'performance': self._generate_performance_report
        }
    
    def generate_report(self, report_type: str, user_id: str = "default", **kwargs) -> str:
        """تولید گزارش بر اساس نوع"""
        if report_type in self.report_templates:
            return self.report_templates[report_type](user_id, **kwargs)
        else:
            return "نوع گزارش نامعتبر است"
    
    def _generate_daily_report(self, user_id: str, **kwargs) -> str:
        """تولید گزارش روزانه"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        # بارگذاری داده‌های پیشرفت
        progress_data = self._load_progress_data(user_id)
        if not progress_data:
            return "داده‌ای برای تولید گزارش یافت نشد"
        
        # محاسبه آمار روزانه
        daily_stats = self._calculate_daily_stats(progress_data)
        
        report = f"""
# 📊 گزارش روزانه - {today}

## 👤 کاربر: {user_id}

### 📈 آمار امروز
- **مسائل حل شده امروز**: {daily_stats['problems_solved_today']}
- **زمان مطالعه**: {daily_stats['study_time_today']} دقیقه
- **امتیاز کسب شده**: {daily_stats['points_earned_today']}
- **سطح فعلی**: {progress_data.get('current_level', 'نامشخص')}

### 🎯 پیشرفت کلی
- **کل مسائل حل شده**: {len(progress_data.get('completed_problems', []))}
- **درصد تکمیل**: {daily_stats['completion_percentage']:.1f}%
- **امتیاز کل**: {progress_data.get('total_score', 0)}

### 📚 فعالیت در دسته‌بندی‌ها
"""
        
        # اضافه کردن آمار دسته‌بندی‌ها
        categories = progress_data.get('categories', {})
        for category, data in categories.items():
            completed = data.get('completed', 0)
            total = data.get('total', 0)
            percentage = (completed / total * 100) if total > 0 else 0
            
            report += f"- **{category}**: {completed}/{total} ({percentage:.1f}%)\n"
        
        # پیشنهادات
        report += f"""
### 💡 پیشنهادات برای فردا
{self._generate_recommendations(progress_data)}

### 🏆 دستاوردهای امروز
{self._generate_achievements(daily_stats)}

---
*گزارش تولید شده در: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""
        
        return report
    
    def _generate_weekly_report(self, user_id: str, **kwargs) -> str:
        """تولید گزارش هفتگی"""
        week_start = datetime.now() - timedelta(days=7)
        week_end = datetime.now()
        
        progress_data = self._load_progress_data(user_id)
        if not progress_data:
            return "داده‌ای برای تولید گزارش یافت نشد"
        
        weekly_stats = self._calculate_weekly_stats(progress_data)
        
        report = f"""
# 📊 گزارش هفتگی
## 📅 {week_start.strftime("%Y-%m-%d")} تا {week_end.strftime("%Y-%m-%d")}

### 📈 خلاصه هفته
- **مسائل حل شده**: {weekly_stats['problems_solved']}
- **ساعات مطالعه**: {weekly_stats['study_hours']:.1f} ساعت
- **میانگین روزانه**: {weekly_stats['daily_average']:.1f} مسئله
- **بهترین روز**: {weekly_stats['best_day']}

### 📊 نمودار پیشرفت هفتگی
```
{self._generate_ascii_chart(weekly_stats['daily_progress'])}
```

### 🎯 اهداف هفته آینده
- حل {weekly_stats['next_week_target']} مسئله
- تمرکز بر دسته‌بندی: {weekly_stats['focus_category']}
- بهبود در: {weekly_stats['improvement_area']}

### 🏅 رتبه‌بندی
- **رتبه کلی**: {weekly_stats['overall_rank']}
- **رتبه در دسته سنی**: {weekly_stats['age_group_rank']}
- **پیشرفت نسبت به هفته قبل**: {weekly_stats['progress_change']}

---
*تولید شده توسط سیستم گزارش‌گیری PythonSaveh*
"""
        
        return report
    
    def _generate_progress_report(self, user_id: str, **kwargs) -> str:
        """تولید گزارش پیشرفت جامع"""
        progress_data = self._load_progress_data(user_id)
        if not progress_data:
            return "داده‌ای برای تولید گزارش یافت نشد"
        
        start_date = progress_data.get('start_date', 'نامشخص')
        total_days = self._calculate_days_since_start(start_date)
        
        report = f"""
# 🚀 گزارش پیشرفت جامع

## 👤 پروفایل کاربر
- **شناسه**: {user_id}
- **تاریخ شروع**: {start_date}
- **روزهای فعالیت**: {total_days} روز
- **سطح فعلی**: {progress_data.get('current_level', 'نامشخص')}

## 📊 آمار کلی
- **کل مسائل**: {self._get_total_problems()}
- **مسائل حل شده**: {len(progress_data.get('completed_problems', []))}
- **درصد تکمیل**: {self._calculate_completion_rate(progress_data):.1f}%
- **امتیاز کل**: {progress_data.get('total_score', 0)}

## 📈 پیشرفت در دسته‌بندی‌ها
"""
        
        # نمودار پیشرفت دسته‌بندی‌ها
        categories = progress_data.get('categories', {})
        for category, data in categories.items():
            completed = data.get('completed', 0)
            total = data.get('total', 0)
            percentage = (completed / total * 100) if total > 0 else 0
            
            # نمودار نواری ASCII
            bar_length = int(percentage / 5)  # هر 5% یک کاراکتر
            bar = "█" * bar_length + "░" * (20 - bar_length)
            
            report += f"""
### {category}
{bar} {percentage:.1f}% ({completed}/{total})
"""
        
        # تحلیل نقاط قوت و ضعف
        report += f"""
## 💪 نقاط قوت
{self._analyze_strengths(progress_data)}

## 🎯 نقاط قابل بهبود
{self._analyze_weaknesses(progress_data)}

## 📅 برنامه پیشنهادی
{self._suggest_study_plan(progress_data)}

## 🏆 دستاوردها
{self._list_achievements(progress_data)}

---
*آخرین به‌روزرسانی: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""
        
        return report
    
    def _generate_performance_report(self, user_id: str, **kwargs) -> str:
        """تولید گزارش عملکرد"""
        progress_data = self._load_progress_data(user_id)
        if not progress_data:
            return "داده‌ای برای تولید گزارش یافت نشد"
        
        performance_metrics = self._calculate_performance_metrics(progress_data)
        
        report = f"""
# ⚡ گزارش عملکرد

## 🎯 شاخص‌های کلیدی عملکرد (KPI)
- **نرخ موفقیت**: {performance_metrics['success_rate']:.1f}%
- **سرعت حل مسئله**: {performance_metrics['solving_speed']:.1f} مسئله/روز
- **کیفیت راه‌حل**: {performance_metrics['solution_quality']:.1f}/10
- **پایداری یادگیری**: {performance_metrics['consistency']:.1f}/10

## 📊 تحلیل عملکرد بر اساس سختی
- **مسائل آسان**: {performance_metrics['easy_success']}% موفقیت
- **مسائل متوسط**: {performance_metrics['medium_success']}% موفقیت  
- **مسائل سخت**: {performance_metrics['hard_success']}% موفقیت

## ⏱️ تحلیل زمانی
- **بهترین ساعت یادگیری**: {performance_metrics['best_hour']}
- **میانگین زمان حل مسئله**: {performance_metrics['avg_solve_time']} دقیقه
- **روزهای پرتلاش**: {', '.join(performance_metrics['productive_days'])}

## 🎨 الگوی یادگیری
- **سبک یادگیری**: {performance_metrics['learning_style']}
- **ترجیح موضوعی**: {performance_metrics['topic_preference']}
- **نقاط قوت**: {', '.join(performance_metrics['strengths'])}

## 📈 پیش‌بینی پیشرفت
- **زمان تخمینی تکمیل**: {performance_metrics['estimated_completion']} روز
- **مسائل قابل حل در هفته آینده**: {performance_metrics['next_week_prediction']}
- **احتمال رسیدن به سطح بعد**: {performance_metrics['level_up_probability']}%

---
*تحلیل انجام شده توسط موتور هوش مصنوعی PythonSaveh*
"""
        
        return report
    
    def _load_progress_data(self, user_id: str) -> Optional[Dict]:
        """بارگذاری داده‌های پیشرفت کاربر"""
        progress_file = f"data/progress_{user_id}.json"
        if os.path.exists(progress_file):
            with open(progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    def _calculate_daily_stats(self, progress_data: Dict) -> Dict:
        """محاسبه آمار روزانه"""
        # این تابع باید با داده‌های واقعی پیاده‌سازی شود
        return {
            'problems_solved_today': 3,
            'study_time_today': 45,
            'points_earned_today': 30,
            'completion_percentage': 25.5
        }
    
    def _generate_recommendations(self, progress_data: Dict) -> str:
        """تولید پیشنهادات"""
        recommendations = [
            "تمرکز بر مسائل ساختار داده",
            "مرور مفاهیم حلقه‌ها",
            "تمرین بیشتر روی الگوریتم‌های مرتب‌سازی"
        ]
        return '\n'.join(f"- {rec}" for rec in recommendations)
    
    def _generate_achievements(self, daily_stats: Dict) -> str:
        """تولید دستاوردها"""
        achievements = []
        if daily_stats['problems_solved_today'] >= 5:
            achievements.append("🏆 حل بیش از 5 مسئله در یک روز")
        if daily_stats['study_time_today'] >= 60:
            achievements.append("⏰ بیش از یک ساعت مطالعه")
        
        return '\n'.join(f"- {achievement}" for achievement in achievements) if achievements else "- هنوز دستاوردی کسب نشده"
    
    def save_report_to_file(self, report: str, filename: str):
        """ذخیره گزارش در فایل"""
        os.makedirs("reports", exist_ok=True)
        filepath = os.path.join("reports", filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"گزارش در {filepath} ذخیره شد")

def main():
    """تست تولیدکننده گزارش"""
    generator = ReportGenerator()
    
    # تولید گزارش روزانه
    daily_report = generator.generate_report('daily', 'test_user')
    print("گزارش روزانه:")
    print(daily_report[:500] + "...")
    
    # ذخیره گزارش
    generator.save_report_to_file(daily_report, f"daily_report_{datetime.now().strftime('%Y%m%d')}.md")

if __name__ == "__main__":
    main()