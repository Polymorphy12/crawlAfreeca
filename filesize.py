import os

totalKB = 0

for i in range(0,1711):
    try:
        n = os.path.getsize("C://Users/Sumin/Desktop/study/crawling/thumbnails/afreeca/"+ str(i)+".jpg")
        print(n, "Bytes")                           # 바이트 단위로 구하기
        print(n / 1024, "KB")                       # 킬로바이트 단위로
        print("%.2f MB" % (n / (1024.0 * 1024.0)))  # 메가바이트 단위
        totalKB += n/1024
    except os.error:
        print("파일이 없거나 에러입니다.")

print(totalKB, " ", totalKB/1710.0)

