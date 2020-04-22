웹사이트 이름: 경영학도의 좌충우돌 코딩 
웹주소 : https://whatisthenext.tistory.com/116

카테고리 : 이철규 (138) 
            프로그래밍 (131) 
            -JAVA (27) 
            - 안드로이드 (38) 
            - 통계 (1) 
            - 파이썬 (14) 
            - 배포 (5) 
            -R (3) 
            -Django (10) 
            - 코드분석 (25) 
            - 컴퓨터구조 (3) 
            - 리눅스 (1) 
            자기계발 (1) 
            언리얼엔진4 (0) 
            리뷰 (2) 
            - 음식 (1) 
            - 전자제품 (1) 


프로그래밍/파이썬

[파이썬] 정규표현식(regular expression) 

사용자 WITN 2017. 5. 27. 01:56 


정규표현식(Regular Expressions)

re 모듈 : 파이썬 정규 표현식을 지원한다.

파이썬에서는 정규 표현식을 지원하기 위해 re(regular expression) 모듈을 제공한다.
자바(JAVA)에서 패턴 객체(p)의 메서드는 조금 다르니, 자바 API 를 참고하도록 하자.

import re 를 통해 모듈을 임포트한 뒤, p = re.compile('정규표현식')을 통해서 정규표현식을 컴파일하고, 컴파일된 패턴 객체(p)를 이용하여 이 객체가 가지고 있는 메서드를 통해 작업을 수행할 수 있다.

어떻게 사용하는가? 첫번째 방법 : 컴파일 후 매칭
import re # 정규표현식 모듈 
 
p = re.compile('[a-z]+') # re 내장모듈 내(.) compile 메서드를 사용. 
                         # compile 메서드는 "패턴 객체"를 반환한다. 
 
m = p.match("python")    # 패턴 객체(p)에는 또다시 검색 메서드가 있다. 


어떻게 사용하는가? 두번째 사용법 : 축약형
m = re.match('정규표현식', 문자열 소스)


축약형은 컴파일하지 않고 바로 매칭할 수 있다. 위에처럼 한 줄로 쓰기가 가능하다.
import re
 
source = 'Lux, the Lady of Luminosity'
m = re.match('[a-z]+', source ) # 컴파일과 매치를 한번에 했다. 


두 개 차이점이 뭔데?
import re
p = re.compile("정규식 표현")

1.
컴파일(compile)을 활용하는 경우, 한 줄 더 써야 하지만 패턴 객체(p)를 만들고 나서 여러번 재사용이 가능하다.

2.
반복적인 매칭 작업이 필요할 경우에는 패턴을 미리 컴파일해서 시간을 단축할 수 있다.


패턴 객체(p)가 제공하는 메서드에 대해서
import re # 정규표현식 모듈 
 
p = re.compile('[a-z]+')
m = p.match("python") # 패턴 객체(p)에는 여러 메서드가 있다. 


패턴 객체(p) 안에는 여러 메서드가 들어있다.

이 메서드들은 주로 검색에 관한 메서드다. 매칭되는 걸 찾았으면 반환하고 어디서 매칭되는지 위치를 알려주고, 필요하다면 바꿔주고 쪼개줘야 할 필요가 있을 것이다.

스크린샷, 2017-05-26 18-31-40
dir(p)를 통해서 패턴 객체(p)가 가지고 있는 메서드를 확인할 수 있다.
대표적으로 아래와 같은 메서드가 존재한다. 자세한 내용은 뒤에서 학습하도록 하겠다.


패턴(pattern) : 정규식을 컴파일 한 결과
 패턴(pattern) 객체 : 정규식을 컴파일한 결과를 담은 변수 (포스팅에서는 p로 표현)

메타 문자
 . ^ $ + ? { } [ ] \ | ( )


11가지를 안보고 기능까지 정확하게 읊을 수 있도록 노력하려 한다.


메타 문자

설명


[ ] 문자 클래스 
. \n을 제외한 모든 문자와 매치 (점 하나는 글자 하나를 의미) 
* 0회 이상 반복 (업어도 상관 없음) 
+ 1회 이상 반복 (무조건 한번 이상 등장해야 함) 
{m, n} m회 이상 n회 이하 
l or 조건식을 의미 
^ 문자열의 시작 의미 
$ 문자열의 끝을 의미 
? 0회 이상 1회 이하 
\ 이스케이프, 또는 메타 문자를 일반 문자로 인식하게 한다 
( ) 그룹핑, 추출할 패턴을 지정한다. 

1. [ ] : 대괄호 안에 아무거나 집어넣을 수 있다.

대괄호는 문자 클래스(character class)다.
문자 클래스의 특징은 세 가지만 알고 있으면 된다.
1.
대괄호 안에는 어떤 것이든 들어갈 수 있다. 
•
단, 엄밀하게 구분된다. 즉, a와 A가 다르고, z와 Z가 다르다.



2.
안에 들어간 것끼리는 or로 연결된다. 
•
하이픈(-)으로 연결해줄 수 있다.

•
[a-z]는 a부터 z까지를 의미한다. [0-9]는 0부터 9까지를 의미한다.



3.
만약 [abc]라면, 'a, b, c' 중에서 한 개의 문자 와 매칭된다.


바로 문제를 내도록 하겠습니다.

1.
정규표현식 [abc]가 있다. 다음중 매칭되는 것은?

(1) a (2) before (3) dude

2.
정규표현식 [a-c]가 있다. 다음중 같은 의미는?

(1) a 또는 c (2) a 또는 b 또는 c (3) [abc] (4) a 그리고 b 그리고 c

3.
정규 표현식 a[a-z0-9]z가 있다. 다음중 매칭(Y) 되는 것은? (응용)
 (1) a!012z (2) aBz (3) a999z (4) azX09z (5) a9z


1.
(1), (2) 풀이 : a 또는 b 또는 c가 들어있으면 된다.

2.
(2) 풀이 : 하이픈(-)은 범위를 나타낸다. [0-9]는 0~9를 의미한다.

3.
(5) 풀이 : 대괄호 안에 한 글자만을 의미한다. +나 *를 써준다면 (3)도 출력된다.


자주 사용하는 문자 클래스 [ ]

문자 클래스(character class)는 위에서 배운 대괄호[ ]를 의미한다.
보통 알파벳을 표현하기 위해서 [a-zA-Z]를 사용하고, 숫자를 표현하기 위해 [0-9]를 쓴다.

이게 너무 귀찮다보니 한 글자로 줄여버렸다.







원래 표현식

축약 표현

부연 설명

사용처


[0-9] \d 숫자를 찾는다 숫자 
[^0-9] \D 숫자가 아닌 것을 찾는다 텍스트 + 특수문자 + 화이트스페이스 
[ \t\n\r\f\v] \s whitespace 문자인 것을 찾는다 스페이스, TAB, 개행(new line) 
[^ \t\n\r\f\v] \S whitespace 문자가 아닌 것을 찾는다 텍스트 + 특수문자 + 숫자 
[a-zA-Z0-9] \w 문자+숫자인 것을 찾는다. (특수문자는 제외. 단, 언더스코어 포함) 텍스트 + 숫자 
[^a-zA-Z0-9] \W 문자+숫자가 아닌 것을 찾는다. 특수문자 + 공백 


TIP 1 : 대문자는 소문자의 반대 역할을 한다.
TIP 2 : 보통 ^문자열은 맨 처음과 일치함을 의미하지만, 문자 클래스[^문자열]에서는 not의 의미다.




2. Dot(.) : \n을 제외한 모든 문자와 매칭된다.

도트 하나는 문자 하나를 의미한다.
도트 두개는 문자 두개를 의미한다.


TIP 1 : 문자는 숫자(0-9)나 특수문자(!@#$%^& 등)을 포함한다.

1.
정규 표현식 a.z가 있다. 다음중 매칭(Y) 되는 것은?
 (1) akdz (2) axz (3) abdeZ (4) aBDEz (5) axcz

2.
정규표현식 a.z가 있다. 다음중 매칭(Y) 되는 것은?
 (1) a&z (2) a!z (3) a0z (4)akz





정답 :
1.
(2) 풀이 : dot(.) 하나는 문자 하나를 의미한다. 따라서 3글자만 매칭 된다.

2.
(1), (2), (3), (4) 풀이 : 문자에는 특수문자와 숫자도 포함됨을 알아야 한다.


3. 반복 * : * 바로 앞 문자가 0번 이상 반복


표현식

설명

매칭 예시


.* 선행문자가 .이므로 하나 이상의 문자를 포함하는 문자열(공백 문자열 제외) 
 모든 문자가 출력될 거라고 생각하기 쉽지만, .이 공백 문자열은 제외하기 때문에 첫줄만 출력된다. 모두 선택을 하고자 한다면 .+로 출력하는 것이 적절해보인다.`
 
ab*c b를 0번 또는 여러번 반복되도 상관없음 ac, az, a123c, abbbb 
like.* 선행문자가 .이므로 like에 0 또는 하나 이상의 문자가 추가된 문자열 like, likely ,likelihood 

4. 반복 + : + 바로 앞 문자가 1번 이상 반복

애스터리스크(*)는 *의 선행문자가 0번 이상 반복될 수 있다는 의미였다면
+는 선행문자가 무조건 1번 이상 등장해야 한다. 양수를 표현할 때 +를 붙이니까 구분하자.


표현식

설명

매칭 예시


ca+t a가 1번 이상 반복되야 함 cat, caaaat, caaaaaaaat 
car+ot r이 1번 이상 반복되어야 함 carrot 
like.+ 선행문자가 .이므로 like에 하나 이상 문자열이 추가되어야 함 liekly, liker (단, like는 안된다.) 
[A-Z]+ 대문자로만 이루어진 문자열 ABC, DEF, ZAX 
 
source = "Luke Skywarker 02-123-4567 luke@daum.net"  # \w와 \w+의 차이 
 
m1 = re.findall('\w', source) # 단어가 아니라 문자 단위로 출력 
m2 = re.findall('\w+', source) # 단어 단위로 출력 
print("m1 : ", m1)
print("m2 : ", m2)
 
>>> 출력결과
m1 :  ['L', 'u', 'k', 'e', 'S', 'k', 'y', 'w', 'a', 'r', 'k', 'e', 'r', '0', '2', '1', '2',&nbnbsp;'3', '4', '5', '6', '7', 'l', 'u', 'k', 'e', 'd', 'a', 'u', 'm', 'n', 'e', 't']
m12 :  ['Luke', 'Skywarker', '02', '123', '4567', 'luke', 'daum', 'net']


+를 붙여야 온전한 단어형태 처럼 출력이 된다. +와 *는 굉장히 자주 등장하니 꼭 숙지하자.

5. 반복 {} : 바로 앞 문자의 반복횟수 지정


표현식

설명

"ct cat caat caaat caaaat"


ca{2}t a가 2회 반복되어야 함 caat 
ca{2,5}t a가 2회 이상 5회 이하 반복되어야 함 caat, caaat, caaaat 
ca{0, }t 반복횟수 0회 이상 (*와 동일) ct, cat, caat, caaat, caaaat 
cat{0, 1}t 반복횟수 0회 ~ 1회 이하 (?와 동일) ct, cat 
cat{ , 3} 반복횟수 0회 이상 ~ 3회 이하 ct, cat, caat, caat 
import re
 
source = "ct cat caat caaat caaaat"
m1 = re.findall("ca{2}t", source)
m2 = re.findall("ca{2,5}t", source)
m3 = re.findall("ca{0,}t", source)
m4 = re.findall("ca{0,1}t", source)
m5 = re.findall("ca{,3}t", source)
print("m1 : ", m1)
print("m2 : ", m2)
print("m3 : ", m3)
print("m4 : ", m4)
print("m5 : ", m5)
 
>>>출력결과
m1 :  ['caat']
m2 :  ['caat', 'caaat', 'caaaat']
m3 :  ['ct', 'cat', 'caat', 'caaat', 'caaaat']
m4 :  ['ct', 'cat']
m5 :  ['ct', 'cat', 'caat', 'caaat']


6. 반복 ? : ? 반복횟수 {0,1}을 의미. 선행문자가 있어도, 없어도 됨


표현식

설명

예시


ab?c b가 있어도 되고 없어도 된다. ac, abc 
import re
 
source = "ct cat caat caaat caaaat"
m1 = re.findall("ca?", source)
print("m1 : ", m1)
 
>>> 출력결과
m1 :  ['c', 'ca', 'ca', 'ca', 'ca']


쉬어가기 처럼 보이지만 공부하기

1. 최소일치와 최대일치


알고가기
*과 +는 탐욕적인 연산자(Greedy Operator)라고도 한다.
?는 비탐욕적인 연산자(Non-greedy Operator)라고도 한다.

1. Greedy : 최대일치 * 또는 +만 사용했을 때

* 메타문자는 Greedy이다. 그래서 최대한 찾고 싶어하기 때문에 최대일치라고도 한다.
import re
source = <li>나이키</li><li>아디다스</li><li>퓨마</li>
m = re.match('<li>.*</li>', source)
if m:
    print(m10.group())
 
>>> 출력결과
<li>나이키</li><li>아디다스</li><li>퓨마</li>


.* 를 잘개 쪼개보면 .은 아무 문자를 의미하고 *는 0번 이상만 등장하면 된다.
그래서 <li>.*</li>를 하게 됐을 때 처음부터 끝까지 출력하게 된다.

2. Non-Greedy : * 또는 + 뒤에 ?가 왔을 때

?가 문자 앞에 등장하게 되면 해당 문자가 있거나 or 없거나 이지만,
?가 greedy operator 뒤에 등장하면 워워~ 이러면서 탐욕을 멈추게 한다.
예를 들어 *나 + 뒤에 물음표를 붙여주면 최소 반복을 수행하도록 한다.

위 코드를 다시 수정해서 출력하면 아래와 같이 된다.
html = "<li>나이키</li><li>아디다스</li><li>퓨마</li>"
m10 = re.match(r'<li>.*?</li>', html)
if m10:
    print(m10.group())
 
>>> 출력결과
> <li>나이키</li> # 가장 처음 만나는 </li>에서 출력을 멈춘다. 

•
.은 문자 1개를 의미

•
*는 해당 패턴이 0회 이상 올 수 있다.

•
.*은 문자가 있거나 없을수도 있다.

•
.*Lady : 앞에 아무 문자열(또는 빈) 이후 Lady로 끝나는 패턴을 의미한다.



7번부터 소개할 메타문자는 성격이 조금 다르다.
+, *, ?, { }는 문자열의 소모와 관련이 깊다. 즉, 매칭을 진행하면서 반복의 조건을 마치면 검색 대상에서 제외된다.

앞으로 소개할 메타문자는 |, ^, $, \, ()이다.
거의 다 왔다.


7. | : OR을 의미
p = re.compile('a|b') # a 또는 b를 찾는다. 
m = p.findall("abcdefg")
print(m)
 
>>>출력결과
> ['a', 'b']


8. ^ : 맨 처음에 이게 와야 한다.
# 메타문자 ^, & 
m1 = re.findall("^Life", "Life is too short")
m2 = re.findall("^is", "Life is too short")
print("m1 결과 : ", m1)
print("m2 결과 : ", m2)
 
>>> 출력결과
> m1 결과 :  ['Life']
> m2 결과 :  []


간단하기 때문에 예제로만 설명하고자 한다.
첫번째 예제는 문장이 Life로 시작하기 때문에 결과를 반환하지만, 두번째 예제는 is로 시작하지 않는다.

9. $ : 맨 마지막에 이게 와야 한다.
m1 = re.findall("short$", "Life is too short")
m2 = re.findall("short$", "Life is too short. So what?")
 
print("m1 결과 : ", m1)
print("m2 결과 : ", m2)
 
>>> 출력결과
> m18 결과 :  ['short'] # 문장 끝이 short기 때문에 short를 반환한다. 
> m19 결과 :  [] # 문장 끝이 short가 아니기 때문에 반환값이 없다. 



외우는 팁 : 마우스가 없던 시절로 거슬로 올라가야 한다. 커서는 문장 처음부터 시작하기에 문장 맨 끝으로 가야 하는 일이 더 많았다. 개발자들은 '문장 끝으로 가라'의 의미 '$(달러사인)'을 손가락에 더 가깝게 배치했다.

반대로 사용 빈도가 적은 '문장 처음으로 오라'의 의미 '^(hat)'은 좀 더 먼 shift+F6에 배치했다. 물론 개인적인 내 추측이다. VIM에 익숙한 분들은 쉽게 캐치할 수 있다.

10. \ : 문자 클래스를 나타내거나, 메타 문자를 일반문자로

\A는 문자열의 처음과 매치됨을 의미한다. ^와 동일한 의미이지만 re.MULTILINE옵션을 사용할 경우에는 다르게 해석된다. re.MULTILINE 옵션을 사용할 경우 ^은 라인별 문자열의 처음과 매치되지만 \A는 라인과 상관없이 전체 문자열의 처음하고만 매치된다.

\Z는 문자열의 끝과 매치됨을 의미한다. 이것 역시 \A와 동일하게 re.MULTILINE 옵션을 사용할 경우 $ 메타문자와는 달리 전체 문자열의 끝과 매치된다.

11. ( ) : 그루핑. 검색 결과의 특정 부분만 출력한다.
# 그루핑 () 
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(1))
print(m.group(2))
 
>>> 출력결과
> park
>010-1234-1234


자세히 보면 괄호가 2개 있다. 첫번째 등장하는 괄호는 group(1)이고, 두번쨰 등장하는 괄호는 group(2)이다.

match 객체의 메서드


메서드

설명


match 문자열의 처음부터 정규식과 매치되는지 조사 
search 문자열 전체를 검색하여 정규식과 매치되는지 조사 
findall 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴 
split 패턴으로 나누기 
sub 패턴 대체하기 

파이썬에서 정규 표현식을 지원하는 re(regular expression) 모듈이 있다.
패턴 객체를 리턴하며, 이 객체를 이용해 메서드를 사용할 수 있다.

search 와 match

match와 search 둘 다 비슷한 의미를 가진 듯 하다.
하지만 어감을 좀 더 살려보면 match는 "일치하다"와 좀 더 가깝고 serach는 수색에 좀 더 가깝다.

match는 매정하다. 처음이 일치하지 않으면 None을 반환한다.
search는 다정하다. 처음이 일치하지 않더라도 전체를 수색해본다.
# match와 search 
source13 = '''All That Is Gold Does Not Glitter"
'''
match = re.match("Not", source13)
search = re.search("Not", source13)
 
if match:
    print("match : ", match.group())
 
if search:
    print("search : ", search.group())
 
>>> 출력결과
>
> search :  Not


match의 결과는 None이 된다. 왜냐하면 처음이 Not으로 시작되지 않기 때문이다.
search는 그래도 전체를 찾아본다. 뒤에 Not이 등장하기 때문에 매칭값을 반환한다.
# match와 search 
source13 = '''All That Is Gold Does Not Glitter"
'''
match = re.match("All", source13)
search = re.search("All", source13)
 
if match:
    print("match : ", match.group())
 
if search:
    print("search : ", search.group())
 
>>> 출력결과
> match : All
> search :  Not


All로 바꿨더니 그제서야 match도 출력을 한다.
이런 쓰레기같은 메서드를 왜 쓰냐 싶겠지만, 비밀번호의 처음 시작은 무조건 대문자여야 한다거나 양식을 엄격히 지켜야 할 필요가 있을 경우에 match를 써야하지 않을까 추측해본다.

match와 search는 성격은 다르지만, 공통점이 하나 있다.
원하는 것이 발견되면 검색을 멈춘다 .

뒤에서 배울 find는 발견되더라도 계속 찾는다. 그래서 결과값을 list또는 iterator값으로 반환한다.

findall 과 finditer
import re
p = re.compile('[a-z]+') # 소문자(a-z)가 1회 이상 반복되는 걸 찾아와라. 
m = p.findall("Life is to short")
print(m)
print(type(m)) # m의 타입은!? 
 
>>> 출력결과
['ife', 'is', 'to', 'short']
<class 'list'>


findall()은 정규식과 매치되는 모든 문자열을 리스트형식으로 리턴한다.
import re
p = re.compile('[a-z]+') # 소문자(a-z)가 1회 이상 반복되는 걸 찾아와라. 
m = p.finditer("Life is to short")
print(m)
print(type(m))
 
>>> 출력결과
<callable_iterator object at 0x7f010c08b588>
<class 'callable_iterator'>


finditer()는 정규식과 매치되는 모든 문자열을 iterator 객체로 리턴한다.
iterator 객체의 값을 불러오려면 for문을 이용해 읽어들여야 한다.
for r in m:
  print(r)
 
>>> 출력결과 # 출력을 해보면 Match 객체를 또 다시 리턴한다. 
 
<_sre.SRE_Match object; span=(1, 4), match='ife'>
<_sre.SRE_Match object; span=(5, 7), match='is'>
<_sre.SRE_Match object; span=(8, 10), match='to'>
<_sre.SRE_Match object; span=(11, 16), match='short'>
 
 
만약 값을 뽑아오고 싶다면
for r in m
  if r:
    print(r)
 
>>> 출력결과
ife
is
to
short


마무리

정규패턴식을 보다보면
p = re.compile(r'\\section')


정규패턴식 앞에 r이 붙어 있는 경우가 많다. 파이썬 정규식에는 Raw string이라고 해서, 컴파일 해야 하는 정규식이 Raw String(순수한 문자)임을 알려줄 수 있도록 문법이 있다.

만약 p = re.compile('\section') 이라고 쓴다면 \s는 공백문자를 의미하는 [ \t\n\r\f\v]이 되어버려서 원하는 결과를 찾지 못한다. 그래서 #10번에서 배웠듯이 이스케이프 \를 활용해 \\section이라고 해주면 되지만, 파이썬은 특수하게 r을 사용하면 백슬래쉬를 1개만 써도 두개를 쓴 것과 같은 효과를 갖는다.

다루지 않은 내용들
1.
10번 이스케이프(\)에서 \A, \Z, \b, \B 등의 내용은 생략됐다.

2.
11번 그룹핑(())에서 그룹핑된 문자열을 재참조할 수 있다는 점은 다루지 않았다.

3.
또한, 그룹핑된 문자열에 이름을 붙이는 것이 가능하다는 점은 다루지 않았다.

4.
전방탐색(긍정형, 부정형)에 대해선 다루지 않았다.

5.
문자열 바꾸기(sub 메서드)에 대해서 다루지 않았다.


다루지 않은 내용은 점프투 파이썬(https://wikidocs.net/4309)에서 확인 가능하다.

참고할만한 사이트
1.
http://www.nextree.co.kr/p4327/ 연산자가 어떻게 묶이는가? (영문))

2.
탐욕적 연산자, 비탐욕적 연산자 *, + 연산자와 ? 연산자의 차이점을 쉽게 배울 수 있다. (한글)

3.
정규표현식 단계별 연습 정규표현식을 통해 여러 표현에 대해 단계별 학습 가능(한글)

4.
점프 투 파이썬 가장 쉽게 설명 되어 있다. 추천 (한글)

5.
파이썬 정규표현식 API 파이썬 공식 API (영문)

6.
정규표현식을 연습해볼 수 있는 사이트 (영문))

