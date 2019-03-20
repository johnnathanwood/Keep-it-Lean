
var myElement = document.getElementById('search_text');

myElement.onpaste = function(e) {
  var pastedText = undefined;
  new Promise((resolve, reject) => {
    if (window.clipboardData && window.clipboardData.getData) { 
      pastedText = window.clipboardData.getData('search_text');
    } else if (e.clipboardData && e.clipboardData.getData) {
      pastedText = e.clipboardData.getData('text/plain');
    }
    resolve()
  })
  .then(() => {
    new Promise((resolve, reject) => {
      document.getElementById('search_text').value = pastedText
      resolve()
    })
  })
  .then(() => {
    document.getElementById('searchbutton').click()
  })
};

var input = document.getElementById('search_text');
input.focus();
input.select();
