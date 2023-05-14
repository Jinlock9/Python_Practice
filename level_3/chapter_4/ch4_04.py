"""
Chapter 4 - Python Advanced (4) : 나만의 Package 만들기 (3) - PypI 배포
Keywords : PyPI, build, package deploy
"""
# imports ==============================================================================================================
from pygifconvt_test_jl.converter import GIFConvertor as Gfc
# ======================================================================================================================

# create object
c = Gfc("../../support/images/*.png", "../../support/image_out/result.gif")

# execute
# c.convert_gif()
print(c.convert_gif.__doc__)

"""  # =================================================================================================================
[ Package 배포 순서 ( PyPI ) ] -------------------------------------------------------------------------------------------
1. https://pypi.org register
2. check project structure
3. write __init__.py
4. 프로젝트 Root 필수 파일 작성
    - README.md
    - setup.py
    - setup.cfg (optional)
    - LICENSE
    - MANIFEST.in
5. pip install setuptools wheel 설치 후 빌드 업 -> 설치판 생성
    - 설치 1 : python -m pip install --upgrade setuptools wheel
    - 설치 2 : python -m pip install --user --upgrade setuptools wheel
    - 빌드 : python setup.py sdist bdist_wheel
6. PyPI 배포
    - 설치 : pip install twine
    - 업로드 : python -m twine upload dist/*
    - 버전 업 : setup.py 에 version 만 바꿔서 재 업로드
7. 설치 확인 ( pip install pygifconvt-test-jl )
    - from pygifconvt-test-jl import GIFConvertor as Alias
------------------------------------------------------------------------------------------------------------------------
"""  # =================================================================================================================
