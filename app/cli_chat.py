import os
import openai
import numpy as np
import faiss
from utils.common import load_json, get_embedding, ask_llm

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 파일 경로
FAISS_INDEX_PATH = "./data/faiss.index"
CHUNK_METADATA_PATH = "./data/chunk_metadata.json"

# 인덱스 및 청크 로드
index = faiss.read_index(FAISS_INDEX_PATH)
chunks = load_json(CHUNK_METADATA_PATH)

# 검색 함수
def search_chunks(question, top_k=3):
    q_emb = np.array([get_embedding(question)], dtype="float32")
    distances, indices = index.search(q_emb, top_k)
    return [chunks[i] for i in indices[0]]

# 실행 부분
if __name__ == "__main__":
    question = input("질문을 입력하세요: ")
    context = "\n\n---\n\n".join(search_chunks(question))
    print("📚 Context:\n", context[:500])  # 미리보기 출력
    answer = ask_llm(context, question)
    print("🧠 GPT 응답:\n", answer)
