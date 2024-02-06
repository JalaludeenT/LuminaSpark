const passField = document.querySelector('.pass-key');
      const passFieldConfirm = document.querySelector('.c-pass-key');
      const showBtn = document.querySelector('.show');
      const showBtnConfirm = document.querySelector('.c-show');
      showBtn.addEventListener('click', togglePasswordVisibility);
      showBtnConfirm.addEventListener('click', togglePasswordVisibilityConfirm);

      function togglePasswordVisibility() {
        if (passField.type === 'password') {
            passField.type = 'text';
            showBtn.textContent = 'HIDE';
            showBtn.style.color = '#3498db';
        }
        else {
            passField.type = 'password';
            showBtn.textContent = 'SHOW';
            showBtn.style.color = '#222';
        }
      }

      function togglePasswordVisibilityConfirm() {
      if (passFieldConfirm.type === 'password') {
            passFieldConfirm.type = 'text';
            showBtnConfirm.textContent = 'HIDE';
            showBtnConfirm.style.color = '#3498db';
         }
         else {
            passFieldConfirm.type = 'password';
            showBtnConfirm.textContent = 'SHOW';
            showBtnConfirm.style.color = '#222';
         }
      }