#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اسکریپت اصلی برای استفاده از ابزارهای PythonSaveh
"""

import sys
import os
import argparse
from datetime import datetime

# اضافه کردن مسیر پروژه به sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import (
    ProgressTracker,
    DifficultyAnalyzer,
    AnswerChecker,
    HintSystem,
    ReportGenerator
)

def main():
    """تابع اصلی"""
    parser = argparse.ArgumentParser(description='ابزارهای کمکی PythonSaveh')
    parser.add_argument('command', choices=[
        'progress', 'analyze', 'check', 'hint', 'report'
    ], help='دستور مورد نظر')
    
    parser.add_argument('--user', default='default', help='شناسه کاربر')
    parser.add_argument('--problem', help='شناسه مسئله')
    parser.add_argument('--directory', default='.', help='مسیر دایرکتوری')
    parser.add_argument('--type', default='daily', help='نوع گزارش')
    parser.add_argument('--level', type=int, default=1, help='سطح راهنمایی')
    
    args = parser.parse_args()
    
    try:
        if args.command == 'progress':
            handle_progress_command(args)
        elif args.command == 'analyze':
            handle_analyze_command(args)
        elif args.command == 'check':
            handle_check_command(args)
        elif args.command == 'hint':
            handle_hint_command(args)
        elif args.command == 'report':
            handle_report_command(args)
    
    except Exception as e:
        print(f"خطا: {e}")
        sys.exit(1)

def handle_progress_command(args):
    """مدیریت دستور پیشرفت"""
    tracker = ProgressTracker(args.user)
    
    if args.problem:
        # علامت‌گذاری مسئله به عنوان تکمیل شده
        category = args.problem[0] + "_basics"  # فرض: A_basics
        success = tracker.mark_completed(args.problem, category)
        
        if success:
            print(f"✅ مسئله {args.problem} به عنوان تکمیل شده علامت‌گذاری شد")
        else:
            print(f"⚠️ مسئله {args.problem} قبلاً تکمیل شده بود")
    
    # نمایش گزارش پیشرفت
    report = tracker.get_progress_report()
    print(f"\n📊 گزارش پیشرفت کاربر {args.user}:")
    print(f"سطح: {report['level']}")
    print(f"مسائل حل شده: {report['completed_problems']}/{report['total_problems']}")
    print(f"درصد تکمیل: {report['completion_percentage']}%")
    print(f"امتیاز کل: {report['total_score']}")
    
    # نمایش پیشنهادات
    recommendations = tracker.get_recommendations()
    if recommendations:
        print("\n💡 پیشنهادات:")
        for rec in recommendations:
            print(f"  - {rec}")

def handle_analyze_command(args):
    """مدیریت دستور تحلیل"""
    analyzer = DifficultyAnalyzer()
    
    if os.path.isfile(args.directory):
        # تحلیل یک فایل
        problem_info = analyzer.analyze_problem_file(args.directory)
        if problem_info:
            print(f"📋 تحلیل مسئله {problem_info.id}:")
            print(f"عنوان: {problem_info.title}")
            print(f"سختی: {problem_info.difficulty}/6")
            print(f"دسته‌بندی: {problem_info.category}")
            print(f"زمان تخمینی: {problem_info.estimated_time} دقیقه")
            print(f"مفاهیم: {', '.join(problem_info.concepts)}")
    else:
        # تحلیل دایرکتوری
        problems = analyzer.analyze_directory(args.directory)
        report = analyzer.generate_difficulty_report(problems)
        
        print(f"📊 گزارش تحلیل دایرکتوری {args.directory}:")
        print(f"تعداد کل مسائل: {report['total_problems']}")
        print(f"میانگین سختی: {report['average_difficulty']}")
        print(f"زمان تخمینی کل: {report['estimated_total_time']}")
        
        print("\nتوزیع سختی:")
        for difficulty, count in report['difficulty_distribution'].items():
            print(f"  {difficulty}: {count} مسئله")

def handle_check_command(args):
    """مدیریت دستور بررسی"""
    checker = AnswerChecker()
    
    if args.problem and os.path.exists(f"{args.directory}/{args.problem}.py"):
        # بررسی یک مسئله خاص
        problem_path = f"{args.directory}/{args.problem}.py"
        test_cases = checker.generate_test_cases(args.problem)
        result = checker.check_problem_solution(problem_path, test_cases)
        
        print(f"🔍 نتیجه بررسی {args.problem}:")
        print(f"وضعیت: {'✅ موفق' if result.passed else '❌ ناموفق'}")
        print(f"امتیاز: {result.score}")
        print(f"زمان اجرا: {result.execution_time:.3f} ثانیه")
        
        if result.error_message:
            print(f"خطا: {result.error_message}")
    else:
        # بررسی دسته‌ای
        results = checker.batch_check_directory(args.directory)
        report = checker.generate_report(results)
        
        print(f"📊 گزارش بررسی دایرکتوری {args.directory}:")
        print(f"کل مسائل: {report['total_problems']}")
        print(f"موفق: {report['passed_problems']}")
        print(f"ناموفق: {report['failed_problems']}")
        print(f"نرخ موفقیت: {report['success_rate']}%")
        
        if report['failed_problem_details']:
            print("\nمسائل ناموفق:")
            for detail in report['failed_problem_details'][:5]:  # فقط 5 مورد اول
                print(f"  - {detail['problem_id']}: {detail['error']}")

def handle_hint_command(args):
    """مدیریت دستور راهنمایی"""
    hint_system = HintSystem()
    
    if not args.problem:
        print("لطفاً شناسه مسئله را مشخص کنید (--problem)")
        return
    
    # خواندن محتوای مسئله
    problem_path = f"{args.directory}/{args.problem}.py"
    if os.path.exists(problem_path):
        with open(problem_path, 'r', encoding='utf-8') as f:
            problem_content = f.read()
    else:
        problem_content = ""
    
    # دریافت راهنمایی
    hints = hint_system.get_problem_hints(args.problem, problem_content, args.level)
    
    print(f"💡 راهنمایی برای مسئله {args.problem}:")
    for i, hint in enumerate(hints, 1):
        print(f"{i}. (سطح {hint.level}) {hint.text}")
        if hint.code_example:
            print(f"   مثال: {hint.code_example}")

def handle_report_command(args):
    """مدیریت دستور گزارش"""
    generator = ReportGenerator()
    
    report = generator.generate_report(args.type, args.user)
    print(report)
    
    # ذخیره گزارش در فایل
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{args.type}_report_{args.user}_{timestamp}.md"
    generator.save_report_to_file(report, filename)

if __name__ == "__main__":
    main()