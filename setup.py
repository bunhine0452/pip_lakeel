from setuptools import setup, find_packages

setup(
    name="lakeel",  # 패키지 이름
    version="0.0.3",  # 버전
    description="Automatically set Korean font for matplotlib based on the user's OS",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author="bunhine0452",
    author_email="hb000122@gmail.com",
    url="https://github.com/bunhine0452/pip_lakeel",
    packages=find_packages(),
    license='MIT',
    install_requires=['matplotlib','pandas'],  # 여기엔 필요한 패키지를 나열
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)


