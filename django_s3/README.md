### 1. IAM
![image](https://user-images.githubusercontent.com/30817924/92573551-ebaf5380-f2c0-11ea-8efd-56d39bf6ce57.png)

> 보안, 자격 증명 및 규정 준수 - IAM 클릭

### 2. 사용자 추가
![image](https://user-images.githubusercontent.com/30817924/92573809-434dbf00-f2c1-11ea-99a5-aa614db94ade.png)

> 사용자 이름 적당히 입력.
> 액세스 유형 - 프로그래밍 방식 액세스 선택

### 3. 그룹생성
![image](https://user-images.githubusercontent.com/30817924/92574017-83ad3d00-f2c1-11ea-9c54-2e95a676b254.png)

> 그룹 이름 적당히 입력.
> 정책 필터에 s3 입력 후 AmazonS3FullAccess 체크

### 4. 태그(다음)

### 5. 검토(다음)

### 6. 생성완료 후 Access Key ID와 Secret access key 보관

### 7. Policy 설정
![image](https://user-images.githubusercontent.com/30817924/92568992-f1a23600-f2ba-11ea-82e6-702ac9f9368a.png)

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::mydjangotestbucket",
                "arn:aws:s3:::mydjangotestbucket/*"
            ]
        }
    ]
}
```

### 8. CORS 구성
![image](https://user-images.githubusercontent.com/30817924/92569489-aa687500-f2bb-11ea-87e3-5f77d9958e96.png)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
