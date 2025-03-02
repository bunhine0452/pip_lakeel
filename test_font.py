#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
한국어 폰트 설정 및 시각화 테스트
================================

이 파일은 temp_task.py의 KoreanVisualization 클래스에 있는 
setup_korean_font 기능을 테스트하기 위한 예제 코드입니다.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from temp_task import KoreanVisualization, jaebal

# 필요한 패키지 확인 및 설치
def check_dependencies():
    try:
        import matplotlib
        import seaborn
        import numpy
        import pandas
        print("모든 필요한 패키지가 설치되어 있습니다.")
        return True
    except ImportError as e:
        print(f"필요한 패키지가 설치되어 있지 않습니다: {e}")
        print("다음 명령어로 필요한 패키지를 설치해주세요:")
        print("pip install matplotlib seaborn numpy pandas")
        return False

# 선 그래프 예제 (라인 플롯)
def test_line_plot():
    print("\n=== 선 그래프 테스트 ===")
    # 한글 폰트 설정
    KoreanVisualization.setup_korean_font()
    
    # 데이터 생성
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # 그래프 생성
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='사인(sin)')
    plt.plot(x, y2, label='코사인(cos)')
    plt.title('삼각함수 그래프')
    plt.xlabel('x축 (라디안)')
    plt.ylabel('y축 (값)')
    plt.grid(True)
    plt.legend()
    
    # 파일로 저장
    plt.savefig('./test_dump/line_plot_korean.png')
    plt.close()
    print("line_plot_korean.png 파일로 그래프가 저장되었습니다.")

# 막대 그래프 예제 (바 플롯)
def test_bar_plot():
    print("\n=== 막대 그래프 테스트 ===")
    # 한글 폰트 설정
    KoreanVisualization.setup_korean_font()
    
    # 데이터 생성
    categories = ['서울', '부산', '인천', '대구', '광주', '대전', '울산']
    values = [1000, 800, 700, 600, 550, 500, 450]
    
    # 그래프 생성
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='skyblue')
    plt.title('주요 도시 인구 통계')
    plt.xlabel('도시')
    plt.ylabel('인구 (만 명)')
    plt.xticks(rotation=45)
    
    # 각 막대 위에 값 표시
    for i, v in enumerate(values):
        plt.text(i, v + 10, str(v), ha='center')
    
    # 파일로 저장
    plt.tight_layout()
    plt.savefig('./test_dump/bar_plot_korean.png')
    plt.close()
    print("bar_plot_korean.png 파일로 그래프가 저장되었습니다.")

# 원형 그래프 예제 (파이 차트)
def test_pie_chart():
    print("\n=== 원형 그래프 테스트 ===")
    # 한글 폰트 설정
    KoreanVisualization.setup_korean_font()
    
    # 데이터 생성
    labels = ['한국어', '영어', '중국어', '일본어', '기타']
    sizes = [45, 25, 15, 10, 5]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    explode = (0.1, 0, 0, 0, 0)  # 첫 번째 조각만 돌출
    
    # 그래프 생성
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.axis('equal')  # 원을 동그랗게 유지
    plt.title('선호하는 언어 비율')
    
    # 파일로 저장
    plt.savefig('./test_dump/pie_chart_korean.png')
    plt.close()
    print("pie_chart_korean.png 파일로 그래프가 저장되었습니다.")

# 히트맵 예제
def test_heatmap():
    print("\n=== 히트맵 테스트 ===")
    # 히트맵 데이터 생성
    data = np.random.rand(6, 6) * 100
    rows = ['서울', '부산', '대구', '인천', '광주', '대전']
    cols = ['1월', '2월', '3월', '4월', '5월', '6월']
    
    # 데이터프레임 생성
    df = pd.DataFrame(data, index=rows, columns=cols)
    
    # 히트맵 플롯 생성
    plt = KoreanVisualization.make_korean_heatmap(df)
    
    if plt:
        plt.title('도시별 월간 강수량 (mm)')
        plt.tight_layout()
        plt.savefig('./test_dump/heatmap_korean.png')
        plt.close()
        print("heatmap_korean.png 파일로 그래프가 저장되었습니다.")

# 박스 플롯 예제
def test_box_plot():
    print("\n=== 박스 플롯 테스트 ===")
    # 한글 폰트 설정
    KoreanVisualization.setup_korean_font()
    
    # 박스플롯 데이터 생성
    data = [np.random.normal(0, std, 100) for std in range(1, 6)]
    labels = ['매우 낮음', '낮음', '보통', '높음', '매우 높음']
    
    # 박스 플롯 생성
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=labels, patch_artist=True)
    plt.title('변동성 수준에 따른 분포')
    plt.xlabel('변동성 수준')
    plt.ylabel('값')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 파일로 저장
    plt.savefig('./test_dump/box_plot_korean.png')
    plt.close()
    print("box_plot_korean.png 파일로 그래프가 저장되었습니다.")

# 모든 테스트 실행
def run_all_tests():
    print("===== 한글 폰트 및 시각화 테스트 =====")
    
    if not check_dependencies():
        return
    
    test_line_plot()
    test_bar_plot()
    test_pie_chart()
    test_heatmap()
    test_box_plot()
    
    print("\n모든 테스트가 완료되었습니다.")
    print("생성된 이미지 파일을 확인해주세요:")
    print("- line_plot_korean.png")
    print("- bar_plot_korean.png")
    print("- pie_chart_korean.png")
    print("- heatmap_korean.png")
    print("- box_plot_korean.png")
    
    # 귀여운 고양이 이모티콘과 함께 "문제 없음!" 메시지 출력
    jaebal()

if __name__ == "__main__":
    run_all_tests() 