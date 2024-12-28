from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


def set_model(model_name: str = "gpt-4o-mini"):
    """
    테스트에 사용할 모델을 설정합니다. 사용할 수 있는 모델은 "gpt-4o", "gpt-4o-mini"입니다.

    Parameters:
        model_name (str): 사용할 모델의 이름. 기본값은 "gpt-4o-mini"입니다.

    Returns:
        ChatOpenAI: 설정된 모델을 반환합니다.

    Raises:
        ValueError: 지원하지 않는 모델 이름이 전달된 경우 발생합니다.
    """
    # 지원 가능한 모델과 기본 설정
    supported_models = {
        "gpt-4o": {"model_name": "gpt-4o", "temperature": 0},
        "gpt-4o-mini": {"model_name": "gpt-4o-mini", "temperature": 0},
    }

    # 모델 이름 검증
    if model_name not in supported_models:
        raise ValueError(
            f"Unsupported model_name: {model_name}. Choose from {list(supported_models.keys())}."
        )

    # 모델 초기화
    model_config = supported_models[model_name]
    model = ChatOpenAI(**model_config)

    return model
