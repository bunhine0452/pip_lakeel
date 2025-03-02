import requests
import datetime
import re
import random
import platform
import subprocess
import webbrowser
from bs4 import BeautifulSoup

# 1. 네이버 실시간 검색어 순위 확인 기능
def naver_trending():
    """네이버 실시간 검색어 순위를 반환합니다."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        url = "https://www.naver.com/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        trending_keywords = []
        elements = soup.select('.list_rank .item_title')
        
        for idx, element in enumerate(elements, 1):
            keyword = element.get_text().strip()
            trending_keywords.append(f"{idx}. {keyword}")
            if idx >= 10:  # 상위 10개만 가져오기
                break
                
        return trending_keywords
    except Exception as e:
        return [f"검색어 순위를 가져오는 중 오류 발생: {str(e)}"]

# 2. 한국 공휴일 확인 기능
def is_korean_holiday(date=None):
    """주어진 날짜가 한국 공휴일인지 확인합니다."""
    if date is None:
        date = datetime.date.today()
    elif isinstance(date, str):
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        
    # 2024년 공휴일 목록 (매년 업데이트 필요)
    holidays_2024 = {
        datetime.date(2024, 1, 1): "신정",
        datetime.date(2024, 2, 9): "설날 연휴",
        datetime.date(2024, 2, 10): "설날",
        datetime.date(2024, 2, 11): "설날 연휴",
        datetime.date(2024, 3, 1): "삼일절",
        datetime.date(2024, 4, 10): "22대 국회의원 선거",
        datetime.date(2024, 5, 5): "어린이날",
        datetime.date(2024, 5, 6): "어린이날 대체공휴일",
        datetime.date(2024, 5, 15): "부처님오신날",
        datetime.date(2024, 6, 6): "현충일",
        datetime.date(2024, 8, 15): "광복절",
        datetime.date(2024, 9, 16): "추석 연휴",
        datetime.date(2024, 9, 17): "추석",
        datetime.date(2024, 9, 18): "추석 연휴",
        datetime.date(2024, 10, 3): "개천절",
        datetime.date(2024, 10, 9): "한글날",
        datetime.date(2024, 12, 25): "크리스마스"
    }
    
    if date in holidays_2024:
        return f"{date.strftime('%Y년 %m월 %d일')}은(는) '{holidays_2024[date]}' 공휴일입니다."
    else:
        return f"{date.strftime('%Y년 %m월 %d일')}은(는) 공휴일이 아닙니다."

# 3. 한글 초성 게임 생성기
def korean_consonant_game():
    """랜덤한 한글 초성을 생성하고 해당 초성으로 시작하는 단어 예시를 제공합니다."""
    consonants = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    
    # 초성별 예시 단어
    examples = {
        'ㄱ': ['고양이', '과일', '공원', '가족', '거북이'],
        'ㄲ': ['까치', '꼬마', '꽃', '꿀', '끼니'],
        'ㄴ': ['나무', '노래', '눈', '늑대', '냄새'],
        'ㄷ': ['다리', '도시', '두부', '다람쥐', '달팽이'],
        'ㄸ': ['따옴표', '때문', '뚜껑', '띠', '떡'],
        'ㄹ': ['라디오', '로봇', '루비', '리본', '레몬'],
        'ㅁ': ['마우스', '모자', '무지개', '미소', '메아리'],
        'ㅂ': ['바다', '보물', '부엉이', '비밀', '베개'],
        'ㅃ': ['빠른', '뽀뽀', '뿌리', '삐약', '빼빼로'],
        'ㅅ': ['사과', '소나기', '수박', '시계', '세상'],
        'ㅆ': ['싸움', '쏘다', '쑥', '씨앗', '쌀'],
        'ㅇ': ['아이', '오렌지', '우산', '이슬', '에너지'],
        'ㅈ': ['자동차', '조개', '주사위', '지구', '제비'],
        'ㅉ': ['짜장면', '찌개', '쭈꾸미', '찔레', '쪽'],
        'ㅊ': ['차', '초콜릿', '추억', '치즈', '체리'],
        'ㅋ': ['카메라', '코끼리', '쿠키', '키위', '케이크'],
        'ㅌ': ['타조', '토마토', '튤립', '티셔츠', '테이블'],
        'ㅍ': ['파도', '포도', '풍선', '피아노', '페인트'],
        'ㅎ': ['하늘', '호랑이', '흙', '힘', '헬리콥터']
    }
    
    selected = random.choice(consonants)
    random_examples = random.sample(examples[selected], min(3, len(examples[selected])))
    
    return {
        "초성": selected,
        "예시 단어": random_examples,
        "게임 방법": "이 초성으로 시작하는 단어를 최대한 많이 생각해보세요!"
    }

# 4. 네이버 맞춤법 검사기 연동
def check_spelling(text):
    """네이버 맞춤법 검사기로 텍스트를 검사하는 링크를 제공합니다."""
    if not text:
        return "텍스트를 입력해주세요."
    
    encoded_text = requests.utils.quote(text)
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=맞춤법+검사기+{encoded_text}"
    
    # 브라우저에서 URL 열기
    webbrowser.open(url)
    return "네이버 맞춤법 검사기 페이지가 브라우저에서 열렸습니다."

# 5. 한국어 텍스트에서 이모티콘 추출
def extract_emoticons(text):
    """한국어 텍스트에서 이모티콘(ㅋㅋ, ㅎㅎ, ㅠㅠ 등)을 추출합니다."""
    emoticons = {
        'ㅋ': 0, 'ㅎ': 0, 'ㅠ': 0, 'ㅜ': 0, 'ㅡ': 0, '^': 0,
        'ㅇ': 0, 'ㄷ': 0, 'ㅂ': 0, 'ㅅ': 0, 'ㄱ': 0
    }
    
    patterns = {
        r'ㅋ+': 'ㅋ', r'ㅎ+': 'ㅎ', r'ㅠ+': 'ㅠ', r'ㅜ+': 'ㅜ',
        r'ㅡ+': 'ㅡ', r'\^+': '^', r'ㅇ_ㅇ': 'ㅇ', r'ㄷㄷ': 'ㄷ',
        r'ㅂㅂ': 'ㅂ', r'ㅅㅅ': 'ㅅ', r'ㄱㄱ': 'ㄱ'
    }
    
    for pattern, key in patterns.items():
        emoticons[key] += len(re.findall(pattern, text))
    
    result = []
    for emoticon, count in emoticons.items():
        if count > 0:
            if emoticon in ['ㅋ', 'ㅎ']:
                result.append(f"{emoticon * min(count, 5)}: {count}회")
            else:
                result.append(f"{emoticon}: {count}회")
    
    if not result:
        return "이모티콘이 발견되지 않았습니다."
    return result

# 6. 한글 자음/모음 통계
def korean_char_stats(text):
    """한글 텍스트의 자음/모음 통계를 분석합니다."""
    # 한글 자음 모음 정의
    consonants = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    vowels = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    
    # 자음/모음 카운트 초기화
    consonant_count = {c: 0 for c in consonants}
    vowel_count = {v: 0 for v in vowels}
    
    for char in text:
        if '가' <= char <= '힣':  # 한글 범위 확인
            # 한글 유니코드 분해
            char_code = ord(char) - ord('가')
            
            # 초성, 중성, 종성 분리
            initial = char_code // (21 * 28)
            medial = (char_code % (21 * 28)) // 28
            final = char_code % 28
            
            # 초성 카운트
            if 0 <= initial < len(consonants):
                consonant_count[consonants[initial]] += 1
                
            # 중성 카운트
            if 0 <= medial < len(vowels):
                vowel_count[vowels[medial]] += 1
                
            # 종성 카운트 (종성이 있는 경우)
            if final > 0 and final <= len(consonants):
                # 종성에는 자음이 없는 경우(0)도 있으므로 주의
                consonant_count[consonants[final-1]] += 1
    
    # 결과 정리
    result = {
        "자음 통계": {c: count for c, count in consonant_count.items() if count > 0},
        "모음 통계": {v: count for v, count in vowel_count.items() if count > 0},
        "가장 많이 사용된 자음": max(consonant_count.items(), key=lambda x: x[1]) if any(consonant_count.values()) else None,
        "가장 많이 사용된 모음": max(vowel_count.items(), key=lambda x: x[1]) if any(vowel_count.values()) else None
    }
    
    return result 