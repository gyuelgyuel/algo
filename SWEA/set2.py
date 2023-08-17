### SWEA Learn에 있는 문제 input.txt를 받아오기 위한 코드입니다.
### SWEA 폴더 안에 set2.py를 넣어주세요
### SWEA 폴더 안에 .env 파일에 ID, PW가 입력 되어 있어야 합니다.
### <.env> || ID : <your_id>\n PW : <your_pw>
### 실행은 SWEA 폴더로 이동한 뒤, python set2.py로 실행하시면 됩니다.
### 인터넷 브라우저가 실행되면 터미널의 커서가 비활성화 되는데,
### 터미널을 다시 클릭하여 터미널에 커서를 옮겨주세요
### SWEA>Learn 인터넷 창이 켜지고 로그인을 했다면,
### 코스번호,강의목록번호,차시를 입력하여 문제 페이지로 이동해주세요.
### (브라우저에서 직접 클릭하여 이동하면 코드 실행이 안될 수 있습니다.)
### 폴더명을 입력하여 temp로 되어있는 폴더명을 수정해주세요. (ex.5105_maze)
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values
import sys
from sys import argv
import os
import shutil
from pathlib import Path
import time

def main():
    global ID, pw

    ## 파일 경로 작성
    parent_path = Path(__file__).parent
    folder_path = parent_path / 'temp'
    
    # 폴더/파일 생성
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(folder_path)
    f1 = open(folder_path / 'sol.py','w')

    # sol.py 기본 템플릿
    template = '''import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    pass
'''
    # sol.py 작성
    f1.write(template)
    f1.close()

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': str(folder_path)}
    chrome_options.add_experimental_option('prefs',prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # 크롬 드라이버 위치 설정 필요
    browser = webdriver.Chrome(options=chrome_options)
    
    browser.get("https://swexpertacademy.com/main/learn/course/courseList.do#none")
    
    # login
    account = browser.find_element(by.XPATH, '/html/body/nav/div[2]/div/div[2]/a[2]')
    account.click()

    config = dotenv_values('.env')

    ID = config.get("ID")
    pw = config.get("PW")        
        
    if not ID:
        ID = input("ID를 입력하세요 : ")
    else:
        print("ID가 입력되었습니다.")
        
    if not pw:
        pw = input("비밀번호를 입력하세요 : ")
    else:
        print("비밀번호가 입력되었습니다.")
    
    login = browser.find_element(by.XPATH, '//*[@id="id"]')
    login.click()
    login.clear()
    login.send_keys(ID)
    password = browser.find_element(by.XPATH, '//*[@id="pwd"]')
    password.click()
    password.clear()
    password.send_keys(pw)
    confirm = browser.find_element(by.XPATH, '//*[@id="LoginForm"]/div/div/div[2]/div/div/fieldset/div/div[4]/button')
    confirm.click()  

    # 코스 번호 선택
    course_select = input(
        '''Course 번호를 입력해주세요
        1:Computational Thinking    2:Programming Beginner
        3:Programming Intermediate, 4:Programming Advanced
        5:Programming Professional, 6:Programming-Solving
        7:Computer Science          8:Other SW Learning Site\n''')
    course = browser.find_element(by.XPATH, '/html/body/div[4]/div[4]/div/div/div/div/div['+course_select+']/a')
    course.click()

    # 강의목록 번호 선택 (목록밖의 번호 입력시 input.txt 받지 않음)
    try:
        list_select = input('강의목록 번호를 입력해주세요 (번호는 1부터 시작하며 순서는 왼쪽에서 오른쪽, 위에서 아래로입니다.)\n')
        list_search = browser.find_element(by.XPATH, '/html/body/div[4]/div[1]/div/ul/li['+list_select+']/a')
        list_search.click()

        try:
            lecture_select = input('차시 번호를 입력해주세요\n')
            lecture_search = browser.find_element(by.XPATH, '/html/body/div[4]/div/div/div[7]/ul/li['+lecture_select+']/div/a')
            lecture_search.click()

            ## input 파일 다운받기  
            try:
                down = browser.find_element(by.XPATH, '/html/body/div[4]/div/div/div[5]/div[2]/div[4]/div[1]/div[1]/div')
                down.click()
                ## 다운로드 대기 (만약 3초 안에 다운이 완료되지 않는 경우 3초보다 큰 값으로 늘리세요)
                time.sleep(3)
                ## input 파일명 input.txt로 변경 (ex. samle_input.txt)
                for file in os.listdir(folder_path):
                    if file.endswith('input.txt'):
                        old_file_path = folder_path / file
                        new_file_path = folder_path / 'input.txt'
                        os.rename(old_file_path,new_file_path)

                ## 폴더 이름 입력받고 변경
                folder_name = input("폴더 이름을 입력해주세요\n")
                if os.path.exists(parent_path / folder_name):
                    shutil.rmtree(parent_path / folder_name)
                for folder in os.listdir(parent_path):
                    if folder.endswith('input.txt'):
                        old_folder_path = parent_path / 'temp'
                        new_folder_path = parent_path / folder_name
                        os.rename(old_folder_path,new_folder_path)

            except NoSuchElementException:
                print("input 파일이 없습니다.")
        except NoSuchElementException:
            print("해당차시가 없습니다.")
    except NoSuchElementException:
        print("번호에 해당하는 강의가 없습니다.")
    print("프로그램이 완료되었습니다.\nshell 명령을 자유롭게 실행하세요\ncurrent dic:{parent_path}\n")
    os.system(f'echo -e "\033[40;33mset2.py working (q:quit, h:help)\033[0m"')
    inp = input(f"$ ")
    while inp != 'q':
        if inp == 'h':
            print('종료하시려면 q를 입력해주세요. 다른 입력문자는 쉘명령으로 그대로 입력됩니다.')
        else:
            os.system(inp)
        os.system(f'echo -e "\033[40;33mset2.py working (q:quit, h:help)\033[0m"')
        inp = input('$ ')
    
if __name__ == '__main__':
    main()
    