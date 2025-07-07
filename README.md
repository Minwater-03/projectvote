# ProjectVote - Django Backend

Django, REST framework, Docker를 활용한 오픈소스 프로젝트 평가 웹서비스입니다.

##  주요 기능

- 관리자 페이지에서 프로젝트 등록
- 사용자: 프로젝트 리스트 확인 및 상세 정보 조회
- 사용자: 1~5점 사이의 투표 기능
- 프로젝트 평균 점수 계산 및 정렬
- Swagger UI를 통한 API 테스트 제공

---

##  실행 방법 (Docker 기반)

```bash
#이미지 빌드 및 컨테이너 실행
docker-compose up --build

# 또는
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser

## API 테스트 방법
http://localhost:8000/swagger/ 접속 후,
GET, POST 요청을 통해 프로젝트 조회 및 투표 테스트 가능

## 보안 설정
.env 파일을 통한 민감정보 관리

.gitignore에 .env, __pycache__, *.pyc 등 포함하여 Git에 업로드되지 않도록 설정

## 기타
requirements.txt에 모든 의존성 명시

관리자 페이지: http://localhost:8000/admin/

기본 superuser 생성 필요 (createsuperuser 명령어 사용)