#  RAG 기반 PDF 질의응답 챗봇 - AI Tutor

> 대학 전공 교재를 기반으로 사용자의 질문에 정확하게 응답하는 LLM 챗봇 프로젝트입니다.  
> PDF 문서의 레이아웃을 분석하여 정보를 구조화하고, 의미 기반 검색(Retrieval)을 통해 신뢰도 높은 답변을 생성합니다.

---

##  프로젝트 개요

이 프로젝트는 비정형 PDF 문서를 처리하여,  
**사용자 질문에 대해 문서 내부 정보만을 기반으로 응답하는 RAG(Retrieval-Augmented Generation) 챗봇**을 구현합니다.

---

##  주요 기능

| 기능 | 설명 |
|------|------|
|  PDF 텍스트 추출 | PyMuPDF로 레이아웃 정보가 보존된 블록 단위 추출 |
|  Token 기반 chunking | tiktoken으로 적절한 길이의 슬라이딩 윈도우 구성 |
|  의미 기반 검색 | OpenAI embedding + FAISS를 활용한 벡터 검색 |
|  LLM 질의응답 | GPT-3.5-turbo를 활용한 문서 기반 응답 생성 |
|  CLI 데모 | 사용자가 직접 질문을 입력하고 응답을 확인할 수 있는 인터페이스 제공 |

---

##  기술 스택

- **문서 처리**: `PyMuPDF`
- **토큰화**: `tiktoken`
- **임베딩**: `OpenAI Embedding API (text-embedding-ada-002)`
- **검색엔진**: `FAISS`
- **응답 생성**: `OpenAI GPT-3.5-turbo`
- **환경**: Python, Jupyter Notebook


