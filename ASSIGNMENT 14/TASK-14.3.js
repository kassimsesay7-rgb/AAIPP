// Simple client-side validation for login form (non-empty username & password)

window.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('loginForm');
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    var errorMsg = document.getElementById('errorMsg');

    if (!form || !username || !password || !errorMsg) {
        // required elements not found; nothing to do
        return;
    }

    // Clear error when user types
    function clearError() {
        errorMsg.textContent = '';
        errorMsg.classList.remove('error');
    }
    username.addEventListener('input', clearError);
    password.addEventListener('input', clearError);

    form.addEventListener('submit', function (e) {
        e.preventDefault(); // stop default submit to validate first

        var userVal = username.value.trim();
        var passVal = password.value.trim();

        if (!userVal || !passVal) {
            if (!userVal && !passVal) {
                errorMsg.textContent = 'Please enter username and password.';
                username.focus();
            } else if (!userVal) {
                errorMsg.textContent = 'Please enter username.';
                username.focus();
            } else {
                errorMsg.textContent = 'Please enter password.';
                password.focus();
            }
            errorMsg.classList.add('error');
            return;
        }

        // Passed validation — proceed (uncomment to allow actual submit)
        // form.submit();

        // For demonstration: you can replace with actual login handling
        errorMsg.textContent = '';
        alert('Validation passed. Submitting form...'); // optional
        form.submit();
    });
});