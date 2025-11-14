#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ابزار بررسی خودکار پاسخ‌های مسائل در پروژه PythonSaveh
"""

import os
import sys
import subprocess
import tempfile
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import time

@dataclass
class TestResult:
    """نتیجه تست یک مسئله"""
    problem_id: str
    passed: bool
    score: int
    execution_time: float
    memory_usage: int
    error_message: Optional[str] = None
    output: Optional[str] = None

class AnswerChecker:
    """کلاس بررسی خودکار پاسخ‌ها"""
    
    def __init__(self):
        self.timeout = 5  # 5 ثانیه timeout
        self.max_memory = 128 * 1024 * 1024  # 128MB حداکثر حافظه
    
    def run_code_safely(self, code: str, inputs: List[str] = None) -> Tuple[bool, str, float]:
        """اجرای ایمن کد پایتون"""
        try:
            # ایجاد فایل موقت
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(code)
                temp_file = f.name
            
            # آماده‌سازی ورودی
            input_data = '\n'.join(inputs) if inputs else ''
            
            # اجرای کد
            start_time = time.time()
            result = subprocess.run(
                [sys.executable, temp_file],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                encoding='utf-8'
            )
            execution_time = time.time() - start_time
            
            # پاک کردن فایل موقت
            os.unlink(temp_file)
            
            if result.returncode == 0:
                return True, result.stdout.strip(), execution_time
            else:
                return False, result.stderr.strip(), execution_time
                
        except subprocess.TimeoutExpired:
            return False, "خطا: زمان اجرا بیش از حد مجاز", self.timeout
        except Exception as e:
            return False, f"خطا در اجرا: {str(e)}", 0
    
    def check_problem_solution(self, problem_path: str, test_cases: List[Dict]) -> TestResult:
        """بررسی راه‌حل یک مسئله"""
        try:
            # خواندن کد راه‌حل
            with open(problem_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            problem_id = os.path.basename(problem_path).replace('.py', '')
            total_score = 0
            max_score = len(test_cases) * 10
            all_passed = True
            error_messages = []
            
            for i, test_case in enumerate(test_cases):
                inputs = test_case.get('inputs', [])
                expected_output = test_case.get('expected_output', '')
                
                success, output, exec_time = self.run_code_safely(code, inputs)
                
                if success:
                    if self._compare_outputs(output, expected_output):
                        total_score += 10
                    else:
                        all_passed = False
                        error_messages.append(f"تست {i+1}: خروجی نادرست")
                else:
                    all_passed = False
                    error_messages.append(f"تست {i+1}: {output}")
            
            return TestResult(
                problem_id=problem_id,
                passed=all_passed,
                score=total_score,
                execution_time=exec_time,
                memory_usage=0,  # فعلاً پیاده‌سازی نشده
                error_message='; '.join(error_messages) if error_messages else None,
                output=output if success else None
            )
            
        except Exception as e:
            return TestResult(
                problem_id=problem_id,
                passed=False,
                score=0,
                execution_time=0,
                memory_usage=0,
                error_message=f"خطا در بررسی: {str(e)}"
            )
    
    def _compare_outputs(self, actual: str, expected: str) -> bool:
        """مقایسه خروجی واقعی با خروجی مورد انتظار"""
        # حذف فاصله‌های اضافی و مقایسه
        actual_clean = actual.strip().replace('\r\n', '\n')
        expected_clean = expected.strip().replace('\r\n', '\n')
        
        # مقایسه دقیق
        if actual_clean == expected_clean:
            return True
        
        # مقایسه عددی (برای مسائل ریاضی)
        try:
            actual_num = float(actual_clean)
            expected_num = float(expected_clean)
            return abs(actual_num - expected_num) < 1e-6
        except ValueError:
            pass
        
        # مقایسه خط به خط
        actual_lines = actual_clean.split('\n')
        expected_lines = expected_clean.split('\n')
        
        if len(actual_lines) != len(expected_lines):
            return False
        
        for actual_line, expected_line in zip(actual_lines, expected_lines):
            if actual_line.strip() != expected_line.strip():
                return False
        
        return True
    
    def generate_test_cases(self, problem_id: str) -> List[Dict]:
        """تولید تست‌کیس‌های خودکار برای مسائل مختلف"""
        test_cases = []
        
        # تست‌کیس‌های پایه بر اساس نوع مسئله
        if 'A0001' in problem_id:  # Hello World
            test_cases = [
                {'inputs': [], 'expected_output': 'Hello, World!'}
            ]
        elif 'A0002' in problem_id:  # جمع دو عدد
            test_cases = [
                {'inputs': ['5', '3'], 'expected_output': '8'},
                {'inputs': ['10', '20'], 'expected_output': '30'},
                {'inputs': ['-5', '3'], 'expected_output': '-2'}
            ]
        elif 'A0003' in problem_id:  # تفریق دو عدد
            test_cases = [
                {'inputs': ['10', '3'], 'expected_output': '7'},
                {'inputs': ['5', '8'], 'expected_output': '-3'},
                {'inputs': ['0', '0'], 'expected_output': '0'}
            ]
        elif 'A0012' in problem_id:  # زوج یا فرد
            test_cases = [
                {'inputs': ['4'], 'expected_output': 'زوج'},
                {'inputs': ['7'], 'expected_output': 'فرد'},
                {'inputs': ['0'], 'expected_output': 'زوج'}
            ]
        else:
            # تست‌کیس عمومی
            test_cases = [
                {'inputs': ['1'], 'expected_output': '1'}
            ]
        
        return test_cases
    
    def batch_check_directory(self, directory: str) -> List[TestResult]:
        """بررسی دسته‌ای تمام مسائل در یک دایرکتوری"""
        results = []
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.py') and file.startswith('A'):
                    file_path = os.path.join(root, file)
                    problem_id = file.replace('.py', '')
                    
                    test_cases = self.generate_test_cases(problem_id)
                    result = self.check_problem_solution(file_path, test_cases)
                    results.append(result)
        
        return results
    
    def generate_report(self, results: List[TestResult]) -> Dict:
        """تولید گزارش نتایج بررسی"""
        total_problems = len(results)
        passed_problems = sum(1 for r in results if r.passed)
        total_score = sum(r.score for r in results)
        max_possible_score = total_problems * 30  # فرض 3 تست برای هر مسئله
        
        failed_problems = [r for r in results if not r.passed]
        
        return {
            "total_problems": total_problems,
            "passed_problems": passed_problems,
            "failed_problems": len(failed_problems),
            "success_rate": round((passed_problems / total_problems) * 100, 2) if total_problems > 0 else 0,
            "total_score": total_score,
            "max_score": max_possible_score,
            "score_percentage": round((total_score / max_possible_score) * 100, 2) if max_possible_score > 0 else 0,
            "failed_problem_details": [
                {
                    "problem_id": r.problem_id,
                    "error": r.error_message,
                    "score": r.score
                } for r in failed_problems
            ]
        }

def main():
    """تست ابزار بررسی پاسخ‌ها"""
    checker = AnswerChecker()
    
    # تست یک کد ساده
    test_code = """
print("Hello, World!")
"""
    
    success, output, exec_time = checker.run_code_safely(test_code)
    print(f"نتیجه تست: {'موفق' if success else 'ناموفق'}")
    print(f"خروجی: {output}")
    print(f"زمان اجرا: {exec_time:.3f} ثانیه")
    
    # تست تولید تست‌کیس
    test_cases = checker.generate_test_cases("A0001")
    print(f"\nتست‌کیس‌های A0001: {test_cases}")

if __name__ == "__main__":
    main()