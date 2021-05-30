const loginSubmit = function(form) {
  document.getElementById('wrong').style.display = 'none';
  const formData = new FormData(form); // Ajax로 백엔드에 데이터를 넘겨주는 오브젝트
  const xhrObject = new XMLHttpRequest();// 페이지 초기화 없이 백엔드에 넘겨주고 받음
  xhrObject.onreadystatechange = function() {
    if (xhrObject.readyState !== 4) return; // 통신 상태에 따라 xhrObject.readyState 값이 변하면 호출되는 함수
    if (xhrObject.status === 200) {
      // 통신 완료 후 실행할 부분
      console.log('Done', xhrObject.responseText); //콘솔 창에만 보여주기
      const result = JSON.parse(xhrObject.responseText); //텍스트를 json형태로 변경
      if (!result.done) { //result.done이 true가 아닐 경우
        document.getElementById('wrong').style.display = 'inline'; // 틀렸을 경우 메시지 보여주기
      } else {
        window.location.href = '/mypage'; // todo: 로그인 후 이동 페이지 
      }
    } else {
      // 통신 도중 에러가 발생 할때 실행할 부분
      const error = {
        status: xhrObject.status,
        statusText: xhrObject.statusText,
        responseText: xhrObject.responseText
      }
      console.error(error);
      alert('서버에서 에러가 발생했습니다.');
    }
  };
  xhrObject.open('POST', '');
  // xhrObject.setRequestHeader('Content-Type', 'application/json');
  xhrObject.send(formData);
}

$('.blinking').on('click', function () {
  $('.login-form > div').fadeIn(300, function () {
  });
  $('.login-form > div').addClass(
      'on');
});
$('.blinking').on('click', function () {
  $('.login-form > div').fadeOut(300);
  $('.login-form > div').removeClass(
      'on');
});

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
