
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
