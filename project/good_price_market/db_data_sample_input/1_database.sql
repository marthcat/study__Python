CREATE database Teamprj;
use Teamprj;

drop 

CREATE TABLE good(
	name varchar(255) null,
    addr varchar(255) null,
    addr1 varchar(255) null,
    id varchar (255) null,
    upjong varchar(255) null,
    food varchar(255) null,
    dong varchar(255) null,
    num varchar(255) null
    );

-- CSV 파일 SQL에 가져오기 
-- CSV 파일 안에 data 가져오기 전에 테이블 생성 ( CSV 파일의 데이터 완전화 정규화 안되있을 수도 있으므로 모든 데이터 VARCHAR(255), NULL허용, 기본키 설정 X
    
LOAD DATA
INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/0_seoul_dobong_food.csv'
INTO TABLE good 
CHARACTER SET euckr
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
IGNORE 1 ROWS;
-- 오류 Error Code : 1290 mySQL8 에서 로컬의 데이터를 입력할 때 보안상의 이유로 지정한 장소의 파일만 업로드가 가능해서 일어나는 문제 
-- 해결법 1. 문서파일을 mysql8.0에서 설정된 지정한 장소에 업로드할 파일 넣어주기
-- 			보통 지정한 장소 = 'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads'
-- 해결법 2. secure-file-priv를 NULL로 만들어 아무 디렉토리에서 import 가능하게 하기 

-- 오류 Error code : 1300 데이터 내용 문자셋이 UTF8로 오류가 날 경우  
-- 해결: 다른 문자셋(한글사용)인 EUCKR을 사용하여 해결 

-- 오류 Error code : 1262 데이터 안의 열,속성,데이터가 생성된 테이블규격에 맞지 않을 경우
-- 해결 : 초기 csv 파일 열 10개( 마지막 x,y 입력된 열 2개 존재) - > 2개 열 삭제 정상작동 
SELECT * FROM good;