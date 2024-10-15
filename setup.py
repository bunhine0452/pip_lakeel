from setuptools import setup, find_packages

setup(
    name="lakeeel",  # 패키지 이름
    version="0.0.1",  # 버전
    description="Automatically set Korean font for matplotlib based on the user's OS",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="bunhine0452",
    author_email="hb000122@gmail.com",
    url="https://github.com/yourusername/my_matplotlib_korean_font",
    packages=find_packages(),
    install_requires=[],  # 여기엔 필요한 패키지를 나열
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)


