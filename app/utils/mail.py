if __name__ == "__main__":
    from dotenv import load_dotenv

    # 환경변수 로드
    load_dotenv()

# 라이브러리 불러오기
import os
from smtplib import SMTP
from email.mime.text import MIMEText

# 개인 정보 입력(email, 앱 비밀번호)
my_email = os.getenv('MY_EMAIL')
password = os.getenv('SMTP_PW')

def send_email(to_addrs, body):
  if my_email is None or password is None:
    raise ValueError("Environment variables MY_EMAIL and SMTP_PW must be set")

  msg = MIMEText(body)
  msg['Subject'] = "정동 익스프레스 비밀번호 설정"
  msg['From'] = my_email
  msg['To'] = to_addrs

  # 방법 2(with 사용)
  with SMTP("smtp.gmail.com") as connection:
    connection.starttls() #Transport Layer Security : 메시지 암호화
    connection.login(user=my_email, password=password)
    connection.sendmail(
      from_addr=my_email,
      to_addrs=to_addrs,
      msg=msg.as_string()
    )

if __name__ == "__main__":
    send_email(input("Send Email To: "), "테스트 이메일")  # 테스트용