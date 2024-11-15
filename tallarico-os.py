from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText

# Config file for login and password
import config

posts_acompanhados = {
    '@teste1': 'url1',
    '@teste2': 'url2', 
    '@teste3': 'url3'
}

driver = webdriver.Chrome()

posts_removidos = []

for key in posts_acompanhados:
    print ("Checando post " + key + "...")
    driver.get(posts_acompanhados[key])
    
    driver.implicitly_wait(10)
    
    try:
        post = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/span')
        if post:
            print("Post de " + key + " foi removido")
            posts_removidos.append(key)
    except:
        print("Post de " + key + " nao foi removido")

subject = "Posts excluidos (TallaricoOS)"
body = "Posts removiods:\n" + ",".join(posts_removidos)
sender = config.sender
recipients = ["recipient1",]
password = config.password

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = ', '.join(recipients)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
   smtp_server.login(sender, password)
   smtp_server.sendmail(sender, recipients, msg.as_string())
print("Mensagem enviada!")