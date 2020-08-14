function myFunction() {
    var position = $('#myDropdown');

    position.offset({});
    document.getElementById("myDropdown").classList.toggle("show");
}

$(document).ready(function () {
    window.onclick = function (e) {
        if (!e.target.matches('.dropbtn')) {
            var myDropdown = document.getElementById("myDropdown");

            if (myDropdown.classList.contains('show')) {
                myDropdown.classList.remove('show');
            }
        }
    }
});