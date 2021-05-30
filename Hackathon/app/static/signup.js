const getOTP = function(button) {
  const email = button.form['email'].value; // 이메일의 value 값
  if (!email) { //이메일이 없다면
    alert('이메일을 입력하세요.');
    return;
  }
  button.disabled = true; 
  const xhrObject = new XMLHttpRequest(); // Ajax 객체 생성, 통신 단계마다 값들이 달라짐
  xhrObject.onreadystatechange = function() {
    if (xhrObject.readyState !== 4) return; // readystate부분에 4가 떠야지 통신완료/ 아니면 오류
    if (xhrObject.status === 200) { // 200이 올바른 통신 완료
      // 통신 완료 후 실행할 부분
      console.log('Done', xhrObject.responseText); // 백엔드에서 넘겨받은 문자를 xhrObject.responseText로 받는다
      window.OTP = JSON.parse(xhrObject.responseText).opt //문자열을 오브젝트로 수정
      button.innerHTML = '발송 완료';
    } else {
      // 통신 도중 에러가 발생 할때 실행할 부분
      const error = { 
        status: xhrObject.status, 
        statusText: xhrObject.statusText,
        responseText: xhrObject.responseText
      }
      console.error(error);
      alert('인증번호 발송이 실패했습니다.');
      button.disabled = false;
    }
  };
  xhrObject.open('GET', '/email/opt?email=' + email);
  xhrObject.setRequestHeader('Content-Type', 'application/json');
  xhrObject.send();
}

const signupSubmit = function() {
  const form = document.getElementById('signup-form');
  if (!form['username'].value) {
    alert('이름을 입력하세요.');
    form['username'].focus();
    return;
  }
  if (!form['id'].value) {
    alert('아이디를 입력하세요.');
    form['id'].focus();
    return;
  }
  if (!form['password'].value) {
    alert('비밀번호를 입력하세요.');
    form['password'].focus();
    return;
  }
  // if (form['password'].value !== form['password_confirm'].value) {
  //   alert('비밀번호가 일치하지 않습니다.');
  //   form['password'].focus();
  //   return;
  // }
  if (!form['nickname'].value) {
    alert('닉네임을 입력하세요.');
    form['nickname'].focus();
    return;
  }
  if (!form['email'].value) {
    alert('이메일을 입력하세요.');
    form['email'].focus();
    return;
  }
  if (!form['opt_button'].disabled) {
    alert('인증번호 받기를 눌러 주세요.');
    form['opt_button'].focus();
    return;
  }
  if (!form['opt'].value) {
    alert('인증번호를 넣어주세요.');
    form['opt'].focus();
    return;
  }
  document.getElementById('same_id').style.display = 'none';
  document.getElementById('not_same_password').style.display = 'none';
  document.getElementById('same_nickname').style.display = 'none';
  document.getElementById('same_email').style.display = 'none';
  document.getElementById('not_same_opt').style.display = 'none';
  const formData = new FormData(form); // Ajax로 백엔드에 데이터를 넘겨주는 오브젝트
  console.log(formData);
  const xhrObject = new XMLHttpRequest();// 페이지 초기화 없이 백엔드에 넘겨주고 받음
  xhrObject.onreadystatechange = function() {
    if (xhrObject.readyState !== 4) return; // 통신 상태에 따라 xhrObject.readyState 값이 변하면 호출되는 함수
    if (xhrObject.status === 200) {
      // 통신 완료 후 실행할 부분
      console.log('Done', xhrObject.responseText);
      const result = JSON.parse(xhrObject.responseText);
      if (result.error) {
        for (let key in result.error) {
          document.getElementById(key).style.display = 'block';
        }
      } else {
        window.location.href = '/signup_done';
      }
    } else {
      // 통신 도중 에러가 발생 할때 실행할 부분
      const error = {
        status: xhrObject.status,
        statusText: xhrObject.statusText,
        responseText: xhrObject.responseText
      }
      console.error(error);
      alert('서버에서 에러가 발생 하였습니다.');
    }
  };
  xhrObject.open('POST', '');
  // xhrObject.setRequestHeader('Content-Type', 'application/json');
  xhrObject.send(formData);
}

jQuery(function($) {
  $("body").css("display", "none");
  $("body").fadeIn(2000);
  $("a.transition").click(function(event){
  event.preventDefault();
  linkLocation = this.href;
  $("body").fadeOut(1000, redirectPage);
  });
  function redirectPage() {
  window.location = linkLocation;
  }
  });