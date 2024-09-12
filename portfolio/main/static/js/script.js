window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
  
    // If the page is scrolled more than 50px, add the shadow
    if (window.scrollY > 50) {
      navbar.classList.add('shadow');
    } else {
      navbar.classList.remove('shadow');
    }
  });
  