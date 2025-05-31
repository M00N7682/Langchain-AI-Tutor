import os
import json
import openai
import numpy as np
import faiss

# 모델 설정
EMBED_MODEL = "text-embedding-ada-002"
LLM_MODEL = "gpt-3.5-turbo"

# 파일 경로 설정
FAISS_INDEX_PATH = "./data/faiss.index"
EMBEDDINGS_PATH = "./data/embeddings.npy"
CHUNK_METADATA_PATH = "./data/chunk_metadata.json"

# OpenAI 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 텍스트 임베딩
def get_embedding(text, model=EMBED_MODEL):
    response = openai.Embedding.create(
        input=text,
        model=model
    )
    return response["data"][0]["embedding"]

# LLM 응답 생성
def ask_llm(context, question):
    system_prompt = (
        "You are a helpful tutor that answers only using the provided context. "
        "If the answer is not in the context, say '정보가 부족합니다'."
    )
    user_prompt = f"""[Context]\n{context}\n\n[Question]\n{question}"""

    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
    )
    return response["choices"][0]["message"]["content"]

# FAISS 인덱스 및 청크 불러오기
index = faiss.read_index(FAISS_INDEX_PATH)
with open(CHUNK_METADATA_PATH, "r", encoding="utf-8") as f:
    chunks = json.load(f)

# 질문에 가장 유사한 청크 검색
def search_similar_chunks(question, top_k=3):
    question_emb = np.array([get_embedding(question)], dtype="float32")
    distances, indices = index.search(question_emb, top_k)
    results = [chunks[i] for i in indices[0]]
    return "\n\n---\n\n".join(results)

# 테스트 실행
if __name__ == "__main__":
    question = "AHP 분석이 교재에서 어떻게 설명되어 있나요?"
    context = search_similar_chunks(question)
    answer = ask_llm(context, question)

    print(" 질문:", question)
    print("\n Context Preview:\n", context[:300], "...")
    print("\n 응답:\n", answer)
