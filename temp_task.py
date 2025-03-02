import os
import re
import platform
import sys
import subprocess
from datetime import datetime
import unicodedata
from urllib.request import urlopen
import json
import calendar
import warnings

# 한영 자판 변환 매핑
KO_EN_MAPPING = {
    'ㅂ': 'q', 'ㅈ': 'w', 'ㄷ': 'e', 'ㄱ': 'r', 'ㅅ': 't', 'ㅛ': 'y', 'ㅕ': 'u', 'ㅑ': 'i', 'ㅐ': 'o', 'ㅔ': 'p',
    'ㅁ': 'a', 'ㄴ': 's', 'ㅇ': 'd', 'ㄹ': 'f', 'ㅎ': 'g', 'ㅗ': 'h', 'ㅓ': 'j', 'ㅏ': 'k', 'ㅣ': 'l',
    'ㅋ': 'z', 'ㅌ': 'x', 'ㅊ': 'c', 'ㅍ': 'v', 'ㅠ': 'b', 'ㅜ': 'n', 'ㅡ': 'm'
}

EN_KO_MAPPING = {v: k for k, v in KO_EN_MAPPING.items()}

# 문제 없음! 메시지와 귀여운 고양이 텍스트 이모티콘 출력 함수
def jaebal():
    """
    귀여운 고양이 텍스트 이모티콘과 함께 '문제 없음!' 메시지를 출력합니다.
    '제발'의 의미처럼 코드가 제발 잘 실행되길 바라는 마음으로 사용합니다.
    """
    cat_emoticons = [
        r"""
        /\_/\  
       ( o.o ) 👍 문제 없음!
        > ^ <
        """,
        
        r"""
         /\__/\  
        (=^.^=) 👍 문제 없음!
         )   (  
        (__)__)
        """,
        
        r"""
        ∧,,,∧
       (= ･ω･)  👍 문제 없음!
        ∪  ∪
        """,
        
        r"""
        ฅ^•ﻌ•^ฅ  👍 문제 없음!
        """
    ]
    
    import random
    print(random.choice(cat_emoticons))
    return True

class KoreanTextUtils:
    """한국어 텍스트 처리 유틸리티"""
    
    @staticmethod
    def split_syllable(char):
        """한글 음절을 초성, 중성, 종성으로 분리"""
        if not '가' <= char <= '힣':
            return char
        
        char_code = ord(char) - ord('가')
        
        cho = char_code // (21 * 28)
        jung = (char_code % (21 * 28)) // 28
        jong = char_code % 28
        
        CHO = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        JUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        JONG = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        
        return (CHO[cho], JUNG[jung], JONG[jong])
    
    @staticmethod
    def join_syllable(cho, jung, jong):
        """초성, 중성, 종성을 합쳐 한글 음절로 변환"""
        CHO = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        JUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        JONG = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        
        try:
            cho_idx = CHO.index(cho)
            jung_idx = JUNG.index(jung)
            jong_idx = JONG.index(jong) if jong else 0
            
            char_code = cho_idx * 21 * 28 + jung_idx * 28 + jong_idx + ord('가')
            return chr(char_code)
        except ValueError:
            return cho + jung + jong
    
    @staticmethod
    def text_to_jamo(text):
        """텍스트의 모든 한글 문자를 자모로 분리"""
        result = []
        for char in text:
            if '가' <= char <= '힣':
                result.extend(KoreanTextUtils.split_syllable(char))
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def normalize_korean(text):
        """한글 자소 정규화 (예: ㅅㅣㄴㅏㄹ -> 시날)"""
        if not text:
            return ""
        
        # NFC 정규화 (결합된 문자를 단일 문자로)
        return unicodedata.normalize('NFC', text)
    
    @staticmethod
    def fix_ko_en_typo(text):
        """한영 자판 오타 수정 (한글 자판으로 영어 입력했을때)"""
        result = []
        for char in text:
            if char in EN_KO_MAPPING:
                result.append(EN_KO_MAPPING[char])
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def fix_en_ko_typo(text):
        """영한 자판 오타 수정 (영어 자판으로 한글 입력했을때)"""
        result = []
        for char in text:
            if char in KO_EN_MAPPING:
                result.append(KO_EN_MAPPING[char])
            else:
                result.append(char)
        return ''.join(result)


class KoreanDateTime:
    """한국 날짜/시간 처리 클래스"""
    
    @staticmethod
    def get_korean_date(date=None):
        """날짜를 한국식으로 표기 (yyyy년 mm월 dd일)"""
        if date is None:
            date = datetime.now()
        return f"{date.year}년 {date.month}월 {date.day}일"
    
    @staticmethod
    def get_korean_time(time=None):
        """시간을 한국식으로 표기"""
        if time is None:
            time = datetime.now()
            
        hour = time.hour
        am_pm = "오전" if hour < 12 else "오후"
        
        if hour > 12:
            hour -= 12
            
        return f"{am_pm} {hour}시 {time.minute}분 {time.second}초"


class KoreanDataFormat:
    """한국식 데이터 포맷 클래스"""
    
    @staticmethod
    def format_number(number):
        """숫자를 한국식으로 천 단위 쉼표 포맷팅"""
        if isinstance(number, int) or isinstance(number, float):
            return '{:,}'.format(number)
        return number
    
    @staticmethod
    def format_currency(amount, symbol='₩'):
        """금액을 원화 표시와 함께 포맷팅"""
        formatted = KoreanDataFormat.format_number(amount)
        return f"{symbol}{formatted}"
    
    @staticmethod
    def format_percent(value, decimal_places=2):
        """비율을 백분율로 변환 (소수점 이하 자릿수 지정)"""
        if isinstance(value, (int, float)):
            return f"{value:.{decimal_places}f}%"
        return value


class KoreanFilePath:
    """한글 경로 및 파일명 처리 클래스"""
    
    @staticmethod
    def safe_path(path):
        """한글 경로를 안전하게 처리"""
        return os.path.normpath(path)
    
    @staticmethod
    def ensure_dir(directory):
        """디렉토리가 존재하지 않으면 생성"""
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory
    
    @staticmethod
    def get_safe_filename(filename):
        """안전한 파일명으로 변환 (특수문자 제거)"""
        # 윈도우에서 사용할 수 없는 문자: \ / : * ? " < > |
        return re.sub(r'[\\/*?:"<>|]', "_", filename)


class KoreanVisualization:
    """한국어 시각화 도우미 클래스"""
    
    @staticmethod
    def setup_korean_font():
        """한국어 폰트 설정 (lakeel.sfo()의 확장 버전)"""
        try:
            import matplotlib.pyplot as plt
            from matplotlib import font_manager, rc
            
            current_os = platform.system()
            
            if current_os == 'Darwin':  # macOS
                font_list = ['AppleGothic', 'Malgun Gothic', 'NanumGothic', 'NanumBarunGothic']
                found = False
                
                for font in font_list:
                    try:
                        rc('font', family=font)
                        print(f"폰트가 {font}로 설정되었습니다.")
                        found = True
                        break
                    except:
                        continue
                
                if not found:
                    print("한글 폰트를 찾을 수 없습니다. 폰트를 설치해주세요.")
                    
            elif current_os == 'Windows':
                font_path = 'C:/Windows/Fonts/malgun.ttf'
                font_name = font_manager.FontProperties(fname=font_path).get_name()
                rc('font', family=font_name)
                print("폰트가 Malgun Gothic으로 설정되었습니다.")
                
            elif current_os == 'Linux':
                # 리눅스의 경우 나눔글꼴 설치 필요
                try:
                    font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
                    font_name = font_manager.FontProperties(fname=font_path).get_name()
                    rc('font', family=font_name)
                    print("폰트가 NanumGothic으로 설정되었습니다.")
                except:
                    print("리눅스에서 한글 폰트를 설정할 수 없습니다. 나눔글꼴을 설치해주세요.")
                    print("sudo apt-get install fonts-nanum")
            
            # 음수 부호 깨짐 방지
            plt.rcParams['axes.unicode_minus'] = False
            
            return True
        except ImportError:
            print("matplotlib이 설치되어 있지 않습니다.")
            print("pip install matplotlib 명령으로 설치할 수 있습니다.")
            return False
            
    @staticmethod
    def make_korean_heatmap(data):
        """한글 지원 히트맵 생성"""
        try:
            import numpy as np
            import seaborn as sns
            import matplotlib.pyplot as plt
            
            # 한글 폰트 설정
            KoreanVisualization.setup_korean_font()
            
            # 히트맵 생성
            plt.figure(figsize=(10, 8))
            sns.heatmap(data, annot=True, cmap='RdYlBu_r', fmt='.2f')
            
            print("히트맵이 생성되었습니다. plt.show()로 표시해주세요.")
            return plt
        except ImportError:
            print("필요한 패키지가 설치되어 있지 않습니다.")
            print("pip install numpy seaborn matplotlib 명령으로 설치할 수 있습니다.")
            return None


# 테스트 함수들
def test_korean_text():
    text_utils = KoreanTextUtils()
    
    # 자모 분리 테스트
    print("== 자모 분리 테스트 ==")
    example = "안녕하세요"
    jamo = text_utils.text_to_jamo(example)
    print(f"원본: {example}")
    print(f"자모 분리: {jamo}")
    
    # 한영 오타 변환 테스트
    print("\n== 한영 오타 변환 테스트 ==")
    ko_typed_as_en = "dkssud"  # 한글 자판으로 영어처럼 친 "안녕"
    fixed = text_utils.fix_ko_en_typo(ko_typed_as_en)
    print(f"오타: {ko_typed_as_en}")
    print(f"수정: {fixed}")

def test_korean_datetime():
    dt = KoreanDateTime()
    
    print("== 한국 날짜/시간 테스트 ==")
    print(f"한국식 날짜: {dt.get_korean_date()}")
    print(f"한국식 시간: {dt.get_korean_time()}")

def test_korean_format():
    fmt = KoreanDataFormat()
    
    print("== 한국식 데이터 포맷 테스트 ==")
    number = 1234567890
    print(f"숫자 포맷: {fmt.format_number(number)}")
    print(f"통화 포맷: {fmt.format_currency(number)}")
    print(f"백분율 포맷: {fmt.format_percent(0.7625)}")

def test_filepath():
    fp = KoreanFilePath()
    
    print("== 한글 파일경로 테스트 ==")
    filename = "테스트:파일?.txt"
    safe_name = fp.get_safe_filename(filename)
    print(f"원본 파일명: {filename}")
    print(f"안전한 파일명: {safe_name}")

def run_all_tests():
    """모든 테스트 실행"""
    print("===== 한국인을 위한 파이썬 편의 기능 테스트 =====\n")
    
    test_korean_text()
    print("\n" + "-"*50 + "\n")
    
    test_korean_datetime()
    print("\n" + "-"*50 + "\n")
    
    test_korean_format()
    print("\n" + "-"*50 + "\n")
    
    test_filepath()
    print("\n" + "-"*50 + "\n")
    
    print("테스트 완료!")
    
    # 귀여운 고양이 이모티콘과 함께 "문제 없음!" 메시지 출력
    jaebal()

# 메인 실행
if __name__ == "__main__":
    run_all_tests()
