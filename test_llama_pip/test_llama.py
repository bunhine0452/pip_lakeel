from llama_cpp import Llama

# GGUF 모델 로드
llm = Llama(
    model_path="./models/your_model.gguf",  # GGUF 파일 경로
    n_ctx=2048,  # 컨텍스트 길이
    n_threads=4  # 사용할 스레드 수
)

# 기본 추론 테스트
prompt = "인공지능이란 무엇인가요?"
output = llm(
    prompt,
    max_tokens=256,
    temperature=0.7,
    top_p=0.95,
    stop=["Human:", "\n"],
    echo=True
)

print("응답:", output['choices'][0]['text'])

# 채팅 형식 테스트
messages = [
    {"role": "system", "content": "당신은 도움이 되는 AI 어시스턴트입니다."},
    {"role": "user", "content": "파이썬으로 'Hello World'를 출력하는 코드를 작성해주세요."}
]

chat_response = llm.create_chat_completion(
    messages=messages,
    temperature=0.7,
    max_tokens=256
)

print("\n채팅 응답:", chat_response['choices'][0]['message']['content'])