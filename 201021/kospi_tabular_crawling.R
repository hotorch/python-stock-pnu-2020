
# --------------------------------------------------------------------------------
# 네이버 증권 : 코스피200 데이터 수집하기 
# --------------------------------------------------------------------------------

# 필요한 패키지를 불러옵니다. 
library(tidyverse)
library(httr)
library(rvest)


# 네이버 증권 > 국내증시 > 코스피로 이동한 다음 웹 브라우저 주소창의 URL을 이용하여
# HTTP 요청을 실행합니다. 
res <- GET(url = 'https://finance.naver.com/sise/sise_index.nhn',
           query = list(code = 'KPI200'))

# HTTP 응답 결과를 출력합니다. 
print(x = res)

## charset이 'EUC-KR'이므로 read_html() 함수의 encoding 인자에 인코딩 방식을 지정합니다. 


# [주의] 로케일 변경은 Windows 사용자만
#Sys.setlocale(category = 'LC_ALL', locale = 'C')

# 크롬 개발자도구 Elements 창에서 HTML element를 찾습니다. 
res %>% 
  read_html(encoding = 'EUC-KR') %>% 
  html_node(css = 'div.subtop_sise_detail > table') %>% 
  html_table() -> tbl 

# [주의] 로케일 원복 역시 Windows 사용자만 하세요!! 
#Sys.setlocale(category = 'LC_ALL', locale = 'korean')


# tbl 객체를 출력합니다. 
print(x = tbl)



# --------------------------------------------------------------------------------
# tbl 객체 전처리
# --------------------------------------------------------------------------------

# 홀수행만 남기고 짝수행을 지웁니다. 
tbl <- tbl[seq(from = 1, to = 14, by = 2), ]

# 세 번째 컬럼을 제거합니다. 
tbl <- tbl[, -3]

# tbl 객체를 출력합니다. 
print(x = tbl)


# 컬럼명을 변경합니다. 
colnames(x = tbl) <- c('구분', '지수', '구분', '지수')

# 1~2번 컬럼 아래에 3~4번 컬럼을 잘라서 붙입니다. 
result <- rbind(tbl[, 1:2], tbl[, 3:4])


# 최종 결과 객체를 출력합니다. 
print(x = result)

# 행과 열을 변환합니다. 
result <- t(x = result)

# 열번호를 첫 번째 행의 값으로 대체합니다. 
colnames(x = result) <- result[1, ]

# 데이터프레임으로 변환합니다. 
result <- as.data.frame(x = result)

# 첫 번째 행을 삭제합니다. 
result <- result[-1, ]

# 행번호를 초기화합니다.
rownames(x = result) <- NULL

result

## End of document
