import fitz  # PyMuPDF
import json
import os
import tiktoken

# 경로 및 파라미터 설정
PDF_PATH = "./data/sample_textbook.pdf"
BLOCKS_PATH = "./data/blocks.json"
CHUNKS_PATH = "./data/chunks.json"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# 토큰 수 계산 함수
def count_tokens(text, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

# PDF에서 블록 추출
def extract_pdf_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    all_blocks = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("blocks")
        for block in blocks:
            x0, y0, x1, y1, text, *_ = block
            if text.strip():
                all_blocks.append({
                    "page": page_num + 1,
                    "x0": x0,
                    "y0": y0,
                    "text": text.strip()
                })

    return all_blocks

# 블록을 chunk로 분할
def chunk_blocks(blocks, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    current_chunk = ""
    current_tokens = 0

    for block in blocks:
        block_text = block["text"]
        tokens = count_tokens(block_text)

        if current_tokens + tokens > chunk_size:
            chunks.append(current_chunk.strip())
            overlap_text = current_chunk[-overlap * 5:]
            current_chunk = overlap_text
            current_tokens = count_tokens(current_chunk)

        current_chunk += " " + block_text
        current_tokens += tokens

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks

# JSON 저장 함수
def save_json(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

# 메인 실행 흐름
if __name__ == "__main__":
    os.makedirs("./data", exist_ok=True)

    blocks = extract_pdf_blocks(PDF_PATH)
    save_json(blocks, BLOCKS_PATH)

    chunks = chunk_blocks(blocks)
    save_json(chunks, CHUNKS_PATH)

    print(f" 완료! 총 {len(chunks)}개 chunk가 생성되었습니다.")
