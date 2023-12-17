function search() {
  var searchInputValue = document.getElementById('searchInput').value;
  console.log('Пошук за словом: ' + searchInputValue);
  $('#searchModal').modal('hide');
}

var dropdownMenu = document.getElementById('dropdownMenu');
var dropdownButton = dropdownMenu.querySelector('.nav-link');

dropdownButton.addEventListener('click', function (e) {
  e.stopPropagation(); // Зупинити подальшу передачу кліків, щоб не спричиняти закриття

  var dropdownMenu = this.nextElementSibling;
  dropdownMenu.classList.toggle('show');

  document.addEventListener('click', closeDropdownMenu);
});

function closeDropdownMenu() {
  var dropdownMenu = document.querySelector('.dropdown-menu.show');
  if (dropdownMenu) {
    dropdownMenu.classList.remove('show');
    document.removeEventListener('click', closeDropdownMenu);
  }
}