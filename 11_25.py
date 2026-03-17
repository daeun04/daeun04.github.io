<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>모바일 웹 페이지</title>

<style>
body{
    margin:0;
    font-family:Arial, sans-serif;
}

header{
    background:#333;
    color:white;
    text-align:center;
    padding:15px;
}

section{
    padding:20px;
    border-bottom:2px solid #ddd;
}

.gallery{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
}

.gallery img{
    width:100%;
    max-width:150px;
    border-radius:8px;
}

footer{
    background:#333;
    color:white;
    text-align:center;
    padding:15px;
    font-size:14px;
}
</style>

</head>
<body>

<header>
<h1>모바일 웹 페이지</h1>
</header>

<!-- 첫번째 섹션 : 컴퓨터 보안 소개 -->
<section id="security">
<h2>컴퓨터 보안 소개</h2>
<p>
컴퓨터 보안은 시스템과 네트워크, 데이터를 보호하기 위한 기술과 정책을 의미합니다.
주요 내용에는 암호화, 인증, 접근 제어, 악성코드 방지 등이 포함됩니다.
</p>
</section>

<!-- 두번째 섹션 : 내 수업 정보 -->
<section id="class">
<h2>내 수업 정보</h2>
<ul>
<li>웹 프로그래밍</li>
<li>인공지능 기초</li>
<li>데이터베이스</li>
<li>컴퓨터 네트워크</li>
</ul>
</section>

<!-- 세번째 섹션 : 갤러리 -->
<section id="gallery">
<h2>갤러리</h2>
<div class="gallery">
<img src="image1.jpg" alt="사진1">
<img src="image2.jpg" alt="사진2">
<img src="image3.jpg" alt="사진3">
</div>
</section>

<!-- 네번째 섹션 : 연락처 및 저작권 -->
<section id="contact">
<h2>연락처</h2>
<p>Email: example@email.com</p>
<p>Phone: 010-0000-0000</p>
</section>

<footer>
<p>© 2026 웹 페이지 제작자. All Rights Reserved.</p>
</footer>

</body>
</html>