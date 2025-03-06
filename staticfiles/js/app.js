setTimeout(function () {
    let messages = document.querySelectorAll('.alert-message');
    messages.forEach(function (message) {
        message.style.display = 'none';
    });
}, 3000);