# 공통 모듈 사용시 활용할 함수 (추후 리팩토링 필요)

import json
import tiktoken

# ✅ 1. 토큰 수 세기
def count_tokens(text, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

# ✅ 2. JSON 저장
def save_json(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

# ✅ 3. JSON 로드
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
