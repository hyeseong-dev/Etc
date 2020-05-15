참고. 기본 주피터 노트북과 주피터 랩의 단축키 기본구성은 거의 동일함. 

1. 주피터 노트북 실행하기 
    - 이 방법은 거의 잘 사용하지 않음
        C:\Users\dojang>C:\Users\dojang\Anaconda3\python.exe -m notebook
    
    - 환경변수에 등록했을 경우 사용 
        C:\Users\dojang>jupyter notebook 

2. ******저장 경로 바꾸기 
      --notebook-dir 옵션에 폴더를 지정
        예시) C:\Users\dojang>C:\Users\dojang\Anaconda3\python.exe -m notebook --notebook-dir C:\project


3. [Magic Command]세부 기능 

    - %cd               디렉터리 경로 변경 시 사용 

    - %ls               파일이나 폴더 목록 표시

    - %paste            클립보드에서 들여쓰기된 상태로 파이썬 코드 붙여넣기 

    - %magic            도움말 출력 

    - %quickref         빠른 도움말 표시 

    - %hist             명령어 히스토리 출력 

    - %run script.py    Jupyter에서 파이썬 스크립트 실행 

    - %time             명령 실행시간 출력

출



참고 웹사이트 : 테리엇의 디지털 놀이터 
주소: https://tariat.tistory.com/545

    0. 커서 위치에서 셀 둘로 나누기
        [shift] + [ctrl] + [-]



출처: https://kkokkilkon.tistory.com/151 [꼬낄콘의 분석일지]

    1. tab, 함수 자동완성
           
        컴퓨터를 오래하다 보면 손목과 손이 아프다. 어떻게든 타이핑을 적게 하고 싶은 것이 사람의 마음이다. 특히, 자주 쓰지 않는 함수는 잘 기억이 나지 않아 찾아보게 된다. 이런 불편함을 덜어주는 것이 tab이다. 입력을 하다가 tab을 누르면, 그에 해당하는 함수들이 list된다. 파이참에서는 별도의 키입력 없이 자동으로 제공되지만, Jupyter Lab은 웹환경이다보니 tab을 눌러야 되지 않나 싶다.

        (  .을 입력하고 tab을 누르면 쓸 수 있는 함수리스트가 나온다 )


    2. shift + tab, 함수 설명 보기
        자동완성을 이용해서 함수를 입력했지만, 문법이 잘 생각나지 않을 때가 있다. 또는 이 함수가 어떤 내용인지 궁금할 때가 있다. 이럴 때는 shift+tab을 입력하면 해당 함수의 설명을 볼 수 있다. 잘   사용하지 않는 함수는 파라미터들이 잘 기억나지 않는데, 그럴 때 유용하게 쓸 수 있는 단축키이다.


    3. shift + Enter, 콘솔창에서 코드 실행
        이전 포스팅에서 파이썬 코드 아래에 Ipython을 띄우는 법을 알아보았다. ( 참조: Jupyter Notebook보다 쉽고 편리하다, Jupyter Lab ) IPython을 띄우고 나면 파이썬 코드 입력 후 바로 Python창에서  실행을 할 수 있다. 코드 라인에 커서를 놓고 shift + Enter를 입력하면 된다. 파이참에서는 ctrl + shift + e로 할 수 있는 기능과 동일하다.



    4. ctrl + shift + [ , ], 좌우창 이동
        이 단축키는 좌우 창으로 이동하는 단축키이다 .파이썬 코드를 입력하다가 가끔은 Python console에 명령을 날리고 싶을 때가 있다. 그럴 때 'ctrl + shift + ] '로  파이썬 콘솔에서 명령어를 날리고, 'ctrl + shift + [' 로 코드창으로 돌아올 수 있다. 데이터 분석을 하다보면 많이 필요한 단축키이다.



    5. Ctrl + Shift + L, 새 창 띄우기
        새 창을 띄울 때 사용하는 단축키이다 .파이썬 콘솔, terminal, jupyter notebook 등 새로운 창을 띄울 때 사용한다. Ctrl + N과 헷갈리는데, Ctrl +N을 입력하면 브라우저로 단축키가 입력된다. 

