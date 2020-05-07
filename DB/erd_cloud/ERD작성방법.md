데이터 모델은 데이터 베이스에 독립적이다.   

정보 시스템을 개발하기 전에 보다 많으 아이디어를 도출하고 데이터베이스 설계의 이해를 높이기 데이터 모델링을 한다. 

관계형 데이터 모델은    
1. 실체(Entity)
2. 속성(Attribute)  
3. 관계(Relationship)으로 구성된 ER Diagram으로 표현된다. 


관계형 데이터 모델 - 데이터베이스 개발 과정     
||
|:------------------|
|1. 업무 정보화 요구|
|2. 개념 데이터 모델링 - 분석,전략수립|
|1. 데이터베이스 설계 - 설계|
|1. 데이터베이스 생성 - 개발|   

    ERD는 개념 데이터 모델링 단계에서 작성하는 다이어 그램

###    실체(Entity): 관리하고자 하는 정보의 실체 

        - 둥근 사각형으로 작성
        
        - Entity 이름은 단수형이고 유일하며 대문자로 크게 표기할 것. ()안에 동의어 표기 가능. 
        
        - 모든 Entity는 하나 이상의 식별자(UID: Unique Identifier)를 가져야함.
        
        - UID가 없다면 Entity가 아님
    

###    속성(Attribute): Entity를 구성하고 있는 구성 요소

        - Attribute 이름은 소문자로 작게 표기할 것. 
        
        - Entity 이름과 Attribute 이름이 같으면 안됨. 
        
        - '#' 은 UID. '*'는 필수(Mandatory). 'o'는 선택(Optional) Attribute를 의미
        
        - 자신의 Attribute가 아니면서 Relation을 위해 늘 자신의 Attribute로 표시해서는 안된다. 


###     관계(Relationship): Entity간의 관계 

        - 두 Entity 사이엔 선을 긋고 관계 명칭을 기록한다. 
        
        - 선택 사항을 표시한다. 
            -> 점선은 선택(may be)을 의미(부서 입장에서는 사원을 배치받을 수도 있고, 안받을 수도 있기 때문에)

            -> 실설은 필수(must be)를 의미 (사원 입장에서는 반드시 부서에 배치되어야 하기 때문)
        - 관계 형태를 표시함. 
            -> 새 발 모양은 하나 이상(one or more)을 의미(사원 여러명이 한 부서에 속할 수 있기때문)
            ->단, 선은 단 하나(one and only one)를 의미(한명의 사원은 한 부서에만 소속될 수 있음.)

        ![](https://t1.daumcdn.net/cfile/tistory/990D76505D2C180E1E)

## Relationship 표현

![](https://t1.daumcdn.net/cfile/tistory/9902DF425D2C20522E)

## Relationship 읽기

![](https://t1.daumcdn.net/cfile/tistory/99FB28455D2C21D014)
먼저 한 방향(좌->우)을 읽고 난 후에 다른 방향(우->좌)을 읽는다. 



## 관계 형태        
### 1:1 관계    

![](https://t1.daumcdn.net/cfile/tistory/9944C2475D2C227709)    

ㄱ. 양쪽 방향 모두 단 하나씩(1 & only 1)(라면은 두개 이상의 스프를 포함하고 있지 않고, 스프도 한개 이상의 라면에 들어 있지 않다. )  
ㄴ. 드물게 발생되는 형태    
ㄷ. 양방향 모두 반드시(must be)가 되는 경우는 아주 드물다.   
ㄹ. 1:1 관계는 실제로는 동일한 ENTITY일 경우가 많다.    

        

### M:1 관계
ㄱ. 한쪽 방향은 하나 이상(one or more)
    -(각 사원은 단 하나의 부서에 반드시 소속되어야 하고, 각 부서는 여러명의 사원을 배치받을 수 있다.)
ㄴ. 다른 방향은 단 하나씩(one and only one) 
ㄷ. 가장 일반적인 관계 형태     
ㄹ. 보통 must be와 may be로 지정되나 양방향 모두 mustbe로 지정되는 경우도 있다.     

### M:M 관계        
ㄱ. 양쪽 방향 모두 하나 이상(one or more) 
    - 각 학생은 하나이상의 교육과정에 신청할 수도 있고, 각 교육과정은 여러 학생을 등록 받을 수있다.)
ㄴ. 자주 발생되는 형태이지만 최종 결과에서는 M:M 관계는 나타나지 않는다. 
ㄷ. 상세 개념모델링(Advanced Conceptual Data Modeling) 단계에서 M:1 관계로 분할된다.    
        -(M:M관계를 그대로 놔두면 문제가 발생되기 때문) 

> 학생과 교육과정 사이에 '수강신청'이라는 Entity를 만들어서 학생은 자신이 수강신청한 교육과정에만 관계를 맺고 있으면 된다. 이런식으로 M:M 관계를 M:1 관계로 분할시키면된다. 

### UID Bar 
한 사원의 부양가족을 확인하려면 부양가족 테이블에 '사번'entity가 있어야하는데   
부양 가족의 UID를 -> 사번 + 주민번호(기본키를 복합키)로 해서 한 사람의 사원에 대한 부양가족을 찾을수 있다.  
![](https://t1.daumcdn.net/cfile/tistory/99C114445D2C286D3A)


# 데이터 베이스 설계 
1. Entity를 Table로 Mapping
2. Attribute를 column으로 Mapping   
3. UID를 Primary Key로 Mapping
4. Relationship을 Foreign Key로 Mapping 


### 관계형 데이터 모델 - 요약
> 데이터 모델은 데이터 베이스에 독립적이다. 
    
> 데이터 모델링은 건축물의 설계도를 그리는 작업과 같다. 

> 관계형 데이터 모델은 여러 가지 데이터 모델 중 가장 널리 사용되는 모델이며, 실체(Entity), 속성(Attribute), 관계(Relationship)로 ER Diagram으로 표현된다. 

> Entity는 하나 이상의 식별자(UID: Unique Identifier)를 가져야 하며 UID가 없다면 Entity가 아니다.   

> E - R Diagram 작도 시 관계를 표현할 때에는 어떤 Entit가 주 인가를 잘 따져서 표현한다.     

> 관계형 데이터베이스는 2차원 테이블로 데이터를 표현한다. 