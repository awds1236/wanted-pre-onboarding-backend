/*변수 선언*/


var pw1 = document.querySelector('#pswd1');
var pwMsg = document.querySelector('#alertTxt');
var pwImg1 = document.querySelector('#pswd1_img1');
var pw2 = document.querySelector('#pswd2');
var pwImg2 = document.querySelector('#pswd2_img1');
var pwMsgArea = document.querySelector('.int_pass');
var email = document.querySelector('#email');
var error = document.querySelectorAll('.error_next_box');

var idPattern = /[a-zA-Z0-9_-]{5,2  0}/;
var pwPattern = /[a-zA-Z0-9~!@#$%^&*()_+|<>?:{}]{8,16}/;
var namePattern = /[a-zA-Z가-힣]/;
var emailPattern = /[a-z0-9]{2,}@[a-z0-9-]{2,}\.[a-z0-9]{2,}/;
var isPhoneNum = /^010[0-9]{8}$/;


pw1.addEventListener("change", checkPw);
pw2.addEventListener("change", comparePw);

email.addEventListener("change", isEmailCorrect);


/*콜백 함수*/


function isEmailCorrect() {
    var emailPattern = /[a-z0-9]{2,}@[a-z0-9-]{2,}\.[a-z0-9]{2,}/;

    if(email.value === ""){ 
        error[0].style.display = "none"; 
    } else if(!emailPattern.test(email.value)) {
        error[0].innerHTML = "올바른 이메일 형식이 아닙니다.";
        error[0].style.display = "block";
    } else {
        error[0].style.display = "none"; 
    }

}


function checkPw() {
    var pwPattern = /[a-zA-Z0-9~!@#$%^&*()_+|<>?:{}]{8,16}/;
    if(pw1.value === "") {
        error[1].innerHTML = "필수 정보입니다.";
        pwMsg.style.display = "block";
        pwMsgArea.style.paddingRight = "40px";

        error[1].style.display = "block";
    } else if(!pwPattern.test(pw1.value)) {
        error[1].innerHTML = "8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요.";
        pwMsg.innerHTML = "사용불가";
        pwMsgArea.style.paddingRight = "93px";
        error[1].style.display = "block";
        pwMsg.style.color = "red";
        pwMsg.style.display = "block";
    } else {
        error[1].style.display = "none";
        pwMsg.innerHTML = "안전";
        pwMsgArea.style.paddingRight = "93px";
        pwMsg.style.color = "#03c75a";
        pwMsg.style.display = "block";
    }
}

function comparePw() {
    if(pw2.value === pw1.value) {
        error[2].style.display = "none";
    } else if(pw2.value !== pw1.value) {
        error[2].innerHTML = "비밀번호가 일치하지 않습니다.";
        error[2].style.display = "block";
    } 

    if(pw2.value === "") {
        error[2].innerHTML = "필수 정보입니다.";
        error[2].style.display = "block";
    }
}


document.querySelector('form').addEventListener("submit", function(event) {
    event.preventDefault();
    var pswd1 = document.querySelector("#pswd1").value;
    var pswd2 = document.querySelector("#pswd2").value;
    var email = document.querySelector("#email").value;

    var emailPattern = /[a-z0-9]{2,}@[a-z0-9-]{2,}\.[a-z0-9]{2,}/;  // 이메일 패턴
    var pwPattern = /^(?=.*[a-zA-Z])(?=.*\d).{8,}$/;


    if (pswd1 === "" || pswd2 === "" || email === "") {
        alert("필수 정보를 모두 입력해주세요.");
        event.preventDefault(); // 폼 제출을 막습니다.
    }

    else if (!emailPattern.test(email)) {  // 이메일 패턴 검사
        alert("올바른 이메일 형식이 아닙니다.");
        event.preventDefault(); // 폼 제출을 막습니다.
    }

    else if (!pwPattern.test(pswd1)) {  // 비밀번호 패턴 검사
        alert("비밀번호는 영어와 숫자를 포함한 8자리 이상의 문자여야 합니다.");
        event.preventDefault(); // 폼 제출을 막습니다.
    }

    else if (pswd1 !== pswd2) {
        alert("비밀번호를 확인해주세요.");
        event.preventDefault(); // 폼 제출을 막습니다.
    }
    else {
        alert("가입이 완료되었습니다.");
        document.querySelector('form').submit();
    }
});
