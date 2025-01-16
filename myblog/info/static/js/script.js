// script.js

// Function to validate the login form
function validateLoginForm(event) {
    const username = document.getElementById('username').value.trim(); // 'username' refers to username
    const password = document.getElementById('password').value.trim();

    if (!username || !password) {
        alert('Both Username and Password are required!');
        event.preventDefault(); // Prevent form submission
    }
}

// Function to validate the signup form
function validateSignupForm(event) {
    const username = document.getElementById('username').value.trim(); // 'username' refers to username
    const password = document.getElementById('password').value.trim();
    const rePassword = document.getElementById('re-password').value.trim(); // 're-password' refers to re_password

    if (!username || !password || !rePassword) {
        alert('All fields are required!');
        event.preventDefault(); // Prevent form submission
    } else if (password !== rePassword) {
        alert('Passwords do not match!');
        event.preventDefault(); // Prevent form submission
    }
}

// Detect the current page and add appropriate event listeners
document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector('form[action=""]'); // Login form
    const signupForm = document.querySelector('form[action="/signup/"]'); // Signup form

    if (loginForm) {
        loginForm.addEventListener('submit', validateLoginForm);
    }

    if (signupForm) {
        signupForm.addEventListener('submit', validateSignupForm);
    }
});
