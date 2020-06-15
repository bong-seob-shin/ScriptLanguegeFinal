import smtplib
from email.mime.text import MIMEText

def SendEmail(EmailAddress, text):

    s = smtplib.SMTP('smtp.gmail.com', 587) # 세션 생성
    s.starttls()    # TLS 보안 시작
    s.login('yongyong9689@gmail.com', '5746857219a')    # 로그인 인증

    # 보낼 메시지 설정
    msg = MIMEText('내용 : 본문내용 테스트입니다.')

    msg['Subject'] = '스크립트언어 기말 프로젝트'
    msg['From'] = '파이썬에서 메일 전송'
    msg['To'] = 'yongyong9689@gmail.com'

    s.sendmail("Python Project", "yongyong9689@gmail.com", msg.as_string()) # 메일 보내기
    s.quit()    # 세션 종료
