temp = int(input("기온은 어때요?"))
if 28 < temp :
    print("더워요 반팔 입으세요.")
elif 10<  temp and temp < 20 :
    print("좋은 날씨네요 얇은 아우터를 입으세요.")
elif 0< temp and temp < 10 :
    print("춥네요 코트를 입으세요.")
else :
    print("추우니까 이불 밖을 나가지 마세요")
