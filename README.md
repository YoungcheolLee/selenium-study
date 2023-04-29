# 크롬 크롤링 자동화테스트

#### Chrome 브라우저를 실행하고 "QA" 이미지를 검색합니다.
#### 검색결과 이미지를 크롤링하는 과정을 자동화 하여 이미지 다운로드 기능이 정상적으로 수행되는지 확인합니다. 

<br/>

가상 환경 생성 </br>
`phtyon -m venv "파일명"`

## 기술스택

- python
- selenium

## Preview


https://user-images.githubusercontent.com/107835019/234367551-767af2d4-ad26-417f-adf1-142235d145c9.mp4


<br/>


## 구현기능

### ▣ 이미지 다운로드 경로 설정
![image](https://user-images.githubusercontent.com/107835019/234354983-847a658d-6bc2-4213-b590-d690b24296c6.png)

<br/>


### ▣ 브라우저 강제 종료 방지 코드 추가

![image](https://user-images.githubusercontent.com/107835019/234358509-b49ffefc-053a-468f-9fd1-620ab69b543d.png)

<br/>


### ▣ 크롬 실행

![image](https://user-images.githubusercontent.com/107835019/234358742-4d82e0c1-2b79-4daa-b2b3-40e3b6c99f0e.png)

<br/>

### ▣ 크롬 브라우저 최대화

![image](https://user-images.githubusercontent.com/107835019/234359119-45bbcfd7-e685-48a7-a8e6-521e82c95cab.png)

<br/>


### ▣ 검색창 name property 명 확인

![image](https://user-images.githubusercontent.com/107835019/234079334-15bf0f12-3965-46d2-9b68-00b6ca89a394.png)

<br/>


### ▣ 검색창 선택

![image](https://user-images.githubusercontent.com/107835019/234359416-270e73da-4274-4027-ba48-ec34635a7f92.png)

<br/>


### ▣ 검색창에 "QA" 문구 입력

![image](https://user-images.githubusercontent.com/107835019/234359554-7b594f02-9bbe-40c0-adce-9fad8175685b.png)

<br/>


### ▣ Enter key 선택

![image](https://user-images.githubusercontent.com/107835019/234359720-ce571790-88ce-40a5-8f47-ceab454e8451.png)

<br/>


### ▣ CSS class 명 확인

![image](https://user-images.githubusercontent.com/107835019/234360574-abf8f933-bb22-423e-a3d0-969ac7413d88.png)

<br/>


### ▣ 확인한 CSS class 모두 선택

![image](https://user-images.githubusercontent.com/107835019/234360867-3217389b-b62c-4bd5-810c-96d4572cdaa8.png)

<br/>

### ▣ 이미지 다운로드

![image](https://user-images.githubusercontent.com/107835019/234361310-287680ab-583e-43a3-bc52-18e3566f022b.png)

<br/>

#### 반복문을 사용해 `wXeWr islib nfEiy` class 명을 가진 모든 이미지 다운로드

1. ```count = 1``` <br/>
 - 저장할 이미지 번호를 붙이기 위해 count 변수 생성 <br/>
  
2. ```image.click()``` <br/>
 - image 클릭 <br/>

3. ```time.sleep(3)``` <br/>
 - 이미지 로드되는 시간 3초 부여 <br/>

4. ```imgUrl = driver.find_element(By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb").get_attribute("src")``` <br/>
 - `r48jcc pT0Scc iPVvYb` 클래스 명을 가진 요소의 이미지 주소 imgUrl 변수에 저장 <br/>

5. ```image_path = os.path.join(img_folder, "crawling" + str(count) + ".jpg")``` <br/>
 - 이미지 다운로드 시 폴더 경로와 이미지명 설정 <br/>
 - 경로 : `img_folder`
 - 이미지명 : crawling1.jpg <br/>

6. ```urllib.request.urlretrieve(imgUrl, image_path)``` <br/>
 - 이미지 저장하는 구문
 - 이미지 저장 시 5번에서 설정한 폴더 경로와 설정한 이름으로 이미지 저장

7. ```count = count + 1``` <br/>
 - 반복문이 돌아가면서 이미지 저장 시 이미지명에 숫자 증가하는 구문
 - Ex) 첫 번째 반복문 crawling1.jpg , 두 번째 반복문 crawling2.jpg ....
