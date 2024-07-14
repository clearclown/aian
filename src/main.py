import os
from utils import chatgpt, command_executor

def main():
    while True:
        user_input = input("何をしたいですか？: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        command = chatgpt.generate_command(user_input)
        if command:
            confirm = input(f"次のコマンドを実行しますか？ {command} (YES/NO): ")
            if confirm.lower() == 'yes':
                result = command_executor.execute_command(command)
                print(result)

if __name__ == "__main__":
    main()
