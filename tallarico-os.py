from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText

# Config file for sensitive data
import config

posts_acompanhados = config.posts_acompanhados
stories_acompanhados = config.stories_acompanhados

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

stories_removidos = []
for key in stories_acompanhados:
    print ("Checando stories " + key + "...")
    driver.get(stories_acompanhados[key])
    
    driver.implicitly_wait(10)
    
    try:
        post = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/span')
        if post:
            print("Post de " + key + " foi removido")
            stories_removidos.append(key)
    except:
        print("Post de " + key + " nao foi removido")

subject = "Posts excluidos (TallaricoOS)"
body = "Posts removiods:\n" + ",".join(posts_removidos) + "\n\nStories removidos:\n" + ",".join(stories_removidos)
sender = config.sender
recipients = config.recipients
password = config.password

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = ', '.join(recipients)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
   smtp_server.login(sender, password)
   smtp_server.sendmail(sender, recipients, msg.as_string())
print("Mensagem enviada!")