window.onload = function() {
  var token = localStorage.getItem('token');
  if (token) {
      // 토큰이 있으면 새 창을 띄움
      window.open('/show_token/');
  }
};