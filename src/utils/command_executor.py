import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return f"成功: {result.stdout}"
        else:
            return f"エラー: {result.stderr}"
    except Exception as e:
        return f"実行中に例外が発生しました: {str(e)}"
