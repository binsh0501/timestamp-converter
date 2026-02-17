'''
python.timestamp의 Docstring

심심풀이용으로 개발 시작하게 된 타임스탬프 변환기입니다.
'''
from math import trunc
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9), name="KST")

def print_dt(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def print_timestamp_to_datetime(utc, kst):
    print(f'{utc.tzinfo} {print_dt(utc)}')
    print(f'{kst.tzinfo} {print_dt(kst)}')

# 사용자에게 제공되는 메뉴 화면
def user_interface():
    while True:
        print('=== timestamp converter ===')
        print('1. 현재 시간')
        print('2. 사용자 입력')
        print('3. 종료')
        print('>> ', end='')
        try:
            input_user = int(input())
        except ValueError:
            print("올바른 번호를 입력하세요.")
            continue
        if input_user == 1:
            current_timestamp_converter()
        elif input_user == 2:
            user_input_timestamp_converter()
        elif input_user == 3:
            break
        else:
            continue
    
# 현재 타임스탬프 기준으로 변환
def current_timestamp_converter():
    now_utc = datetime.now(timezone.utc)
    now_kst = datetime.now(KST)
    timestamp = trunc(now_utc.timestamp())
    print(f"현재 타임스탬프 : {timestamp}")
    print_timestamp_to_datetime(now_utc, now_kst)

# 사용자에게 입력 받은 타임스탬프 기준으로 변환
def user_input_timestamp_converter():
    try:
        input_timestamp = int(input(f'타임스탬프 입력(예 : {trunc(datetime.now(timezone.utc).timestamp())})\n>> '))
    except ValueError:
        print("올바르지 않은 타임스탬프 값입니다.")
        return
    now_utc = datetime.fromtimestamp(input_timestamp, tz=timezone.utc)
    now_kst = datetime.fromtimestamp(input_timestamp, tz=KST)
    print_timestamp_to_datetime(now_utc, now_kst)

def main():
    # os.system("cls")
    user_interface()

if __name__ == '__main__':
    main()