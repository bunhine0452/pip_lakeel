from lakeel import GGUFChat
import os

def test_llama_chat():
    # 모델 경로 설정 (환경 변수나 직접 경로 지정)
    model_path = os.getenv('LLAMA_MODEL_PATH', 'llama-3.2-3b-instruct.gguf')
    
    try:
        # 채팅 모델 초기화
        chat = GGUFChat(model_path=model_path)
        
        print("\n=== 기본 채팅 테스트 ===")
        prompts = [
            "안녕하세요! 자기소개 해주세요.",
            "파이썬으로 'Hello, World!'를 출력하는 코드를 작성해주세요.",
            "인공지능에 대해 설명해주세요."
        ]
        
        # 일반 채팅 테스트
        for prompt in prompts:
            print(f"\n사용자: {prompt}")
            response = chat.chat(prompt, max_tokens=512)
            print(f"AI: {response}")
            
        # 스트리밍 채팅 테스트
        print("\n=== 스트리밍 채팅 테스트 ===")
        prompt = "미래의 기술 발전에 대해 설명해주세요."
        print(f"\n사용자: {prompt}")
        print("AI: ", end='', flush=True)
        
        for token in chat.chat_stream(prompt, max_tokens=512):
            print(token, end='', flush=True)
        print("\n")
        
    except Exception as e:
        print(f"오류 발생: {str(e)}")

if __name__ == "__main__":
    test_llama_chat()