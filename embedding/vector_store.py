import os
import json
import numpy as np
import openai
import faiss
from tqdm import tqdm

# 경로 설정
CHUNKS_PATH = "./data/chunks.json"
FAISS_INDEX_PATH = "./data/faiss.index"
EMBEDDINGS_PATH = "./data/embeddings.npy"
CHUNK_METADATA_PATH = "./data/chunk_metadata.json"

# OpenAI 모델 설정
EMBED_MODEL = "text-embedding-ada-002"
openai.api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 불러오기

# 청크 로드
with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
    chunks = json.load(f)
print(f"✅ 총 {len(chunks)}개의 chunk 로드 완료")

# 임베딩 생성 함수
def get_embedding(text, model=EMBED_MODEL):
    response = openai.Embedding.create(
        input=text,
        model=model
    )
    return response["data"][0]["embedding"]

# 전체 청크 임베딩
def embed_chunks(chunks):
    embeddings = []
    for chunk in tqdm(chunks, desc="🔍 Embedding 생성 중"):
        emb = get_embedding(chunk)
        embeddings.append(emb)
    return np.array(embeddings, dtype="float32")

embeddings = embed_chunks(chunks)
print(f"임베딩 shape: {embeddings.shape}")

# FAISS 인덱스 저장
def save_faiss_index(embeddings, path):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, path)

save_faiss_index(embeddings, FAISS_INDEX_PATH)
np.save(EMBEDDINGS_PATH, embeddings)

# 메타데이터 저장
with open(CHUNK_METADATA_PATH, "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

print("FAISS 인덱스 및 메타데이터 저장 완료")
