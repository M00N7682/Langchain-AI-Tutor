# 📚 AI Tutor for Course PDFs using RAG

> **학교 수업 PDF를 전처리하고, RAG(Retrieval-Augmented Generation) 기반 챗봇에 학습시켜 질의응답을 수행하는 AI Agent 프로젝트입니다.**

---

## 🧠 프로젝트 소개

이 프로젝트는 대학 수업에서 제공된 PDF 교재를 효율적으로 활용하기 위한 AI Agent입니다.  
PDF 파일을 전처리하고, 내용을 검색 가능하게 변환한 후, RAG 구조를 통해 질의응답이 가능한 소프트웨어를 구축하였습니다.

### ✅ 주요 기능
- 수업 교재 PDF 자동 텍스트 추출 및 정제
- 문서 chunking 및 벡터화(Vectorization)
- RAG 기반 AI 챗봇을 통한 질문 응답
- LangChain과 OpenAI API 연동

---

## 🛠 기술 스택

| 분야        | 기술 |
|-------------|------|
| 언어        | Python |
| 문서 처리   | PyMuPDF, LangChain, tiktoken |
| 검색 인덱싱 | FAISS |
| AI 모델     | OpenAI GPT-4 (RAG 구조 활용) |
| 프레임워크  | LangChain |
| 기타        | Streamlit (선택), dotenv |
