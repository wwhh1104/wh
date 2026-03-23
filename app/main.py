from app.services.chat_service import ChatService
from app.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info("程序启动")

    service = ChatService()

    print("欢迎使用命令行 LLM 助手")
    print("输入 exit 退出\n")

    while True:
        user_input = input("你: ").strip()

        if not user_input:
            print("请输入内容")
            continue

        if user_input.lower() == "exit":
            logger.info("用户退出程序")
            print("再见")
            break

        try:
            answer = service.ask(user_input)
            print(f"\n助手: {answer}\n")
        except Exception:
            print("\n助手: 调用失败，请检查日志和配置。\n")


if __name__ == "__main__":
    main()