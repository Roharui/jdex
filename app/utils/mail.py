if __name__ == "__main__":
    from dotenv import load_dotenv

    # 환경변수 로드
    load_dotenv()

# 라이브러리 불러오기
import os
import smtplib

# 개인 정보 입력(email, 앱 비밀번호)
my_email = os.getenv('MY_EMAIL')
password = os.getenv('SMTP_PW')

def send_email(to_addrs, subject, body):
  if my_email is None or password is None:
    raise ValueError("Environment variables MY_EMAIL and SMTP_PW must be set")

  # 방법 2(with 사용)
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #Transport Layer Security : 메시지 암호화
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=to_addrs, 
        msg=f"Subject:{subject}\n\n{body}"
    )

if __name__ == "__main__":
    send_email(input("Send Email To: "), "정동 익스프레스 비밀번호 설정", "정동 익스프레스 이메일 세팅")  # 테스트용